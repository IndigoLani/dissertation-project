import string
import re
import numpy as np

#Files to open
infile = "sarcasm_training_data.txt"
outfile = "sarcasm_training_data_cleaned.txt"

#Array of characters and words for removal
remove = ["@", "#", "sarcasm", "sarcastic", "Sarcasm", "Sarcastic", "RT @", "RT"]

fin = open(infile)
fout = open(outfile, "w+")

for line in fin:
    #Remove links (causes issue with attributes)
    re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)

    #Replace each unwanted word with 'nothing'
    for word in remove:
        line = line.replace(word, "")
    fout.write(line)

fin.close()
fout.close()
