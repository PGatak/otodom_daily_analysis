#!/bin/sh

date
echo "RUN"
python --version

python scraper.py
python data_preparation.py
python data_recording.py
python data_visualization.py

date