-# Final-Project

# Data collecter
Each data collecter file has code for the entire year. To get the data using this code, you need to be logged-in to Karora.

Run the file using the commands:
bash data_collecter_2015.sh >> output_file_of_2015.txt
bash data_collecter_2020.sh >> output_file_of_2015.txt

These commands will direct the output to two different files. Copy these files to your directory.

# Data processer
This file has Pyhton code.
To run this code, type this exact command for each year:
python3 data_processer.py idioms.txt _file_of_the_year.txt

Python wil automatically open these files and use them to compare, and calculate the amounts.
It is important to know that this process will take at least an hour per file. Do not interrupt this program while it is busy or else the results will not show up.
