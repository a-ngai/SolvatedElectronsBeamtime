'''
Extremely poorly documented library that I made. Sorry! If the Search returns
an Error, check your search_string, and make sure it follows the basic rules:
    - No spaces within the "keyword" or "options"
    - No illegal characters in the "keyword" or "options" (every symbol in the
      operator_dict or function_dict or parentheses)
If it still gives errors, then bracket everything in case the search_string
is somehow bracketed wrong within the functions.
i.e. change
    'keyword1 : option1 | keyword2 : option2'
    -> '(keyword1:option1)|(keyword2:option2)'
to be on the safe side.
'''



import re
from itertools import chain
import numpy as np

def infix_to_postfix_functions(infix_list,
                            operator_dict=None,
                            function_dict=None,
                            ):
    """ Converts infix to postfix notation, only treats operators and
    functions.
    """

    # defaults for the operators, functions, and contexts
    if operator_dict is None:
        operator_dict = {
            '&' : OperatorInfo(num_args=2,
                               precedence=2,
                               rule=(lambda bool1, bool2: bool1 and bool2)),
            '|' : OperatorInfo(num_args=2,
                               precedence=1,
                               rule=(lambda bool1, bool2: bool1 or bool2)),
            '^' : OperatorInfo(num_args=2,
                               precedence=1,
                               rule=(lambda bool1, bool2:
                                     (bool1 and not bool2) or (not bool1 and bool2))),
            }
    if function_dict is None:
        function_dict = {
            '~' : OperatorInfo(num_args=1,
                               precedence=1,
                               rule=(lambda bool1: not bool1)),
            }

    operators = list(operator_dict.keys())
    functions = list(function_dict.keys())
    precedence = {}
    for key in operator_dict.keys():
        precedence[key]=operator_dict[key].precedence
    for key in function_dict.keys():
        precedence[key]=function_dict[key].precedence


    temp_list = []
    temp_list.extend(infix_list)

    queue = []
    stack = []
    while len(temp_list)>0:

        token = temp_list[0]

        if not isinstance(token, int) and token not in operators+functions+['(',')']:
            raise Exception(f'Token ({token}) is not a valid character')

        if isinstance(token, int):
            queue.append(temp_list.pop(0))
        elif token in functions:
            stack.append(temp_list.pop(0))
        elif token in operators:
            while (
                    (len(stack)>0)
                    and (stack[-1] not in ['(',')'])
                    and (
                            (stack[-1] in functions)
                            or (precedence[token] <= precedence[stack[-1]]) )
                    and (stack[-1] != '(' ) ):
                queue.append(stack.pop())
            stack.append(temp_list.pop(0))
        elif token == '(':
            stack.append(temp_list.pop(0))
        elif token == ')':
            while stack[-1] != '(':
                queue.append(stack.pop())
            if stack[-1]=='(':
                stack.pop()
            temp_list.pop(0)

    while len(stack)>0:
        queue.append(stack.pop())

    return queue




def evaluate_search_term_instance(post_fix_expression,
                               Elements,
                               input_object,
                               operator_dict=None,
                               function_dict=None,
                               context_dict=None,
                               word_dict=None,
                               _debug_output=False):

    if word_dict is None:
        word_dict=['no_word_dict',]*len(Elements)
    if operator_dict is None:
        raise Exception('No operator_dict given!')
    if function_dict is None:
        raise Exception('No function_dict given!')
    if context_dict is None:
        raise Exception('No context_dict given!')

    elements = []
    elements.extend(Elements)
    postfix = []
    postfix.extend(post_fix_expression)

    operator_symbols = list(operator_dict.keys())
    function_symbols = list(function_dict.keys())

    combined_dict = {**operator_dict, **function_dict}


    # for cases where the postfix is >= 3 items

    if _debug_output:
        print()
        print('debug(function) Beginning of debugging print statements as debug(evaluate_search_term_instance)')


    bool_result = None
    while len(postfix)>=2:
        i = 0
        while postfix[i] not in operator_symbols+function_symbols: i+=1
        operator = postfix[i]
        num_args = combined_dict[operator].num_args
        old_arguments = [elements[postfix[i+k]] for k in range(-num_args,0)]
        arguments = [
                context_dict[item.context](item.keyword, item.option, input_object)
                if (not isinstance(item, bool) and not isinstance(item, np.bool_) and not isinstance(item, np.ndarray))
                else item for item in old_arguments
                ]  # if the items are not booleans or numpy arrays, then I assume they are
                   # functions, and we evaluate them. These elements always have 3 arguments

        if _debug_output: # checking the individual operations
            print('\tdebug(evaluate_search_term_instance) bool evaluation step as debug(step):')
            for j in range(-len(arguments),0):
                print('\t\t debug(step) element {}: '.format(postfix[i+j]), word_dict[postfix[i+j]], arguments[j])
            print('\t\t debug(step) operator : ', operator )

        bool_result = combined_dict[operator].rule(*arguments)
        del postfix[i-num_args:i+1]
        postfix.insert(i-num_args, len(elements))

        if _debug_output:
            print('\t\t debug(step) result   : ', bool_result)

        elements.append(bool_result)
        word_dict.append(bool_result)

    # for cases with only one postfix item
    if bool_result is None:
        one_element = elements[0]
        if not isinstance(one_element, bool):
            #test_one = one_element(input_object)
            test_one = context_dict[one_element.context](one_element.keyword, one_element.option,
                                                         input_object)
        else: test_one = one_element

        bool_result = test_one

    if _debug_output:
        print('debug(evaluate_search_term_instance) final bool result:\n\t', bool_result)

    return bool_result



def standardize_string(string,
                      operator_list=['&','|','^','%'],
                      function_list=['~'],
                      context_list=[':',';']):


    filler_symbol = '%'

    if not isinstance(operator_list, list) and isinstance(operator_list, dict):
        operator_names = list(operator_list.keys())
        operator_precedence = [operator_list[key].precedence for key in operator_list.keys()]
        operator_precedence, operator_names = list(
                zip(*sorted(zip(operator_precedence, operator_names))))
        filler_symbol = operator_names[0]

        operator_list = list(operator_list.keys())
    elif not isinstance(operator_list, list) and not isinstance(operator_list, dict):
        raise Exception(f'operator_symbols argument (type={type(operator_list)}) is neither list nor dict')
    if not isinstance(function_list, list) and isinstance(function_list, dict):
        function_list = list(function_list.keys())
    elif not isinstance(function_list, list) and not isinstance(function_list, dict):
        raise Exception(f'function_smbols argument (type={type(function_list)}) is neither list nor dict')
    if not isinstance(context_list, list) and isinstance(context_list, dict):
        context_list = list(context_list.keys())
    elif not isinstance(context_list, list) and not isinstance(context_list, dict):
        raise Exception(f'function_smbols argument (type={type(context_list)}) is neither list nor dict')

    temp_string = ' '+string+' '

    operator_symbols_for_re = '\\'+'\\'.join(operator_list)
    function_symbols_for_re = '\\'+'\\'.join(function_list)
    context_symbols_for_re = '\\'+'\\'.join(context_list)

    re_context = re.compile(f'([{context_symbols_for_re}])')

    context_starts = [i.start(1) for i in re_context.finditer(temp_string)]

    re_keyword_start = re.compile(
            r'[ {}\(\)]'.format(operator_symbols_for_re+function_symbols_for_re)  # no space, functions, operators, nor brackets
            + r'([^ {}\(\)]+)[{}]'.format(operator_symbols_for_re+function_symbols_for_re, context_symbols_for_re)
            )
    #keyword_names = [i.group(1) for i in re_keyword_start.finditer(temp_string)]
    keyword_starts = [i.start(1) for i in re_keyword_start.finditer(temp_string)]

    # put brackets around options so that keyword:options -> keyword:(options)
    for i in list(range(len(keyword_starts)))[::-1]:
        keyword_start = keyword_starts[i]
        context_start = context_starts[i]
        parenthesis_count_list = [0,]
        option_start = context_start+1
        j = option_start
        if keyword_start == keyword_starts[-1]:
            next_keyword_start = len(temp_string)-1
        else:
            next_keyword_start = keyword_starts[i+1]
        option_end = None

        # forwards
        while j<next_keyword_start-1:
            current_char = temp_string[j]
            if current_char == '(':  parenthesis_count_list.append(parenthesis_count_list[-1]+1)
            elif current_char == ')': parenthesis_count_list.append(parenthesis_count_list[-1]-1)
            else: parenthesis_count_list.append(parenthesis_count_list[-1])
            j+=1

        if -1 in parenthesis_count_list:
            negative_locations = [index for index, num in enumerate(parenthesis_count_list)
                                  if num == -1]
            option_end = context_start + negative_locations[0] - 1

        elif parenthesis_count_list[-1]>0:
            zero_locations = [index for index, num in enumerate(parenthesis_count_list) if num == 0]
            j = context_start + zero_locations[-1]


        # backwards
        if option_end is None:
            while j > context_start:
                current_char = temp_string[j]
                if current_char not in [' ','(',')']+operator_list+function_list:
                    break
                j+=-1
            option_end = j

        temp_string = (
                temp_string[:context_start+1]+'('
                +temp_string[context_start+1:option_end+1]+')'
                +temp_string[option_end+1:]
                )

#    print('putting brackets around options: ', temp_string)
    # now put brackets around keyword and options as keyword:(options) -> (keyword:(options))
    #keyword_names = [i.group(1) for i in re_keyword_start.finditer(temp_string)]
    keyword_starts = [i.start(1) for i in re_keyword_start.finditer(temp_string)]
    for i in list(range(len(keyword_starts)))[::-1]:
        keyword_start = keyword_starts[i]

        seen_bracket = False
        parenthesis_count = 0
        j = keyword_start
        while not (seen_bracket and parenthesis_count==0):
            j += 1
            current_char = temp_string[j]
            if current_char == '(':
                parenthesis_count += 1
                seen_bracket = True
            elif current_char == ')':
                parenthesis_count += -1
        option_end = j

        temp_string = (
                temp_string[:keyword_start]+'('
                +temp_string[keyword_start:option_end+1]+')'
                +temp_string[option_end+1:]
                )
#    print('putting brackets around keyword and options: ', temp_string)

    temp_string = temp_string.replace(' ','')
    temp_string = temp_string.replace(')(', f'){filler_symbol}(')

#    print('replacing spaces and inserting operators: ', temp_string)

    re_missing_function = re.compile(r'([^{}\(])[{}]'.format(operator_symbols_for_re, function_symbols_for_re))
    missing_function_locations = [item.end(1) for item in re_missing_function.finditer(temp_string)]

    for loc in missing_function_locations[::-1]:
        temp_string = temp_string[:loc] + filler_symbol + temp_string[loc:]


#    raise Exception

    return temp_string





def separate_keyword_options(string,
                          operator_symbols=['&','|','^'],
                          function_symbols=['~'],
                          context_symbols=[':',';',],
                          _debug_output=False):
    """ Converts the rule string into a key part, and a list of all the
    other elements/operators """

    if not isinstance(operator_symbols, list) and isinstance(operator_symbols, dict):
        operator_symbols

    re_operator_symbols = '\\'+'\\'.join(operator_symbols)
    re_function_symbols = '\\'+'\\'.join(function_symbols)
    re_context_symbols = '\\'+'\\'.join(context_symbols)


    keywords = re.compile(r'(\S*)[{}]'.format(re_context_symbols))

    keys = re.findall(keywords, string)
    key = keys[0]

    shortening = string

    only_string = re.search('('+key+f')([{re_context_symbols}])(.*)$', shortening)
    context = only_string[2]
    options = only_string[3]
    #keyword_and_options = only_string[1] + only_string[2] + only_string[3]

    between_parts = options.replace(' ','')

    separate_options = re.compile(
        r'([ \(\){}]*)'.format(re_operator_symbols+re_function_symbols)
        + r'([^ \(\){}]*)'.format(re_operator_symbols+re_function_symbols)
        + r'([ \(\){}]*)'.format(re_operator_symbols+re_function_symbols)
        )

    option = between_parts

    temp_constituents = re.findall(separate_options, option)
    for i in list(range(len(temp_constituents)))[::-1]:
        if temp_constituents[i][1]=='':
            temp_constituents.pop(i)

    elements = [part[1] for part in temp_constituents]

    int_constituents = [list(row) for row in temp_constituents]

    for i in range(len(int_constituents)):
        int_constituents[i][1]=i

    infix_syntax = ''
    for i in range(len(int_constituents)):
        infix_syntax += int_constituents[i][0]+str(int_constituents[i][1])+int_constituents[i][2]

    infix_list = []
    for i in range(len(int_constituents)):
        infix_list.extend(
            list(int_constituents[i][0])
            +[int_constituents[i][1],]
            +list(int_constituents[i][2])
            )

    if elements == []:
        elements = ['',]
        infix_list = [0,]

    return key, elements, context, infix_list


def keywords_postfix_simplification(string,
                           operator_dict=None,
                           function_dict=None,
                           context_dict=None,
                           _debug_output=False):


    # defaults for the operators, functions, and contexts
    if operator_dict is None:
        operator_dict = {
            '&' : OperatorInfo(num_args=2,
                               precedence=2,
                               rule=(lambda bool1, bool2: bool1 and bool2)),
            '|' : OperatorInfo(num_args=2,
                               precedence=1,
                               rule=(lambda bool1, bool2: bool1 or bool2)),
            '^' : OperatorInfo(num_args=2,
                               precedence=1,
                               rule=(lambda bool1, bool2: (bool1 and not bool2) or (not bool1 and bool2))),
            '%' : OperatorInfo(num_args=2,
                               precedence=0,
                               rule=(lambda bool1, bool2: bool1 and bool2)),
            }
    if function_dict is None:
        function_dict = {
            '~' : OperatorInfo(num_args=1,
                               precedence=1,
                               rule=(lambda bool1: not bool1)),
            }
    if context_dict is None:
        context_dict = {
            ':' : lambda keyword, option, SearchObject: str(SearchObject.attributes[keyword]) == str(option),
            ';' : lambda keyword, option, SearchObject: str(SearchObject.attributes[keyword]) == str(option),
            }


    operator_list = list(operator_dict.keys())
    function_list = list(function_dict.keys())
    context_list = list(context_dict.keys())

    operator_symbols_for_re = '\\'+'\\'.join(operator_list)
    function_symbols_for_re = '\\'+'\\'.join(function_list)
    context_symbols_for_re = '\\'+'\\'.join(context_list)

    re_keyword_start = re.compile(
        r'\(([^ {}\(\)]+)[{}]'.format(operator_symbols_for_re+function_symbols_for_re, context_symbols_for_re)
            )
    keyword_starts = [i.start(1) for i in re_keyword_start.finditer(string)]

    infix_list = [char for char in string[:keyword_starts[0]]]
    infix_keywordislands = []

    for i in range(len(keyword_starts)):
        if i == len(keyword_starts)-1:
            next_start = len(string)
        else:
            next_start = keyword_starts[i+1]

        parenthesis_count = 0
        start = keyword_starts[i]
        j = start
        while j < next_start and parenthesis_count>=0:
            j += 1
            current_char = string[j]
            if current_char == '(':
                parenthesis_count += 1
                #seen_bracket = True
            elif current_char == ')':
                parenthesis_count += -1
        end = j-1

        infix_list.extend([i,]+[char for char in string[end+1:next_start]])
        infix_keywordislands.append(string[start:end+1])

    infix_condensed = []
    infix_condensed.extend(infix_list)

    infix_overall = []
    infix_overall.extend(infix_list)

    seen_keyword_list = []
    seen_element_list = []
    seen_function_list = []
    seen_context_list = []
    seen_infix_lists = []
    for keywordisland in infix_keywordislands:
        separated = separate_keyword_options(keywordisland,
                              operator_symbols=operator_list,
                              function_symbols=function_list,
                              context_symbols=context_list,
                              _debug_output=_debug_output)
        keyword, elements, context, infix = separated
        seen_keyword_list.append(keyword)
        seen_element_list.append(elements)
        seen_context_list.append(context)
        seen_infix_lists.append(infix)

        functions = []
        for element in elements:

            class FunctionalContextElement:
                def __init__(self, keyword, context, option):
                    self.keyword = keyword
                    self.context = context
                    self.option = option

            context_element_instance = FunctionalContextElement(
                    keyword=keyword,
                    context=context,
                    option=element,
                    )

            functions.append(context_element_instance)

        seen_function_list.append(functions)

    current_int = 0
    for i in range(len(seen_keyword_list)):
        seen_infix_lists[i] = [j+current_int if isinstance(j, int) else j for j in seen_infix_lists[i]]
        current_int = max([j if isinstance(j, int) else 0 for j in seen_infix_lists[i]])+1


    functions_overall = list(chain.from_iterable(seen_function_list))

    sub_locations = [infix_condensed.index(i) for i in range(len(seen_keyword_list))]
    for i in list(range(len(seen_keyword_list)))[::-1]:
        sub_loc = sub_locations[i]
        infix_overall[sub_loc:sub_loc]=seen_infix_lists[infix_overall.pop(sub_loc)]

    postfix_overall = infix_to_postfix_functions(infix_overall,
                                              operator_dict=operator_dict,
                                              function_dict=function_dict)

#    if _debug_output:
#        print('debug(generalKeywordsPostfixConverter) overall_infix:\n\t', overall_infix)
#        print('debug(generalKeywordsPostfixConverter) overall_postfix:\n\t', overall_postfix)
#        print('debug(generalKeywordsPostfixConverter) overall_postfix word_terms:\n\t', word_terms)

    return postfix_overall, functions_overall, infix_keywordislands



def evaluate_search_term(rule, input_dict,
                       operator_dict=None,
                       function_dict=None,
                       context_dict=None,
                       _debug_output=False):

    """ The all-in-one function.

    Performance note: If the search string is the same, it's much
    faster to use the generalKeywordsPostfixConverter() once to generate the
    postfix expression and element functions, then use the
    evaluate_search_term_instance() function to evaluate the SearchObject.
    """

    class OperatorInfo:
        def __init__(self, num_args=0, precedence=0, rule=None):
            self.num_args = num_args
            self.precedence = precedence
            self.rule = rule

    # defaults for the operators, functions, and contexts
    if operator_dict is None:
        operator_dict = {
            '&' : OperatorInfo(num_args=2,
                               precedence=2,
                               rule=(lambda bool1, bool2: bool1 and bool2)),
            '|' : OperatorInfo(num_args=2,
                               precedence=1,
                               rule=(lambda bool1, bool2: bool1 or bool2)),
            '^' : OperatorInfo(num_args=2,
                               precedence=1,
                               rule=(lambda bool1, bool2:
                                     (bool1 and not bool2) or (not bool1 and bool2))),
            '%' : OperatorInfo(num_args=2,
                               precedence=0,
                               rule=(lambda bool1, bool2: bool1 and bool2)),
            }
    if function_dict is None:
        function_dict = {
            '~' : OperatorInfo(num_args=1,
                               precedence=1,
                               rule=(lambda bool1: not bool1)),
            }
    if context_dict is None:
        context_dict = {
            ':' : lambda keyword, option, input_dict: str(input_dict[keyword]) == str(option),
            ';' : lambda keyword, option, input_dict: str(input_dict[keyword]) == str(option),
            '>' : lambda keyword, option, input_dict: float(input_dict[keyword]) > float(option),
            '<' : lambda keyword, option, input_dict: float(input_dict[keyword]) < float(option),
            '=' : lambda keyword, option, input_dict: float(input_dict[keyword]) == float(option),
            '†' : lambda keyword, option, input_dict: True
            }

    standardized_rule = standardize_string(rule,
                                      operator_list=operator_dict,
                                      function_list=function_dict,
                                      context_list=context_dict)
    search_objects = keywords_postfix_simplification(standardized_rule,
                                      operator_dict=operator_dict,
                                      function_dict=function_dict,
                                      context_dict=context_dict)
    sample_postfix, sample_function_elements, word_terms  = search_objects

    is_list = isinstance(input_dict, list)

    input_list = []
    if not is_list:
        input_list.append(input_dict)
    else:
        input_list = input_dict

    bool_list = []
    for object_instance in input_list:

        bool_result = evaluate_search_term_instance(
            sample_postfix, sample_function_elements,
            object_instance,
            word_dict=word_terms,
            operator_dict=operator_dict,
            function_dict=function_dict,
            context_dict=context_dict,
            _debug_output=_debug_output)

        bool_list.append(bool_result)

    if _debug_output:
        print()

    if not is_list:
        return bool_result

    return bool_list


class SearchClass:
    def __init__(self,
                 search_string=None,
                 operator_dict=None,
                 function_dict=None,
                 context_dict=None,
                 _autoprepare=True,
                 _debug_output=False):

        # defaults for the operators, functions, and contexts
        if operator_dict is None:
            operator_dict = {
                '&' : OperatorInfo(num_args=2,
                                   precedence=2,
                                   rule=(lambda bool1, bool2: bool1 and bool2)),
                '|' : OperatorInfo(num_args=2,
                                   precedence=1,
                                   rule=(lambda bool1, bool2: bool1 or bool2)),
                '^' : OperatorInfo(num_args=2,
                                   precedence=1,
                                   rule=(lambda bool1, bool2: (bool1 and not bool2) or (not bool1 and bool2))),
                }
        if function_dict is None:
            function_dict = {
                '~' : OperatorInfo(num_args=1,
                                   precedence=1,
                                   rule=(lambda bool1: not bool1)),
                }
        if context_dict is None:
            context_dict = {
                ':' : lambda keyword, option, input_dict: str(input_dict[keyword]) == str(option),
                ';' : lambda keyword, option, input_dict: str(input_dict[keyword]) == str(option),
                '>' : lambda keyword, option, input_dict: float(input_dict[keyword]) > float(option),
                '<' : lambda keyword, option, input_dict: float(input_dict[keyword]) < float(option),
                '=' : lambda keyword, option, input_dict: float(input_dict[keyword]) == float(option),
                '†' : lambda keyword, option, input_dict: True
                }

        if search_string is None or search_string=='':
            search_string = 'a†a'
        self.search_string=search_string
        self.standardized_rule=None
        self.operator_dict=operator_dict
        self.function_dict=function_dict
        self.context_dict=context_dict
        self.search_ready=False
        self._debug_output=_debug_output

        if _autoprepare: self.prepare_search_function()

    def prepare_search_function(self):
        """ Use if the operator_dict, function_dict, context_dict were changed
        """

        standardized_rule = standardize_string(self.search_string,
                                          operator_list=self.operator_dict,
                                          function_list=self.function_dict,
                                          context_list=self.context_dict)
        self.standardized_rule=standardized_rule

        postfix_string, FunctionElements, word_terms = keywords_postfix_simplification(
                self.standardized_rule,
                operator_dict=self.operator_dict,
                function_dict=self.function_dict,
                context_dict=self.context_dict,
                _debug_output=self._debug_output)

        self.postfix_string = postfix_string
        self.postfix_elements = FunctionElements
        self.postfix_elements_words = word_terms

        self.search_ready=True


    def evaluate(self, input_object):
        if not self.search_ready: raise Exception(
                'evaluation functionality not prepared, use',
                'prepare_search_function() first.')
        is_list = isinstance(input_object, list)

        input_list = []
        if not is_list:
            input_list.append(input_object)
        else:
            input_list = input_object

        bool_list = []
        for object_instance in input_list:

            bool_result = evaluate_search_term_instance(
                    self.postfix_string,
                    self.postfix_elements,
                    object_instance,
                    operator_dict=self.operator_dict,
                    function_dict=self.function_dict,
                    context_dict=self.context_dict,
                    word_dict=self.postfix_elements_words,
                    _debug_output=self._debug_output
                    )
            bool_list.append(bool_result)

        # raise Exception


        if not is_list:
            return bool_result


        return bool_list


class OperatorInfo:
    """ Class used to define the operations for the search functions.
    e.g.
        operator_dict = {
            '&' : OperatorInfo(num_args=2,
                               precedence=2,
                               rule=(lambda bool1, bool2: bool1 and bool2)),
            '|' : OperatorInfo(num_args=2,
                               precedence=1,
                               rule=(lambda bool1, bool2: bool1 or bool2)),
            '^' : OperatorInfo(num_args=2,
                               precedence=1,
                               rule=(lambda bool1, bool2: (bool1 and not bool2) or (not bool1 and bool2))),
            }
    gives the appropriate dictionary for the action of the &, |, ^ operators.
    """

    def __init__(self, num_args=0, precedence=0, rule=None):
        self.num_args = num_args
        self.precedence = precedence
        self.rule = rule

# array_operator_dict = {
#     '&' : OperatorInfo(num_args=2,
#                        precedence=2,
#                        rule=(lambda bool1, bool2: bool1 * bool2)),
#     '|' : OperatorInfo(num_args=2,
#                        precedence=1,
#                        rule=(lambda bool1, bool2: bool1 + bool2)),
#     '^' : OperatorInfo(num_args=2,
#                        precedence=1,
#                        rule=(lambda bool1, bool2: (bool1 * ~bool2) + (~bool1 * bool2))),
#     '%' : OperatorInfo(num_args=2,
#                        precedence=0,
#                        rule=(lambda bool1, bool2: bool1 * bool2)),
#     }
# array_function_dict = {
#     '~' : OperatorInfo(num_args=1,
#                        precedence=1,
#                        rule=(lambda bool1: ~bool1)),
#     }
# array_context_dict = {
#     ':' : lambda keyword, option, input_func: np.array(input_func(keyword),dtype=str) == str(option),
#     '>' : lambda keyword, option, input_func: np.array(input_func(keyword),dtype=float) > float(option),
#     '<' : lambda keyword, option, input_func: np.array(input_func(keyword),dtype=float) < float(option),
#     '=' : lambda keyword, option, input_func: np.array(input_func(keyword),dtype=float) == float(option),
#     '†' : lambda keyword, option, input_func: np.array([True,]),#slice(0,None,1)
#     ';' : lambda keyword, option, input_func: ExtendedFunctions[keyword](input_func, option),
#     }

def operator_and(bool1, bool2):
    return bool1 * bool2
def operator_or(bool1, bool2):
    return bool1 + bool2
def operator_xor(bool1, bool2):
    return (bool1 * ~bool2) + (~bool1 * bool2)
def operator_not(bool1):
    return ~bool1
def keyword_string_equal(keyword, option, input_func):
    return np.asarray(input_func(keyword),dtype=str) == str(option)
def keyword_float_greater(keyword, option, input_func):
    return np.asarray(input_func(keyword),dtype=float) > float(option)
def keyword_float_lesser(keyword, option, input_func):
    return np.asarray(input_func(keyword),dtype=float) < float(option)
def keyword_float_equal(keyword, option, input_func):
    return np.asarray(input_func(keyword),dtype=float) == float(option)
def keyword_any(keyword, option, input_func):
    return np.asarray([True,])#slice(0,None,1)

array_operator_dict = {
    '&' : OperatorInfo(num_args=2,
                    precedence=2,
                    rule=operator_and),
    '|' : OperatorInfo(num_args=2,
                    precedence=1,
                    rule=operator_or),
    '^' : OperatorInfo(num_args=2,
                    precedence=1,
                    rule=operator_xor),
    '%' : OperatorInfo(num_args=2,
                    precedence=0,
                    rule=operator_and),
    }
array_function_dict = {
    '~' : OperatorInfo(num_args=1,
                    precedence=1,
                    rule=operator_not),
    }
array_context_dict = {
    ':' : keyword_string_equal,
    '>' : keyword_float_greater,
    '<' : keyword_float_lesser,
    '=' : keyword_float_equal,
    '†' : keyword_any,
    # ';' : lambda keyword, option, input_func: ExtendedFunctions[keyword](input_func, option),
    }

search_symbols = {
    'operator_dict' : array_operator_dict,
    'function_dict' : array_function_dict,
    'context_dict' : array_context_dict}

def wavelength_sigma_geq(input_func, option):
    bool_array = np.asarray(input_func('wavelength')[:,1], dtype=float) >= float(option)
    return bool_array
def wavelength_sigma_leq(input_func, option):
    bool_array = np.asarray(input_func('wavelength')[:,1], dtype=float) <= float(option)
    return bool_array
def wavelength_mu_geq(input_func, option):
    bool_array = np.asarray(input_func('wavelength')[:,0], dtype=float) >= float(option)
    return bool_array
def wavelength_mu_leq(input_func, option):
    bool_array = np.asarray(input_func('wavelength')[:,0], dtype=float) <= float(option)
    return bool_array

ExtendedFunctions = {
    'wavelength_mu_geq' : wavelength_mu_geq,
    'wavelength_mu_leq' : wavelength_mu_leq,
    'wavelength_sigma_geq' : wavelength_sigma_geq,
    'wavelength_sigma_leq' : wavelength_sigma_leq,
    }

