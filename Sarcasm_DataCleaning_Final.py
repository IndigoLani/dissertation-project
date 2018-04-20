import string
import re
import numpy as np

# Define files 
infile = "sarcasm_training_data.txt"
outfile = "sarcasm_training_data_cleaned.txt"

# Array of unwanted words 
remove = ["@", "#", "sarcasm", "sarcastic", "Sarcasm", "Sarcastic", "RT @", "RT"]

# Open files
fin = open(infile)
fout = open(outfile, "w+")

# For each line in the file 
for line in fin:
    for word in remove:
        # Replace unwanted with with 'nothing'
        line = line.replace(word, "")
    # Write line to new file
    fout.write(line)

# Close files to avoid read/write errors 
fin.close()
fout.close()
