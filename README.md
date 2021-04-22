# serial_data_capture
This package allows you to run this python script to capture serial data and dump it in csv file with date and time stamp for each session.

Need to install minicom
sudo apt-get install minicom

git clone the repository

cd serial_data_capture

python3 serial_data_capture.py

check the serial data dump in csvData folder

be sure to corrrect the serial port of your sensor in the serial_data_capture python script. i have used ttyUSB0.
