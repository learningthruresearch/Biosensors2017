# execute this with python2, python3 doesn't seem to like next() method

import glob

interesting_files = glob.glob("*.csv")       # Create a iterable of files with the .csv pattern in their path, from the repository where the programm is executed

header_saved = False                         # Create a Boolean, to indicate that headers of the csv have already been added or not
with open('output.csv','wb') as fout:        # create a output object csv file in which you will put the csv files to merge
    for filename in interesting_files:       # interate on interesting_files
        with open(filename) as fin:          # create a file object for every file in interesting_file
            header = next(fin)               # create an object containing the firt line of each file object
            if not header_saved:             # verify the condition : this will only be verified for the first file object
                fout.write(header)           # write the first line of the first file object in the output
                header_saved = True          # make sure that the first line of the other csv files will not be written in the ouput
            for line in fin:                 # iterate on all the file objects inside interesting_files
                fout.write(line)             # write each line of a file object (except the first) in the output file
