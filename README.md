# Quick start guide

### How to set up in JupyterLab

In the terminal, create a virtual environment with the command
> python -m venv venv

To make your JupyterNotebooks see the virtual environment, run the following commands on the terminal
> pip install ipykernel
> python -m ipykernel install --user --name=venv 


### How to set up Python and modules through Terminal

Python3 is required, as well as Python's pip for install modules. To install python, you can use the installer provided at "https://www.python.org/downloads/". Make sure Python is properly installed, by running the following command on the terminal of your choosing (e.g. cmd or PowerShell for Windows):

> python

If python is not found, make sure you add the location of the "python.exe" file into the __PATH__ of your system (search online for "How to add a folder to PATH"; for Windows it's called "ENVIRONMENT VARIABLES").

Once Python is properly installed, use your terminal to go into our data analysis folder which you downloaded (e.g. the "cd" change directory command for CMD). You should see 4 items there:

- examples/
- Lib/
- requirements.txt
- README.md (you're here!)

Now install the necessary modules through pip, which includes our custom libraries:
> pip install -r requirements.txt

### Opening a Jupyter Notebook

Open any Notebook file. To run the notebook in the virtual environment, you must swap the kernel (upper-right hand corner) from "Python 3 (ipykernel)" -> "venv".

### Run a preliminary script

Run either "save_gdata.py" or "save_gdata.ipynb". For the .py file, you can run it through the terminal as:

> python save_gdata.py

\*This may take a few minutes\*. This script generates the CPBASEX data, and the output will be saved as e.g. "G_r256_k64_l4_half.h5". **If you do not run this, the abel inversion scripts will not work**

### What to look at

In order of complexity:

1. basic_tutorial.ipynb
2. tof_to_mq_calibration.ipynb
3. basic_filtering.ipynb
4. basic_abel_inversion.ipynb
5. basic_delay_analysis.ipynb


# Introduction

During the beamtime, the main task of the on-demand data analysis is to
transform raw velocity-map-imaging (VMI) images into photoelectron spectra
(PES). So why are these libraries so large and complicated? Answer: FERMI generates a large amount of raw data, and reading/compiling this raw data is 1. slow (i.e. I/O-rate limited) 2. leads to a lot of code bloat. The purpose of these libraries is to make the following easier and hopefully more intuitive:

- compilation of raw data from h5 files
- filtering of raw data based on adjustable rules
- separation of "foreground" and "background" data
- calibration of ion TOF -> ion m/q

To understand the scripts, I recommend looking at the scripts in increasing order of complexity:

1. basic_tutorial.ipynb
2. tof_to_mq_calibration.ipynb
3. basic_filtering.ipynb
4. basic_abel_inversion.ipynb
5. basic_delay_analysis.ipynb

If the .ipynb are too annoying to use, you can also look at the .py versions of these scripts in the IDE of your choice (I recommend either Spyder for a simple standalone installation, or VScode for more feature-richness). These .py files were used to generate the .ipynb files through ipynb-py-convert library. **HOWEVER**, conventional online data analysis is done using Jupyter Labs hosted on the FERMI server, where we do use only .ipynb files. So I recommend you to at least get used to this format.


# Raw data

We expect to have two main types of raw data: data from the ion time-of-flight (TOF) spectrometer, and data from the VMI spectrometer. The discussion for both of these will be the same; the only difference is that TOF spectra do not use the Abel inverse transform, otherwise the steps are analogous.

### "Main" data

"Main" raw data, i.e. TOF and VMI images, fall into 4 categories. These are determined by the combination of having either the **FEL** and **SLU** lasers *ON* or *OFF*:

1. FEL/*ON* + SLU/*ON*,
2. FEL/*ON* + SLU/*OFF*,
3. FEL/*OFF* + SLU/*ON*,
4. FEL/*OFF* + SLU/*OFF*;

and raw data must be separated accordingly. We will typicallly refer to a combination of these 4 as the **"Foreground"** (e.g. FEL/*ON*+SLU/*ON*), and another combination as the **"Background"** (e.g. FEL/*ON*+SLU/*OFF*).

### "Diagnostic" data

"Diagnostic" data e.g. FEL intensity (I0-monitor), FEL spectrum, etc.; is also available in conjunction with the "main" data. These will typically be used to further filter out the "main" raw data on top of the FEL/SLU/ON/OFF combinations. For example, we may only consider VMI images with a narrow range of FEL intensities. This can be done by filtering the VMI data based on I0-monitor data i.e. through a **filter rule** (our scripts handle this).

# Workflow

Here is the basic workflow of the on-demand data analysis:

1. (optional) Retrieve diagnostic data (e.g. I0M) to determine possible **filter rule**s.
2. With (or without) **filter rule**s, *simultaneously* (i) filter the raw data (ii) separate the filtered data into "Foreground" and "Background" parts (iii) average over the data.
3. (VMI only) Correct image distortions and center the VMI image (more difficult than you think!).
4. (VMI only) Abel-invert the raw images into 1D photoelectron spectra.
5. Transform the TOF/PES spectra from TOF-/radial-coordinates to mq-/KE coordinates.

# Modules used:

numpy==2.1.0\
matplotlib==3.9.2\
pbasex==1.3.0\
h5py==3.11.0\
Cython==3.0.11\
quadrant==1.0\
dill==0.3.8\
scipy==1.14.1\
lmfit==1.3.2\
ipynb-py-convert==0.4.6

To download the modules, simply run the "requirements.txt" through pip:

> pip3 install -r requirements.txt

# FERMI GUI instructions
## How to build

The ui_form.py is generated through QT Creator; its project folder is currently located at "C:\Users\ngaia\Downloads\testing_qtcreator". This QT Creator project folder is ~0.5GB, so it will be left there.

With QT Creator, run "build" and "deploy", and that will generate the "ui_form.py". Copy and paste this to replace the beginning of the "main.py" file. The "main.py" file is made up of the "ui_form.py", and "mainwindow_for_ui_form.py" put together.

After generating "ui_form.py", copy the code from "mainwindow_for_ui_form.py" into  "ui_form.py", and then it will run.