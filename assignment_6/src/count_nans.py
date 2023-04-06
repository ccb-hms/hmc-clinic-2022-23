import csv
from collections import Counter

csv_name = "/Users/cgcouto/Downloads/data_release_baysor_merfish_gut/high_resolution_cell_boundaries_head.csv"


# Open relevant csv readers and writers, parse the data line by line and save formatted
# versions in another csv file
with open(csv_name) as input:
    nans = Counter()
    data_reader = csv.reader(input, delimiter=',')
    next(data_reader) # Skip the header! 
    for row in data_reader:
        for i in range(7):
                # The x's and y's live from cols 6 to 19 so we map from layer id to that
            x_list = row[6+2*i]
            y_list = row[7+2*i]
            x = x_list.replace(' ', '').split(';')[:-1]
            y = y_list.replace(' ', '').split(';')[:-1]
            nans[str(x.count('NaN')+y.count('NaN'))] += 1
    print(nans.most_common())