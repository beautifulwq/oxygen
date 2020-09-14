# oximetry-phone-cam-data
This repository contains the open source data source repository to share smartphone camera oximetry data from Viswanath et al 2020 [include link].

## Getting Started
Clone the repo and run ??.ipynb to get started!

More example code can be found in the examples directory.

### Needed packages: 
* fill out on a fresh run

## Data Format
There were 6 patients in this study (numbered 10001-10006).

The smartphone oximetry data was collected in the form of MP4 videos, downloadable from: http://bit.ly/oxy-raw-z.  Each frame's R, G, and B values were averaged to create the csv files in data/ppg-csv.

The ground truth data was collected from a few standard pulse oximeters attached to the subjects' other fingers.  That data can be found in data/gt.

### Data Format Notes
* Camera framerate = 30 Hz
* Ground truth pulse oximeters framerate = 1 Hz
* Recording was started and stopped on the camera and the pulse oximeters at the same time

## Background
SpO
We performed a clinical development validation induced hypoxemia study, in which test subjects were given a controlled mixture of oxygen and nitrogen to lower their SpO2 level over a period of 12-16 minutes.  The patients had one finger from each hand on a phones camera, while the camera flash transmitted light through their fingertips for reflectance photoplethysmography.  The camera recorded 

For more details, see the publication in IMWUT from 2020: [include link].

### Ideas
Go ahead and try different models:
* Analytical (eg. ratio-of-ratios)
* Deep Learning
* Linear 
* Or, think of your own!

## Citation
If you use this data or code in your project, please cite it.  Here's the ACM format:
* Add citation later when it's ready.

### License
This data is provided open-source via the MIT license.  For more details, see the license file.  We want you to use it for whatever creative projects you can come up with!  

