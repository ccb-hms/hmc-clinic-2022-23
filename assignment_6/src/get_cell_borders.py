import csv

csv_name = "/Users/cgcouto/Downloads/data_release_baysor_merfish_gut/high_resolution_cell_boundaries_head.csv"

# Cols 0 and 1 are the feature_uID and feature_ID respectively
# Cols 6 through 19 are the alternating x-y pairs

# Function that takes in two lists of x's and y's (separated by semicolons)
# and gets them into the desired POLYGON((X Y, ...)) format for SQL
def create_polygon(x_list, y_list):

    # Parse our x and y-lists into lists of ordered floats
    x = [float(num) for num in x_list.split(';')[:-1]]
    y = [float(num) for num in y_list.split(';')[:-1]]
    
    # Combine into one list via zip
    points = zip(x,y)

    # Need to get into POLYGON((x[0] y[0], x[1] y[1], ...)) format and return that string
    return 'POLYGON((' + ','.join([f'{x} {y}' for x, y in points]) + '))'

    

# Open relevant csv readers and writers, parse the data line by line and save formatted
# versions in another csv file
with open(csv_name) as input:
    with open('cell_boundaries_reformatted.csv', 'w+') as output: #w+ makes sure we overwrite existing data
        data_reader = csv.reader(input, delimiter=',')
        next(data_reader) # Skip the header! 
        data_writer = csv.writer(output, delimiter=',')
        data_writer.writerow(['layer', 'feature_uid', 'feature_id', 'geometry_string']) # Header for new csv
        for row in data_reader:
            for i in range(7):
                # The x's and y's live from cols 6 to 19 so we map from layer id to that
                cell_boundary = create_polygon(row[6+2*i], row[7+2*i])
                # Save the new row!
                data_writer.writerow([i, row[0], row[1], cell_boundary])

                