# pythonutils
This repository will contain the python utilities for big data

It will contain the utilities that will be useful to everyone.

The utils are based on python version folder.

RandomLinesFromLargeFile.py 
  When you have a large files, say like 35 Million rows, for data sampling you may want to pick up random sample of N lines.  Using sed or awk or shuf is expensive as they load the file in memory and tries to get the random records.
  
  RandomLinesFromLargeFile helps you choosing the random records and for 38 Million records, it takes approzimately 15 minutes.
  
  Usage: 
  RandomLinesFromLargeFile.py -e <number of lines to extract> -t  <total number of lines in input file -i <input file path> -o <output file path>

RemoveLineFromFile.py 
  is a utility to remove selected lines from a large file.  For large files removing the selected lines is time consuming with the shell script and this tool helps you to accomplish the task with ease.

Usage: 

RemoveLineFromFile.py -e <line number to remove 1-based> -i <input file path> -o <output file path>

Example:
RemoveLineFromFile.py -e 1 -i /tmp/input.csv -o /tmp/output.csv

With multiple lines to remove:
RemoveLineFromFile.py -e 1,2,3 -i /tmp/input.csv -o /tmp/output.csv
