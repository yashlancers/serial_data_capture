# serial_data_capture
This package allows you to run this python script to capture serial data and dump it in csv file with date and time stamp for each session.

Need to install minicom
sudo apt-get install minicom

git clone the repository

cd serial_data_capture

python3 serial_data_capture.py

Check the serial data dump in csvData folder. The file will be .csv with date and time as file name autocreated. Be sure to corrrect the serial port where your sensor is attached with Raspberry Pi 4 or anyother Linux board in the serial_data_capture.py python script. i have used ttyUSB0.
