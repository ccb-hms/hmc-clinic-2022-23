import csv
from collections import Counter
import numpy as np

### This code finds the number of nan's in the original Moffitt et al. cell boundaries data
### from Harvard CCB's AWS S3 bucket

### Point csv_name to csv of MERFISH cell boundaries you want to analyze
csv_name = "/data/harvardccb22/data-mouse-hypothalamus/high_resolution_cell_boundaries.csv"
null_percents = []

# Open relevant csv readers and writers, parse the data line by line and save formatted
# versions in another csv file
with open(csv_name) as input:
    data_reader = csv.reader(input, delimiter=',')
    next(data_reader) # Skip the header! 
    for row in data_reader:
        for i in range(7):
                # The x's and y's live from cols 6 to 19 so we map from layer id to that
            x_list = row[6+2*i]
            y_list = row[7+2*i]
            x = x_list.replace(' ', '').split(';')[:-1]
            y = y_list.replace(' ', '').split(';')[:-1]
            if (len(x) + len(y)) > 0:
                percent = (x.count('NaN') + y.count('NaN')) / (len(x) + len(y)) * 100
                null_percents.append(percent)

np.save("nan_distribution.npy", null_percents)
