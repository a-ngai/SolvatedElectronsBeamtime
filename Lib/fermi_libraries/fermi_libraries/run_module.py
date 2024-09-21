import os
import warnings
import time
import logging
import re
import hashlib
import numpy as np
import h5py
from functools import wraps
from multiprocessing import cpu_count, pool
from scipy.interpolate import interp1d
from .dictionary_search import SearchClass, search_symbols as default_search_symbols
from .common_functions import single_pass_moment_sums

# warnings.simplefilter('always', DeprecationWarning)

def _make_zero_inner(array):
    old_shape = np.array(np.shape(array))
    temp_shape = old_shape[1:]
    return np.zeros(temp_shape)

def _make_zero_shape(array):
    old_shape = np.array(np.shape(array))
    temp_shape = old_shape[:]
    temp_shape[0] = 0
    return np.zeros(temp_shape)

class KeywordWarning(UserWarning):
    pass

def default_keyword_functions(keyword, alias_func, DictionaryObject):
    '''
    Simplest look-up function for a dictionary(-like) object.

    Parameters
    ----------
    keyword : TYPE
        DESCRIPTION.
    alias_func : TYPE
        DESCRIPTION.
    DictionaryObject : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    return DictionaryObject[alias_func(keyword)]

def get_cache_filepath(outdir, filepaths, args, datanames, use_cache=True):
    idf = hashlib.md5(str(args).encode()).hexdigest()
    filepath = f'{outdir}/{idf}.npz' # cache file unique to all arguments
    return filepath

def get_cache_filepath_h5(outdir, filepaths, args, datanames, use_cache=True):
    idf = hashlib.md5(str(args).encode()).hexdigest()
    filepath = f'{outdir}/{idf}.h5' # cache file unique to all arguments
    return filepath

def cache_function(outdir, filepaths, args, datanames, use_cache=True):
    """
    Intended to be used for functions which processes large amounts of data e.g.
    average_run_data.
    
    IMPORTANT: it checks the creation time of the cache, and remakes the cache
    if the creation time of the filepaths are later than that cache creation
    time.
    """

    if not os.path.exists(outdir):
        os.mkdir(outdir)
    idf = hashlib.md5(str(args).encode()).hexdigest()
    cachefile = get_cache_filepath(outdir, filepaths, args, datanames, use_cache=use_cache)
    if os.path.exists(cachefile):

        # latest = sorted(filepaths)[0]
        # rawtime = os.path.getmtime(latest)
        # cachetime = os.path.getmtime(cachefile)
        # # load cached data if it is up-to-date
        # if (cachetime > rawtime) and use_cache:

        if use_cache:

            try:
                loaded_dict = np.load(cachefile, allow_pickle=True)
                output = [loaded_dict[name] for name in datanames]
                return output
            except KeyError as e:
                print(f'{e}, remaking the cache file')

    return cachefile



def function_for_imap(filepath, run_object_attributes, dataname, back_sep=True, slu_sep=True, slice_range=None, rules=[None,]):
    run_object = Run([])
    for name, value in run_object_attributes:
        setattr(run_object, name, value)
    data_sum, data_count = list(run_object.yield_sums_counts_filedata(
        dataname, back_sep=back_sep, slu_sep=slu_sep,
        slice_range=slice_range, rules=rules, filepaths=[filepath,]))[0]
    return data_sum, data_count

from itertools import repeat

def apply_args_and_kwargs(fn, args, kwargs):
    return fn(*args, **kwargs)

def starmap_with_kwargs(pool, fn, args_iter, kwargs_iter):
    args_for_starmap = zip(repeat(fn), args_iter, kwargs_iter)
    return pool.starmap(apply_args_and_kwargs, args_for_starmap)


class Run:
    '''
    Each Run class is linked to one HDF5 file. However, this
    file is not accessed/loaded until its data is explicitly needed, and
    even then not the whole file.
    '''

    def __init__(self, hdf5_filepaths,
                 alias_dict={}, search_symbols=default_search_symbols,
                 keyword_functions=default_keyword_functions,
                 background_offset=0):
        if isinstance(hdf5_filepaths, str):
            hdf5_filepaths = [hdf5_filepaths,]
        self.filepaths = hdf5_filepaths
        self.kept_data = {}
        self.alias_dict = alias_dict
        self.search_symbols = search_symbols
        self.keyword_functions = keyword_functions
        self.background_offset = background_offset
        self.background_periods = None
        self.slu_offset = None
        self.slu_period = np.array([[2.,]])

    def keyword_alias(self, keyword):
        try:
            return self.alias_dict[keyword]
        except:
            return keyword

    def _alias(func):
        @wraps(func)
        def _name_wrapped_func(self, *args, **kwargs):
            # assume name is the last argument (sometimes 'self' is the first argument, can't
            # be prevented!)
            name = args[-1]
            alias = self.keyword_alias(name)
            new_args = list(args)
            new_args[-1] = alias
            return func(self,*new_args,**kwargs)
        return _name_wrapped_func

    @_alias
    def alias(self, name):
        return name

    @_alias
    def _check_background_split(self, check_name, data=None):
        '''
        Checks if the dataset can be split irebinningnto measurement and background,
        by matching the size of bunch_number list with the size of the
        check_name dataset.

        Parameters
        ----------
        check_name : str
            DESCRIPTION.

        Returns
        -------
        True if splitting possible, else False.
        '''

        for filepath in self.filepaths[:1]:
            with h5py.File(filepath,'r') as file:
                bunch_length = (file['bunches'].shape)[0]
                if data is not None:
                    data_length = data.shape[0]
                else:
                    data_length = (file[check_name].shape)[0]
            if bunch_length != data_length:
                warnings.warn('dataset cannot be split into measurement and background, setting back_sep=False')
                return False

        return True

    def check_file_path(self):
        '''
        Checks if the file location is valid, and checks if the file can be
        loaded into a h5py.File object.

        Returns
        -------
        (invalid_paths, invalid_h5files) : tuple
            invalid_paths are where the filepath does not exist, and
            invalid_h5files are where the filepath exists, but cannot be
            loaded as an h5py.File object.

        '''

        valid_paths = []
        invalid_paths = []
        for path in self.filepaths:
            if not os.path.exists(path):  # check file location
                invalid_paths.append(path)
            else:
                valid_paths.append(path)

        valid_h5files = []
        invalid_h5files = []
        for path in valid_paths:
            try: # try loading the file into an h5py.File object
                with h5py.File(path) as file:
                    _ = file.keys()
                valid_h5files.append(path)
            except (FileNotFoundError, OSError):
                invalid_h5files.append(path)

        return invalid_paths, invalid_h5files

    @_alias
    def simple_load_data(self, name, filepaths=None):
        '''
        Simplest way to extract data from the HDF5 files. Only here in case other methods break.
        '''

        if filepaths is None:
            filepaths = self.filepaths

        data = []
        for filepath in filepaths:
            with h5py.File(filepath,'r') as file:
                data.append(file[name][()])

        return data

    def get_background_period(self, filepaths=None):
        """
        Returns the background period found in the files in filepaths. If not found, returns
        a default value
        """
        if self.background_periods is None or len(self.background_periods)==0:
            try:
                self.background_periods = np.array(self.simple_load_data(
                    'Background_Period',filepaths=filepaths),dtype=float)
            except (FileNotFoundError, OSError):
                warnings.warn(f"Cannot find dataset 'Background_Period' in one of ({filepaths})\n\n\
                        Setting period to (-1)", KeywordWarning)
                self.background_periods = np.zeros(shape=(len(filepaths),)) - 1

        return self.background_periods

    def background_from_bunches(self, bunches, filepaths=None):
        """
        Makes a boolean mask based to discriminate foreground from background shots, using the
        background period, and the bunch number
        """

        background_period = self.get_background_period(filepaths)
        background_period[background_period<0]=np.max(bunches)+1
        background_offset = self.background_offset
        is_background_bool = np.array([(
            bunches-background_offset)%period==0 for period in background_period])
        return is_background_bool

    def slu_from_bunches(self, bunches, filepaths=None):
        '''
        Similar to background_from_bunches(). If there is no offset specified (i.e. self.slu_offset
        is None), this attempts to detect the offset of the SLU, and then set it in the 
        Run attributes.

        Note! This automatic detection of the SLU offset might not match up with the actual shot
        number; we've had problems where the synchronization of the slu and the other data
        didn't match up (as of 2022)!
        

        Parameters
        ----------
        bunches : TYPE
            DESCRIPTION.
        filepaths : TYPE, optional
            DESCRIPTION. The default is None.
        auto : bool, optional
            If True, the SLU parity is determined automatically. If there is
            a problem with it, set to False and determine the parity after
            the fact.

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''

        background_period = self.slu_period
        # background_period = np.array(self.simple_load_data('Background_Period'),dtype=float)
        background_period[background_period<0]=np.inf
        background_period = background_period[0]  # assume it is the same for all files within a run
        if self.slu_offset is None and background_period != np.inf:
            background_period = int(np.squeeze(background_period))
            test_slu = self.simple_load_data('slu', filepaths=filepaths)
            offset_intensity = np.array([
                [
                np.average(filedata[offset::background_period])
                    for offset in range(background_period)
                    ] for filedata in test_slu])
            background_offset = np.where(
                    offset_intensity == np.min(offset_intensity,axis=1)[:,np.newaxis]
                    )[1][:,np.newaxis]
        else:
            background_offset = self.slu_offset
        is_background_bool = (np.arange(len(bunches))-background_offset)%background_period==0

        return is_background_bool

    @_alias
    def yield_file_data(self, name, back_sep=False, slu_sep=False, slice_range=None, rules=[None,], filepaths=None, supress_warnings=True):
        '''

        This is the base method for compiling data from the raw data files.

        Filedata will be yielded in the following form:

                yield (
                    [rule1_meas, rule2_meas,...,ruleN_meas],
                    [rule1_back, rule2_back,...,ruleN_back],
                    [rule1_SLU, rule2_SLU,...,ruleN_SLU],
                    [rule1_backSLU, rule2_backSLU,...,ruleN_backSLU],
                    )

        Parameters
        ----------
        name : TYPE
            DESCRIPTION.
        back_sep : TYPE, optional
            DESCRIPTION. The default is False.
        slu_sep : TYPE, optional
            DESCRIPTION. The default is False.
        slice_range : TYPE, optional
            DESCRIPTION. The default is None.
        rule : TYPE, optional
            DESCRIPTION. The default is None.
        filepaths : TYPE, optional
            DESCRIPTION. The default is None.

        Raises
        ------
        Exception
            DESCRIPTION.

        Yields
        ------
        TYPE
            DESCRIPTION.
        TYPE
            DESCRIPTION.
        TYPE
            DESCRIPTION.
        TYPE
            DESCRIPTION.

        '''
        search_symbols = self.search_symbols

        back_sep_warning_flag = True
        error_in_all_files_flag = True  # if there is a problem loading a single file out of many, we will skip it
        if filepaths is None:
            filepaths = self.filepaths
        for filepath in filepaths:
            fore_out = []
            back_out = []
            fore_no_slu_out = []
            back_no_slu_out = []
            with h5py.File(filepath,'r') as file:
                try:
                    h5_data = self.keyword_functions(name, lambda x:x, file)
                except KeyError as e:
                    logging.warning(f'Error getting data with keyword ({name})) in file ({filepath}), skipping. Error message: {e}')
                    if filepath == self.filepaths[-1] and error_in_all_files_flag:
                        filepaths_string = '    ''\n    '.join(self.filepaths)
                        raise Exception(f"No data found with keyword ({name}).\nFiles checked:\
\n    {filepaths_string}.\nError message: {e}")
                    continue
                
                error_in_all_files_flag = False
                
                h5_dim = h5_data.ndim
                h5_shape = h5_data.shape

                if slice_range is None:
                    slice_after_bunches = tuple(slice(None,None,1) for _ in range(1, h5_dim))
                else:
                    slice_after_bunches = tuple([slice(None,None,1),]
                                                + [slice(i,j,k) for i,j,k in slice_range])
                if len(slice_after_bunches)>h5_dim:
                    raise Exception(f'slice_range has length ({len(slice_after_bunches)}) larger than the data dimension ({h5_dim})')

                # we must load the while data; the chunks from FERMI data are too large, and
                # slicing from the hdf5 data is actually much slower because of this!
                h5_data = self.keyword_functions(name, lambda x:x, file)[()]
                h5_data = h5_data[slice_after_bunches]

                # we will process all data as if everything were organized into shots.
                # Including the background_period; e.g. this is a 0-dim numpy array,
                # so we will yield/return it as a 2-dim numpy array.
                if h5_dim == 0:  # no such thing as slicing operations here
                    reshape_data = lambda data: np.array([[np.array(data),],])
                    for _, rule in enumerate(rules):
                        fore_out.append(reshape_data(h5_data))
                        back_out.append(0*reshape_data(h5_data))
                        fore_no_slu_out.append(0*reshape_data(h5_data))
                        back_no_slu_out.append(0*reshape_data(h5_data))
                    if back_sep and back_sep_warning_flag:
                        warnings.warn(f'(back_sep=True) keyword not valid for this dataframe ({name})',
                                      KeywordWarning)
                        logging.warning(f'back_sep keyword not valid for this dataframe ({name})')
                        back_sep_warning_flag=False
                    yield fore_out, back_out, fore_no_slu_out, back_no_slu_out
                    continue

                if h5_dim == 1 and h5_shape[0] != file['bunches'].shape[0]:
                    reshape_data = lambda data: data[np.newaxis,:]
                    for _, rule in enumerate(rules):
                        fore_out.append(reshape_data(h5_data))
                        back_out.append(0*reshape_data(h5_data))
                        fore_no_slu_out.append(0*reshape_data(h5_data))
                        back_no_slu_out.append(0*reshape_data(h5_data))
                    if back_sep and back_sep_warning_flag:
                        warnings.warn(f'back_sep keyword not valid for this dataframe ({name})',
                                      KeywordWarning)
                        logging.warning(f'back_sep keyword not valid for this dataframe ({name})')
                        back_sep_warning_flag=False
                    yield fore_out, back_out, fore_no_slu_out, back_no_slu_out
                    continue

                if h5_dim == 1 and h5_shape[0] == file['bunches'].shape[0]:
                    reshape_data = lambda data: data[:,np.newaxis]
                else:
                    reshape_data = lambda data: data

                bunches = np.array(file['bunches'][()])

                is_background=self.background_from_bunches(bunches, filepaths=[filepath,])[0]
                is_slu_off=self.slu_from_bunches(bunches, filepaths=[filepath,])[0]

                def warnings_for_empty_sets(input_tuple, rule, background_period,
                                            back_sep=None,slu_sep=None, supress_warnings=True):
                    fore, back, fore_no_slu, back_no_slu = input_tuple
                    empty_array = None
                    for array in [fore,back,fore_no_slu,back_no_slu]:
                        if len(array)!=0:
                            empty_array = array[0:0]*0
                            break
                    if empty_array is None:
                        empty_array = fore[:1]
                        if not supress_warnings:
                            warnings.warn(
                                f'All arrays (fore, back, fore_no_slu, back_no_slu) are\
                                        empty! rule ({rule})')

                    if len(fore)==0:
                        if not supress_warnings:
                            warnings.warn(
                                f'no foreground shots found with background period\
                                        ({background_period}) and rule ({rule})')
                        fore = empty_array
                    if len(back)==0:
                        if back_sep and not supress_warnings:
                            warnings.warn(f'no background shots found with background period\
                                    ({background_period}) and rule ({rule})')
                        back = empty_array
                    if len(fore_no_slu)==0:
                        if slu_sep and not supress_warnings:
                            warnings.warn(f'no foreground+noSLU shots found with background period\
                                    ({background_period}) and rule ({rule})')
                        fore_no_slu = empty_array
                    if len(back_no_slu)==0:
                        if back_sep and slu_sep and not supress_warnings:
                            warnings.warn(f'no background+noSLU shots found with background period\
                                    ({background_period}) and rule ({rule})')
                        back_no_slu = empty_array
                    return fore, back, fore_no_slu, back_no_slu

                for rule in rules:

                    filter_search = SearchClass(
                            rule,
                            operator_dict=search_symbols['operator_dict'],
                            function_dict=search_symbols['function_dict'],
                            context_dict=search_symbols['context_dict'],
                            )

                    alias_func = lambda keyword: self.keyword_alias(keyword)
                    input_function = lambda keyword: self.keyword_functions(keyword, alias_func, file)
                    rule_crit = filter_search.evaluate(input_function) + bunches!=bunches  # gets a bool array, with the shape of the bunches in the first dim

                    if back_sep and slu_sep and self._check_background_split(name, data=h5_data):
                        fore_slice = tuple([~is_background * ~is_slu_off * rule_crit,])
                        back_slice = tuple([is_background * ~is_slu_off * rule_crit,])
                        fore_no_slu_slice = tuple([~is_background * is_slu_off * rule_crit,])
                        back_no_slu_slice = tuple([is_background * is_slu_off * rule_crit,])

                        reshaped_data = reshape_data(h5_data)
                        fore = reshaped_data[fore_slice]
                        back = reshaped_data[back_slice]
                        fore_no_slu= reshaped_data[fore_no_slu_slice]
                        back_no_slu = reshaped_data[back_no_slu_slice]

                        fore, back, fore_no_slu, back_no_slu = warnings_for_empty_sets(
                                (fore, back, fore_no_slu, back_no_slu), rule,
                                self.get_background_period(filepaths), back_sep=back_sep,slu_sep=slu_sep)

                    elif back_sep and not slu_sep and self._check_background_split(name, data=h5_data):

                        fore_slice = tuple([~is_background  * rule_crit,])
                        back_slice = tuple([is_background  * rule_crit,])

                        reshaped_data = reshape_data(h5_data)
                        fore = reshaped_data[fore_slice]
                        back = reshaped_data[back_slice]

                        fore, back, fore_no_slu, back_no_slu = warnings_for_empty_sets(
                                (fore, back, [], []), rule,
                                self.get_background_period(filepaths), back_sep=back_sep,slu_sep=slu_sep)

                    elif not back_sep and slu_sep and self._check_background_split(name, data=h5_data):
                        fore_slice = tuple([ ~is_slu_off * rule_crit,])
                        fore_no_slu_slice = tuple([ is_slu_off * rule_crit,])

                        reshaped_data = reshape_data(h5_data)

                        fore = reshaped_data[fore_slice]
                        fore_no_slu = reshaped_data[fore_no_slu_slice]

                        fore, back, fore_no_slu, back_no_slu = warnings_for_empty_sets(
                                (fore, [], fore_no_slu, []), rule,
                                self.get_background_period(filepaths), back_sep=back_sep,slu_sep=slu_sep)

                    else:
                        if back_sep:
                            warnings.warn(f'back_sep keyword not valid for this dataframe ({name})')
                        if slu_sep:
                            warnings.warn(f'slu_sep keyword not valid for this dataframe ({name})')
                        all_slice = tuple([(is_background+~is_background)*rule_crit,])
                        fore = reshape_data(h5_data[all_slice])

                        fore, back, fore_no_slu, back_no_slu = warnings_for_empty_sets(
                                (fore, [], [], []), rule,
                                self.get_background_period(filepaths), back_sep=back_sep,slu_sep=slu_sep)

                    fore_out.append(fore)
                    back_out.append(back)
                    fore_no_slu_out.append(fore_no_slu)
                    back_no_slu_out.append(back_no_slu)

            yield fore_out, back_out, fore_no_slu_out, back_no_slu_out

    @_alias
    def load_data(self, name, back_sep=False, slu_sep=False, slice_range=None,
                 rules=[None,], filepaths=None):

        compiled_data = []
        for file_data in self.yield_file_data(name, back_sep=back_sep, slu_sep=slu_sep,
                                       slice_range=slice_range,
                                       rules=rules, filepaths=filepaths):
            for i, split_data in enumerate(file_data):
                if len(compiled_data)<=i:
                    compiled_data.append([])
                for j, rule_data in enumerate(split_data):
                    if len(compiled_data[i])<=j:
                        compiled_data[i].append([])
                    compiled_data[j].extend(rule_data)
        return compiled_data

    @_alias
    def yield_sums_counts_filedata(self, dataname, back_sep=False, slu_sep=False, slice_range=None, rules=[None,], filepaths=None):
        '''
        Helps with computing the file-by-file or entire run average of the
        datasets.

        Output axes = (files, sum/counts, conditions,  rules)

        Parameters
        ----------
        dataname : TYPE
            DESCRIPTION.
        back_sep : TYPE, optional
            DESCRIPTION. The default is False.
        slice_range : TYPE, optional
            DESCRIPTION. The default is None.
        rule : TYPE, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        file_data_sums : TYPE
            DESCRIPTION.
        file_data_counters : TYPE
            DESCRIPTION.

        '''

        for _, file_level_data in enumerate(self.yield_file_data(
            dataname, back_sep=back_sep, slu_sep=slu_sep,
            slice_range=slice_range, rules=rules, filepaths=filepaths)):

            file_data_sums = []
            file_data_counts = []
            for split_data in file_level_data:
                split_data_sums = []
                split_data_counts = []
                for rule_data in split_data:
                    rule_data_sum = np.sum(rule_data,axis=0)
                    rule_data_count = len(rule_data)

                    split_data_sums.append(rule_data_sum)
                    split_data_counts.append(rule_data_count)

                file_data_sums.append(split_data_sums)
                file_data_counts.append(split_data_counts)

            yield file_data_sums, file_data_counts

    @_alias
    def yield_moment_sums_filedata(self, dataname, back_sep=False, slu_sep=False, slice_range=None, rules=[None,], filepaths=None,
                                         filter1=None, filter2=None):
        '''
        Helps with computing the file-by-file statistics of the
        datasets.

        Output axes = (files, covar/sum/counts, conditions,  rules)

        Parameters
        ----------
        dataname : TYPE
            DESCRIPTION.
        back_sep : TYPE, optional
            DESCRIPTION. The default is False.
        slice_range : TYPE, optional
            DESCRIPTION. The default is None.
        rule : TYPE, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        file_data_sums : TYPE
            DESCRIPTION.
        file_data_counters : TYPE
            DESCRIPTION.

        '''
        if filter1 is None:
            filter1 = lambda x: x
        if filter2 is None:
            filter2 = lambda x: x

        for _, file_level_data in enumerate(self.yield_file_data(
            dataname, back_sep=back_sep, slu_sep=slu_sep,
            slice_range=slice_range, rules=rules, filepaths=filepaths)):

            file_data_covar, file_data_sum1, file_data_sum2, file_data_counts = [], [], [], []
            for split_data in file_level_data:
                split_data_covar, split_data_sum1, split_data_sum2, split_data_counts = [], [], [], []
                for rule_data in split_data:
                    if len(rule_data)>0:
                        data_generator = (line for line in rule_data)
                        weight = 1
                    else:
                        temp_data_shape = list(np.shape(rule_data))
                        temp_data_shape[0]=1
                        temp_data = np.zeros(shape=temp_data_shape)
                        data_generator = (line for line in temp_data)
                        weight = 0
                    AnalysisDict = single_pass_moment_sums(
                        data_generator,
                        filter1=filter1, filter2=filter2,
                        _weight=weight)
                    rule_data_covar = AnalysisDict['covar_sum']
                    rule_data_sum1 = AnalysisDict['x_sum']
                    rule_data_sum2 = AnalysisDict['y_sum']
                    rule_data_count = AnalysisDict['count']

                    split_data_covar.append(rule_data_covar)
                    split_data_sum1.append(rule_data_sum1)
                    split_data_sum2.append(rule_data_sum2)
                    split_data_counts.append(rule_data_count)

                file_data_covar.append(split_data_covar)
                file_data_sum1.append(split_data_sum1)
                file_data_sum2.append(split_data_sum2)
                file_data_counts.append(split_data_counts)

            yield file_data_covar, file_data_sum1, file_data_sum2, file_data_counts

    @_alias
    def give_sums_counts_filedata(self, dataname, back_sep=False, slu_sep=False, slice_range=None, rules=[None,], filepaths=None):
        '''
        Similar to Run.yield_sums_counts_filedata(), but this method is a function and not a
        generator. Output axes are adapted accordingly.

        Output axes: (sums/counts, files, conditions, rules)
        '''

        output_sums = []
        output_counts = []
        for data_sums, data_counts in self.yield_sums_counts_filedata(
            dataname, back_sep=back_sep, slu_sep=slu_sep,
            slice_range=slice_range, rules=rules, filepaths=filepaths):

            output_sums.append(data_sums)
            output_counts.append(data_counts)

        return output_sums, output_counts

    @_alias
    def give_moment_sums_filedata(self, dataname, back_sep=False, slu_sep=False, slice_range=None, rules=[None,], filepaths=None,
                                        filter1=None, filter2=None):
        '''
        Similar to Run.yield_sums_counts_filedata(), but this method is a function and not a
        generator. Output axes are adapted accordingly.

        Output axes: (sums/counts, files, conditions, rules)
        '''

        output_covar, output_sum1, output_sum2, output_counts = [], [], [], []
        for data_covar, data_sum1, data_sum2, data_counts in self.yield_moment_sums_filedata(
            dataname, back_sep=back_sep, slu_sep=slu_sep,
            slice_range=slice_range, rules=rules, filepaths=filepaths,
            filter1=filter1, filter2=filter2):

            output_covar.append(data_covar)
            output_sum1.append(data_sum1)
            output_sum2.append(data_sum2)
            output_counts.append(data_counts)

        return output_covar, output_sum1, output_sum2, output_counts

    @_alias
    def give_rundata(self, dataname, back_sep=False, slu_sep=False, slice_range=None,
                     rules=[None,], filepaths=None, use_cache=False, make_cache=False,
                     filter1=None):
        '''
        Give the raw data, with the nice "back_sep", "slu_sep", "slice_range", "rules" keywords.
        The individual files of the Run are concatenated.

        IMPORTANT: don't use this for Runs with many files; this function loads everything into memory!!!

        Output axes: (conditions, rules)
        '''

        if filter1 is None:
            filter1 = lambda x: x

        if self.filepaths:
            outdir = self.filepaths[0].split('/rawdata/')[0] + '/work/get_rundata_cache'
            args = (filepaths, dataname, back_sep, slu_sep, slice_range, rules, filter1)
            cache_return = cache_function(outdir, self.filepaths, args, ['rundata',], use_cache=use_cache)
            if not isinstance(cache_return, str):
                return cache_return[0]


        rundata_collect = []
        for file_level_data in self.yield_file_data(
            dataname, back_sep=back_sep, slu_sep=slu_sep,
            slice_range=slice_range, rules=rules, filepaths=filepaths):

            for i, split_data in enumerate(file_level_data):
                if len(rundata_collect)<=i:
                    rundata_collect.append([])

                for j, rule_data in enumerate(split_data):
                    if len(rundata_collect[i])<=j:
                        rundata_collect[i].append([])

                    def _get_data_from_filter(data, data_filter):
                        ''' This allows filtering of non-zero AND zero-size arrays. '''

                        filtered_data = [filter1(line) for line in data]


                        if len(data)==0:
                            filtered_data = _make_zero_shape(np.array([filter1(_make_zero_inner(data)),]))

                        return filtered_data

                    rundata_collect[i][j].append(_get_data_from_filter(rule_data, filter1))
        for i, _ in enumerate(rundata_collect):
            for j, _ in enumerate(rundata_collect[0]):
                rundata_collect[i][j] = np.concatenate(rundata_collect[i][j],axis=0)

        if make_cache and self.filepaths:
            np.savez_compressed(cache_return,
                     rundata=np.array(rundata_collect, dtype=object),
                     )

        return rundata_collect

    @_alias
    def average_run_data_weights(self, dataname, back_sep=False, slu_sep=False, slice_range=None,
                                 rules=[None,], use_cache=True, make_cache=True, _filepaths=None,
                                 num_files_per_cache=None, 
                                 _save_incomplete_cache=False, _save_total_cache=True):
        '''
        Output axes: (sum/counts, conditions, rules, data)
        '''
        if _filepaths is None:
            filepaths = self.filepaths
        else:
            filepaths = _filepaths
        
        # checking possible caches
        _files_per_cache = len(filepaths)
        look_for_filepaths = filepaths[:num_files_per_cache]
        outdir = filepaths[0].split('/rawdata/')[0] + '/work/average_run_data_weights_cache'
        args = (filepaths, dataname, back_sep, slu_sep, slice_range, rules)
        cache_filepath = get_cache_filepath(
                        outdir, look_for_filepaths, args, ['rundata','runweights'], use_cache=use_cache)
        cache_found = os.path.exists(cache_filepath)
        if num_files_per_cache is not None: _files_per_cache = num_files_per_cache
        
        # call recursively, but only on subsets of all files
        if (_filepaths is None) and (num_files_per_cache is not None):
            num_files = len(filepaths)
            num_blocks = int(np.ceil(num_files / _files_per_cache))
            subsets_of_filepaths = [filepaths[i*_files_per_cache:(i+1)*_files_per_cache] for i in range(num_blocks)]
            partial_run_avg = []
            partial_run_weights = []
            for subset in subsets_of_filepaths:
                cache_is_incomplete = (len(subset)!=_files_per_cache)
                save_if_incomplete = _save_incomplete_cache and cache_is_incomplete
                save_part_cache = make_cache and (not cache_is_incomplete or save_if_incomplete)
                save_incomplete_cache = make_cache * _save_incomplete_cache * cache_is_incomplete
                block_avg, block_weights = self.average_run_data_weights(
                    dataname, back_sep=back_sep, slu_sep=slu_sep, slice_range=slice_range,
                    rules=rules, use_cache=use_cache, make_cache=save_part_cache, _filepaths=subset,
                    num_files_per_cache=None,
                    _save_incomplete_cache=True # possibly a problem? save_in_complete_cache variable is unused...
                )
                partial_run_avg.append(block_avg)
                partial_run_weights.append(block_weights)

            run_file_weights = np.array(partial_run_weights) 
            run_file_avg = np.array(partial_run_avg)

            data_dim = np.ndim(run_file_avg)
            weights_dim = np.ndim(run_file_weights)
            match_dim_weights = np.expand_dims(run_file_weights, axis=[-(i+1) for i in range(data_dim-weights_dim)])

            run_file_sum = run_file_avg * match_dim_weights
            run_file_data = run_file_sum
            
            cache_return = cache_function(outdir, self.filepaths, args, ['rundata','runweights'], use_cache=False)

        # this is the original path without recursion
        else:
            if filepaths:
                outdir = filepaths[0].split('/rawdata/')[0] + '/work/average_run_data_weights_cache'
                args = (filepaths, dataname, back_sep, slu_sep, slice_range, rules)
                cache_return = cache_function(outdir, filepaths, args, ['rundata','runweights'], use_cache=use_cache)
                if not isinstance(cache_return, str):
                    # print(f'found a cache with {len(filepaths)} files')
                    return cache_return

        compiled_data = []
        compiled_count = []
        run_average = []
        run_weight = []
        if num_files_per_cache is None:
            run_file_data, run_file_weights = self.give_sums_counts_filedata(
                                    dataname, back_sep=back_sep, slu_sep=slu_sep,
                                    slice_range=slice_range, rules=rules)
            
        # print()
        # print()
        # print()
        # print(f'num_files_per_cache: {num_files_per_cache}')
        # print(f'filepaths: {filepaths}')
        # print(f'_filepaths: {_filepaths}')
        # print()
        # print()
        # print()

        for filedata_sum, filedata_count in zip(run_file_data, run_file_weights):
            for i, (split_sum, split_count) in enumerate(zip(filedata_sum, filedata_count)):
                if len(compiled_data)<=i:
                    compiled_data.append([])
                    compiled_count.append([])
                compiled_data[i].append(split_sum)
                compiled_count[i].append(split_count)
        for split_data, split_count in zip(compiled_data, compiled_count):
            data_dim = np.ndim(split_data)
            match_dim_split_count = np.expand_dims(split_count, axis=[-(i+1) for i in range(data_dim-2)])
            divisor = np.sum(match_dim_split_count, axis=0)
            divisor[divisor==0]=1
            run_average.append(np.sum(split_data, axis=0)/divisor)
            run_weight.append(np.sum(split_count, axis=0))
        
        if make_cache and (_filepaths is not None) and filepaths:
            rundata = np.array(run_average, dtype=float)
            runweights = np.array(run_weight, dtype=int)
            print(f'_filepath is list: saving cache with {len(filepaths)} files')

            np.savez_compressed(cache_return,
                     rundata=rundata,
                     runweights=runweights,
                     )

        elif make_cache and (_filepaths is None) and filepaths and _save_total_cache:
            rundata = np.array(run_average, dtype=float)
            runweights = np.array(run_weight, dtype=int)
            print(f'_filepath is None: saving cache with {len(filepaths)} files')

            np.savez_compressed(cache_return,
                     rundata=rundata,
                     runweights=runweights,
                     )
            
            # h5_filepath = get_cache_filepath_h5(outdir, filepaths, args, ['rundata','runweights'])
            # with h5py.File(h5_filepath, 'w') as f:
            #     f.create_dataset('rundata', data=rundata, chunks=rundata.shape,
            #             compression='gzip', compression_opts=5)
            #     f.create_dataset('runweights', data=runweights, chunks=runweights.shape,
            #             compression='gzip', compression_opts=5)

        return run_average, run_weight

    @_alias
    def give_moment_sums_rundata(self, dataname, back_sep=False, slu_sep=False, slice_range=None,
                                 rules=[None,], use_cache=True, make_cache=True,
                                filter1=None, filter2=None, _filepaths=None):
        '''
        Output axes: (sum/counts, conditions, rules, data)
        '''
        if _filepaths is None:
            filepaths = self.filepaths
        else:
            filepaths = _filepaths

        if self.filepaths:
            outdir = self.filepaths[0].split('/rawdata/')[0] + '/work/give_moment_sums_rundata_cache'
            args = (filepaths, dataname, back_sep, slu_sep, slice_range, rules)
            cache_return = cache_function(outdir, self.filepaths, args, ['runcovar','runsum1', 'runsum2','runweights'], use_cache=use_cache)
            if not isinstance(cache_return, str):
                warnings.warn("Cache used! If this should not be the case, set the 'use_cache' keyword argument to False!")
                return cache_return

        run_file_covar, run_file_sum1, run_file_sum2, run_file_weights = self.give_moment_sums_filedata(
                                dataname, back_sep=back_sep, slu_sep=slu_sep,
                                slice_range=slice_range, rules=rules,
                                filter1=filter1, filter2=filter2)

        compiled_covar, compiled_sum1, compiled_sum2, compiled_count = [], [], [], []
        run_covar, run_sum1, run_sum2, run_weight = [], [], [], []
        for filedata_covar, filedata_sum1, filedata_sum2, filedata_count in zip(run_file_covar, run_file_sum1, run_file_sum2, run_file_weights):
            for i, (split_covar, split_sum1, split_sum2, split_count) in enumerate(zip(filedata_covar, filedata_sum1, filedata_sum2, filedata_count)):
                if len(compiled_sum1)<=i:
                    compiled_covar.append([])
                    compiled_sum1.append([])
                    compiled_sum2.append([])
                    compiled_count.append([])
                compiled_covar[i].append(split_covar)
                compiled_sum1[i].append(split_sum1)
                compiled_sum2[i].append(split_sum2)
                compiled_count[i].append(split_count)
        for split_covar, split_sum1, split_sum2, split_count in zip(compiled_covar, compiled_sum1, compiled_sum2, compiled_count):
            for i, (part_comoment_list, part_sum1_list, part_sum2_list, part_count_list) in enumerate(zip(split_covar, split_sum1, split_sum2, split_count)):
                if i==0:
                    temp_comoment = np.array(part_comoment_list[:])
                    temp_sum1 = np.array(part_sum1_list)
                    temp_sum2 = np.array(part_sum2_list)
                    temp_count = np.array(part_count_list)
                    continue

                part_comoment = np.array(part_comoment_list)
                part_sum1 = np.array(part_sum1_list)
                part_sum2 = np.array(part_sum2_list)
                part_count = np.array(part_count_list)

                temp_zero_part_nonzero = (temp_count==0)*(part_count!=0)
                temp_nonzero_part_nonzero = (temp_count!=0)*(part_count!=0)
                update_comoment = np.zeros(shape=np.shape(temp_comoment))
                update_comoment[temp_zero_part_nonzero] = part_comoment[temp_zero_part_nonzero]
                update_comoment[temp_nonzero_part_nonzero] = (
                    ((temp_count*part_count)/(temp_count+part_count))[:,np.newaxis,np.newaxis]
                    * (temp_sum1/temp_count[:,np.newaxis]-part_sum1/part_count[:,np.newaxis])[:,np.newaxis,:]
                    * (temp_sum2/temp_count[:,np.newaxis]-part_sum2/part_count[:,np.newaxis])[:,:,np.newaxis]
                )[temp_nonzero_part_nonzero]

                temp_comoment += update_comoment
                temp_sum1 += part_sum1
                temp_sum2 += part_sum2
                temp_count += part_count

            # run_covar.append(np.sum(split_covar, axis=0))
            # run_sum1.append(np.sum(split_sum1, axis=0))
            # run_sum2.append(np.sum(split_sum2, axis=0))
            # run_weight.append(np.sum(split_count, axis=0))

            run_covar.append(temp_comoment)
            run_sum1.append(temp_sum1)
            run_sum2.append(temp_sum2)
            run_weight.append(temp_count)

        if make_cache and self.filepaths:

            np.savez_compressed(cache_return, 
                     runcovar=np.array(run_covar, dtype=float), 
                     runsum1=np.array(run_sum1, dtype=float), 
                     runsum2=np.array(run_sum2, dtype=float), 
                     runweights=np.array(run_weight, dtype=int),
                     )

        return run_covar, run_sum1, run_sum2, run_weight

    @_alias
    def average_run_data(self, dataname, back_sep=False, slu_sep=False, slice_range=None,
                         rules=[None,], use_cache=True, make_cache=True, num_files_per_cache=None,
                         _save_total_cache=True):
        '''
        Same as Run.saverage_run_data_weights(), but just returning the "data" part of the tuple)

        Output axes: (conditions, rules, data)
        '''

        return self.average_run_data_weights(
                dataname, back_sep=back_sep, slu_sep=slu_sep,
                slice_range=slice_range, rules=rules,
                use_cache=use_cache, make_cache=make_cache,
                num_files_per_cache=num_files_per_cache, _save_total_cache=_save_total_cache)[0]


    @_alias
    def average_file_data(self, dataname, back_sep=False, slu_sep=False, slice_range=None, rules=[None,]):
        '''
        Output axes: (file, condition, rules, data)
        '''

        file_average = []
        run_sums, run_counters = self.give_sums_counts_filedata(
                dataname, back_sep=back_sep, slu_sep=slu_sep, slice_range=slice_range, rules=rules)
        for file_sums, file_counters in zip(run_sums, run_counters):
            for i, (split_sum, split_counter) in enumerate(zip(file_sums, file_counters)):
                if len(file_average)<=i:
                    file_average.append([])
                # keep this as a list, in case it is non-rectangular althought I don't expect it
                file_average[i].append([_sum/_counter for _sum, _counter in zip(split_sum, split_counter)])

        return file_average


class RunSets:
    '''

    This Class is intended to operate on multiple Run instances e.g.
    data averages, data over different Runs

    This class should be thought of as a "wrapper" around the Dictionary of
    Runs, in that it compiles data from their output (and runs them if
    data was not extracted yet), and then processes them here. Some of the
    functions could be done from the Run objects themsevles, but others e.g.
    time-delay vs covariance can only be done with multiple runs.
    '''

    def __init__(self, list_of_run_instances):
        self.run_instances = list_of_run_instances

    def keyword_alias(self, keyword):
        try:
            return self.alias_dict[keyword]
        except:
            return keyword

    def _alias(func):
        @wraps(func)
        def _name_wrapped_func(self, *args, **kwargs):
            # assume name is the last argument (sometimes 'self' is the first argument, can't
            # be prevented!)
            name = args[-1]
            alias = self.keyword_alias(name)
            new_args = list(args)
            new_args[-1] = alias
            return func(self,*new_args,**kwargs)
        return _name_wrapped_func

    @_alias
    def alias(self, name):
        return name

    def add(self, list_of_new_instances):
        '''
        Add more Run() instances. If an instance is already within the collection, it is ignored.
        '''
        for item2 in list_of_new_instances:
            if item2 not in self.run_instances:
                self.run_instances.append(item2)

    def remove(self, list_of_new_instances):
        '''
        Remove Run() instances. If an instance is not within the collection, it is ignored.
        '''
        for i, item1 in range(len(self.run_instances)-1,-1,-1):
            item1 = self.run_instances[i]
            for item2 in list_of_new_instances:
                if item1 is item2: list_of_new_instances.pop(i)

    @_alias
    def average_run_data_weights(self, dataname, back_sep=False, slu_sep=False, slice_range=None,
                                 rules=[None,], use_cache=True, make_cache=True,
                                 num_files_per_cache=None):
        '''
        Output has axes: (average/weights, condition, run, average)
        '''

        print(f'num_files_per_cache: {num_files_per_cache}')
        print(f'use_cache: {use_cache}')
        print(f'make_cache: {make_cache}')
        print(f'dataname: {dataname}')
        compiled_averages = []
        compiled_weights = []
        for i, run_instance in enumerate(self.run_instances):
            for j, (split_data, split_weights) in enumerate(
                    zip(*run_instance.average_run_data_weights(
                        dataname, back_sep=back_sep, slu_sep=slu_sep,
                        slice_range=slice_range, rules=rules,
                        use_cache=use_cache, make_cache=make_cache,
                        num_files_per_cache=num_files_per_cache, ))):

                if len(compiled_averages)<=j:
                    compiled_averages.append([])
                    compiled_weights.append([])
                compiled_averages[j].append(split_data)
                compiled_weights[j].append(split_weights)

        return compiled_averages, compiled_weights

    @_alias
    def average_run_data(self, dataname, back_sep=False, slu_sep=False, slice_range=None,
                         rules=[None,], use_cache=True, make_cache=True,
                         num_files_per_cache=None):
        return self.average_run_data_weights(dataname, back_sep=back_sep, slu_sep=slu_sep,
                                         slice_range=slice_range, rules=rules,
                                         use_cache=use_cache, make_cache=make_cache,
                                         num_files_per_cache=num_files_per_cache, )[0]

    @_alias
    def average_set_data_weights(self, dataname, back_sep=False, slu_sep=False, slice_range=None,
                                 rules=[None,], use_cache=True, make_cache=True,
                                 num_files_per_cache=None):

        run_averages, run_weights = self.average_run_data_weights(
                dataname, back_sep=back_sep, slu_sep=slu_sep,
                slice_range=slice_range, rules=rules,
                use_cache=use_cache, make_cache=make_cache,
                num_files_per_cache=num_files_per_cache, )

        set_averages = []
        set_weights = []
        for slice_averages, slice_weights in zip(run_averages, run_weights):
            avg = np.array(slice_averages)
            num = np.array(slice_weights)
            data_dim = np.ndim(avg)
            match_dim_num = np.expand_dims(num, axis=[-(i+1) for i in range(data_dim-2)])

            set_averages.append(
                    np.sum(avg * match_dim_num, axis=0) / np.sum(match_dim_num, axis=0))
            set_weights.append(np.sum(num, axis=0))

        return set_averages, set_weights

    @_alias
    def average_set_data(self, dataname, back_sep=False, slu_sep=False, slice_range=None,
                         rules=[None,], use_cache=True, make_cache=True):
        return self.average_set_data_weights(dataname=dataname, back_sep=back_sep, slu_sep=slu_sep,
                                             slice_range=slice_range, rules=rules,
                                             use_cache=use_cache, make_cache=make_cache)[0]


    @_alias
    def yield_file_data(self, name, back_sep=False, slu_sep=False, slice_range=None, rules=[None,]):
        '''
        For each hdf5 file in each of the Run instances in this object, a
        a dataset is yielded, i.e. not separated by Run objects! Similar to
        yield_rundata_generator, except for this Run-object separation.

        Parameters
        ----------
        name : str
            group name (or alias) of the desired dataset.
        back_sep : bool, optional
            DESCRIPTION. The default is False.
        slice_range : list, optional
            DESCRIPTION. The default is None.

        Yields
        ------
        data : tuple
            #data = (meas, back)
            #If the back_sep keyword is True, then data=(meas, back) is returned.
            #Otherwise, just data=meas is returned.
            
            axes = (file, rule, condition)

        '''
        for RunInstance in self.run_instances:
            for data in RunInstance.yield_file_data(name, back_sep=back_sep, slu_sep=slu_sep,
                                                    slice_range=slice_range, rules=rules):
                yield data

    @_alias
    def yield_rundata_filedata_generator(self, name, back_sep=False, slu_sep=False, slice_range=None, rules=[None,]):
        '''
        For each hdf5 file in each of the Run instances in this object, a
        a dataset is yielded.

        This yields generators (at Run-level) which each yield generators
        (at File-level).

        Parameters
        ----------
        name : str
            group name (or alias) of the desired dataset.
        back_sep : bool, optional
            DESCRIPTION. The default is False.
        slice_range : list, optional
            DESCRIPTION. The default is None.

        Yields
        ------
        data : tuple
            data = (meas, back)
            If the back_sep keyword is True, then data=(meas, back) is returned.
            Otherwise, just data=meas is returned

        '''
        for RunInstance in self.run_instances:
            yield RunInstance.yield_file_data(name, back_sep=back_sep, slu_sep=slu_sep,
                                              slice_range=slice_range, rules=rules)

    @_alias
    def give_rundata(self, name, back_sep=False, slu_sep=False, slice_range=None,
                     rules=[None,], use_cache=True, make_cache=True):
        '''
        Give the raw data, with the nice "back_sep", "slu_sep", "slice_range", "rules" keywords.
        The individual files of the Run are concatenated.

        Output axes: (conditions, runs, rules)
        '''

        output = []
        for j, run_instance in enumerate(self.run_instances):
            for i, split_data in enumerate(run_instance.give_rundata(
                name, back_sep=back_sep, slu_sep=slu_sep, slice_range=slice_range,
                rules=rules, use_cache=use_cache, make_cache=make_cache)):

                if len(output) <= i:
                    output.append([])
                for rule_data in split_data:
                    if len(output[i]) <= j:
                        output[i].append([])
                    output[i][j].append(rule_data)

        return output


class MultithreadRun(Run):

    def __init__(self, hdf5_filepaths,
                 alias_dict={}, search_symbols=default_search_symbols,
                 keyword_functions=default_keyword_functions,
                 background_offset=0):
        super().__init__(hdf5_filepaths,
                 alias_dict=alias_dict, search_symbols=search_symbols,
                 keyword_functions=keyword_functions,
                 background_offset=background_offset)
        self.num_cores = 1

    def _alias(func):
        @wraps(func)
        def _name_wrapped_func(self, *args, **kwargs):
            # assume name is the last argument (sometimes 'self' is the first argument, can't
            # be prevented!)
            name = args[-1]
            alias = self.keyword_alias(name)
            new_args = list(args)
            new_args[-1] = alias
            return func(self,*new_args,**kwargs)
        return _name_wrapped_func

    @_alias
    def alias(self, name):
        return name

    @_alias
    def average_run_data_weights(self, dataname, back_sep=False, slu_sep=False, slice_range=None,
                                rules=[None,], use_cache=True, make_cache=True, _filepaths=None,
                                num_files_per_cache=None, 
                                _save_incomplete_cache=False, _save_total_cache=False):
        '''
        Output axes: (sum/counts, conditions, rules, data)

        This follows a different logic compared to Run.average_run_data_weights(). We multi-thread every
        file regardless of num_files_per_cache, and only after they are returned, do we sort them back into
        blocks.
        '''


        if _filepaths is None:
            filepaths = self.filepaths
        else:
            filepaths = _filepaths

        num_files = len(filepaths)
        if num_files_per_cache is None: num_files_per_cache = num_files
        num_blocks = int(np.ceil(num_files / num_files_per_cache))
        subsets_of_filepaths = [filepaths[i*num_files_per_cache:(i+1)*num_files_per_cache] for i in range(num_blocks)]

        uncached_filepath_blocks = []
        blocks_data = []
        # checking possible caches
        for look_for_filepaths in subsets_of_filepaths:
            outdir = filepaths[0].split('/rawdata/')[0] + '/work/average_run_data_weights_cache'
            args = (look_for_filepaths, dataname, back_sep, slu_sep, slice_range, rules)
            cache_filepath = get_cache_filepath(
                outdir, look_for_filepaths, args, ['rundata','runweights'], use_cache=use_cache)
            cache_found = os.path.exists(cache_filepath)
            if cache_found and use_cache:
                cache_return = cache_function(outdir, look_for_filepaths, args, ['rundata','runweights'], use_cache=use_cache)
                if type(cache_return)==str:
                    raise Exception(f'cache is a string! ({cache_return})')
                blocks_data.append(cache_return)
            else:
                
                uncached_filepath_blocks.append(look_for_filepaths)

        from itertools import chain
        uncached_filepaths = list(chain.from_iterable(uncached_filepath_blocks))
        time_start = time.time()

        N_max_processes = self.num_cores

        if False:  # multithreading using threadpool
            threadpool = pool.ThreadPool(N_max_processes)
            pool_results = []
            callback_results = []
            for filepath in filepaths:

                def function_for_process():
                    data_sum, data_count = list(self.yield_sums_counts_filedata(
                        dataname, back_sep=back_sep, slu_sep=slu_sep,
                        slice_range=slice_range, rules=rules, filepaths=[filepath,]))[0]
                    return data_sum, data_count

                pool_results.append(threadpool.apply_async(
                        function_for_process,
                        args=(),
                        callback=callback_results))
            threadpool.close()
            threadpool.join()

            data_sums_counts = []
            for ProcessedObject in pool_results:
                data_sum, data_count = ProcessedObject.get()
                data_sums_counts.append((data_sum, data_count))

        elif False: # multithreading using imap; it seems to be 3x faster than threadpool

            # def function_for_imap(filepath):
            #     data_sum, data_count = list(self.yield_sums_counts_filedata(
            #         dataname, back_sep=back_sep, slu_sep=slu_sep,
            #         slice_range=slice_range, rules=rules, filepaths=[filepath,]))[0]
            #     return data_sum, data_count

            from multiprocessing import cpu_count, pool, Pool
            pool_results = []
            pool = Pool(processes=N_max_processes)
            for result in pool.imap(function_for_imap, filepaths):
                pool_results.append(result)
            pool.close()
            pool.join()

        elif True:
            from multiprocessing import cpu_count, pool, Pool
            pool_results = []
            pool = Pool(processes=N_max_processes)

            import inspect
            attributes = inspect.getmembers(self, lambda a:not(inspect.isroutine(a)))
            object_attributes = [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]

            args_iter = zip(uncached_filepaths, repeat(object_attributes), repeat(dataname))
            kwargs_iter = repeat(dict(back_sep=back_sep, slu_sep=slu_sep, slice_range=slice_range, rules=rules))
            pool_results = starmap_with_kwargs(pool, function_for_imap, args_iter, kwargs_iter)

            data_sums_counts = []
            for ProcessedObject in pool_results:
                data_sum, data_count = ProcessedObject
                data_sums_counts.append((data_sum, data_count))

        time_end = time.time()

        time_start = time.time()
        # function_for_process()
        function_for_imap(filepaths[0], object_attributes, dataname)
        time_end = time.time()

        blocks_avg_counts = []
        _count = 0
        for block_files in uncached_filepath_blocks:
            n_files = len(block_files)
            _incomplete = n_files != num_files_per_cache

            separate_sums = np.array([item[0] for item in data_sums_counts[_count:_count+n_files]])
            separate_counts = np.array([item[1] for item in data_sums_counts[_count:_count+n_files]])
            block_sum = np.sum(separate_sums, axis=0)
            block_counts = np.sum(separate_counts, axis=0) 

            data_dim = np.ndim(block_sum)
            weights_dim = np.ndim(block_counts)
            match_dim_weights = np.expand_dims(block_counts, axis=[-(i+1) for i in range(data_dim-weights_dim)])
            match_dim_weights[match_dim_weights==0] = 1

            block_avg = block_sum / match_dim_weights
            blocks_avg_counts.append([block_avg, block_counts])
            rundata = block_avg
            runweights = block_counts

            filepaths = block_files
            # outdir = filepaths[0].split('/rawdata/')[0] + '/work/average_run_data_weights_cache'
            args = (filepaths, dataname, back_sep, slu_sep, slice_range, rules)
            cache_return = cache_function(outdir, filepaths, args, ['rundata','runweights'], use_cache=use_cache)
            if make_cache and (not _incomplete or _save_incomplete_cache):
                print(f'saving cache with files {block_files}')
                np.savez_compressed(cache_return,
                        rundata=rundata,
                        runweights=runweights,)

            _count += n_files

        blocks_avg_counts.extend(blocks_data)
        _temp = blocks_avg_counts[:]

        partial_run_avg = [item[0] for item in blocks_avg_counts]
        partial_run_weights = [item[1] for item in blocks_avg_counts]

        try:
            run_file_weights = np.array(partial_run_weights) 
            run_file_avg = np.array(partial_run_avg)
        except ValueError as e:
            print('blocks_avg_counts: ')
            partial_run_avg = [item[0] for item in _temp]
            partial_run_weights = [item[1] for item in _temp]
            for item in partial_run_avg:
                print(f'    {np.shape(np.array(item))}')
            print('blocks_weights_counts: ')
            for item in partial_run_weights:
                print(f'    {np.shape(np.array(item))}')
            print('blocks_data: ')
            for item in blocks_data:
                print(f'    {np.shape(np.array(item))}')
            
            print()
            print()
            print()
            print()
            print(partial_run_weights)
            print()
            print()
            print()
            print(partial_run_avg)
            print()
            print()
            print()
            print()
            raise e

        data_dim = np.ndim(run_file_avg)
        weights_dim = np.ndim(run_file_weights)
        match_dim_weights = np.expand_dims(run_file_weights, axis=[-(i+1) for i in range(data_dim-weights_dim)])

        try:
            run_file_data = run_file_avg * match_dim_weights
        except Exception as e:
            print('exception at 1433')
            print('run_file_avg: ', np.shape(run_file_avg))
            print('match_dim_weights: ', np.shape(match_dim_weights))

            print('blocks_avg_counts: ')
            partial_run_avg = [item[0] for item in _temp]
            partial_run_weights = [item[1] for item in _temp]
            for item in partial_run_avg:
                print(f'    {np.shape(np.array(item))}')
            print('blocks_weights_counts: ')
            for item in partial_run_weights:
                print(f'    {np.shape(np.array(item))}')
            print('blocks_data: ')
            for item in blocks_data:
                print(f'    {np.shape(np.array(item))}')
            raise e

        compiled_data = []
        compiled_count = []
        run_average = []
        run_weight = []
        for filedata_sum, filedata_count in zip(run_file_data, run_file_weights):
            for i, (split_sum, split_count) in enumerate(zip(filedata_sum, filedata_count)):
                if len(compiled_data)<=i:
                    compiled_data.append([])
                    compiled_count.append([])
                compiled_data[i].append(split_sum)
                compiled_count[i].append(split_count)
        for split_data, split_count in zip(compiled_data, compiled_count):
            data_dim = np.ndim(split_data)
            match_dim_split_count = np.expand_dims(split_count, axis=[-(i+1) for i in range(data_dim-2)])
            divisor = np.sum(match_dim_split_count, axis=0)
            divisor[divisor==0]=1
            run_average.append(np.sum(split_data, axis=0)/divisor)
            run_weight.append(np.sum(split_count, axis=0))

        if make_cache and filepaths and _save_total_cache:
            rundata = np.array(run_average, dtype=float)
            runweights = np.array(run_weight, dtype=int)

            np.savez_compressed(cache_return,
                    rundata=rundata,
                    runweights=runweights,
                    )
        
        return run_average, run_weight

    @_alias
    def average_run_data(self, dataname, back_sep=False, slu_sep=False, slice_range=None,
                         rules=[None,], use_cache=True, make_cache=True, num_files_per_cache=None,
                         ):
        '''
        Same as Run.average_run_data_weights(), but just returning the "data" part of the tuple)

        Output axes: (conditions, rules, data)
        '''

        return self.average_run_data_weights(
                dataname, back_sep=back_sep, slu_sep=slu_sep,
                slice_range=slice_range, rules=rules,
                use_cache=use_cache, make_cache=make_cache,
                num_files_per_cache=num_files_per_cache)[0]