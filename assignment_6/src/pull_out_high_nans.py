import csv

### This code finds all of the cells in the MERFISH cell boundaries data with high
### numbers of NaN's

# Change this to point to your cell boundaries csv!
csv_name = "/data/harvardccb22/data-mouse-hypothalamus/high_resolution_cell_boundaries.csv"


# Open relevant csv readers and writers, parse the data line by line and save formatted
# versions in another csv file
with open(csv_name) as input:
    with open('high_nan_boundaries.csv', 'w+') as output: #w+ makes sure we overwrite existing data
        data_reader = csv.reader(input, delimiter=',')
        next(data_reader) # Skip the header! 
        data_writer = csv.writer(output, delimiter=',')
        data_writer.writerow(['layer', 'feature_uid', 'feature_id', 'x', 'y']) # Header for new csv
        for row in data_reader:
            for i in range(7):
                # The x's and y's live from cols 6 to 19 so we map from layer id to that
                x_list = row[6+2*i]
                y_list = row[7+2*i]

                # Parse our x and y-lists into lists of ordered floats
                x = x_list.replace(' ', '').split(';')[:-1]
                y = y_list.replace(' ', '').split(';')[:-1]

                if len(x) > 0 and len(y) > 0: 
                    percent = ((x.count('NaN') + y.count('NaN'))/(len(x) + len(y)))*100

                    # Add to new csv if the percentage exceeds 10%
                    if percent > 10:
                        x.append(x[0])
                        y.append(x[0])
                        data_writer.writerow([i, row[0], row[1], x, y])
