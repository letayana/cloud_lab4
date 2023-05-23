#!/bin/bash

# Install required packages
pip3 install boto3
pip3 install matplotlib
pip3 install pandas

# Change directory to cloud_lab4
cd cloud_lab4

# Execute script_plot.py
python3 script_plot.py

# Execute script_upload.py
python3 script_upload.py

# Change back to the previous directory
cd ..
