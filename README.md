# Introduction

During the beamtime, the main task of the on-demand data analysis is to
transform raw velocity-map-imaging (VMI) images into photoelectron spectra
(PES).

## Raw data

We expect to have two main types of raw data: data from the ion time-of-flight
(TOF) spectrometer, and data from the VMI spectrometer. The discussion for both
of these will be the same; the only difference is that TOF spectra do not use
the Abel inverse transform, otherwise the steps are analogous.

The "main" raw data, i.e. TOF and VMI images, fall into 4 categories, determined
by the combination of having either the **FEL** and **SLU** lasers *ON* or *OFF*. The 4
categories are:

    1. FEL/*ON* + SLU/*ON*,
    2. FEL/*ON* + SLU/*OFF*,
    3. FEL/*OFF* + SLU/*ON*,
    4. FEL/*OFF* + SLU/*OFF*;

and raw data must be separated accordingly. We will typicallly refer to a
combination of these 4 as the **"Foreground"** (e.g. FEL/*ON*+SLU/*ON*), and another
combination as the **"Background"** (e.g. FEL/*ON*+SLU/*OFF*).

"Diagnostic" data e.g. FEL intensity (I0-monitor), FEL spectrum, etc.; is also
available in conjunction with the "main" data. These will typically be used to
further filter out the "main" raw data on top of the FEL/SLU/ON/OFF
combinations. For example, we may only consider VMI images with a narrow range
of FEL intensities. This can be done by filtering the VMI data based on
I0-monitor data i.e. through a **filter rule** (our scripts handle this).

## Workflow

Here is the basic workflow of the on-demand data analysis:

1. (optional) Retrieve diagnostic data (e.g. I0M) to determine possible **filter rule**s.
2. With (or without) **filter rule**s, *simultaneously* filter and separate the raw data into "Foreground" and "Background" parts.
3. Average the raw data.
4. (VMI only) Correct image distortions and center the VMI image (more difficult than you think!).
5. (VMI only) Abel-invert the raw images into 1D photoelectron spectra.
6. Transform the TOF/PES spectra from TOF-/radial-coordinates to mq-/KE coordinates.

# Modules used:

numpy-2.1.0
matplotlib-3.9.2
    (Dependencies:
    contourpy-1.2.1
    cycler-0.12.1
    fonttools-4.53.1
    kiwisolver-1.4.5
    pillow-10.4.0
    pyparsing-3.1.2
    )
pbasex-1.3.0
h5py-3.11.0
Cython-3.0.11
quadrant-1.0
dill-0.3.8
scipy-1.14.1