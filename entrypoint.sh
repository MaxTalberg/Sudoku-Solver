#!/bin/bash
# Initialize Conda in bash shell
source /opt/conda/etc/profile.d/conda.sh
# Activate the Conda environment
conda activate RC_Coursework
# Run the Flask application
exec python src/webapp/app.py
