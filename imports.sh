#!/bin/bash

# Install required packages
pip install boto3
pip install matplotlib
pip install pandas

# Change directory to cloud_lab4
cd cloud_lab4

# Execute script_plot.py
python3 script_plot.py

# Execute script_upload.py
python3 script_upload.py

# Change back to the previous directory
cd ..
