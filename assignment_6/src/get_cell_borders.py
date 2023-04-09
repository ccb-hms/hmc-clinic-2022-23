import csv

csv_name = "/Users/cgcouto/Downloads/data_release_baysor_merfish_gut/assignment_6_boundaries/high_resolution_cell_boundaries_head.csv"

# Cols 0 and 1 are the feature_uID and feature_ID respectively
# Cols 6 through 19 are the alternating x-y pairs

# Function that takes in two lists of x's and y's (separated by semicolons)
# and gets them into the desired POLYGON((X Y, ...)) format for SQL
def create_polygon(x_string, y_string):

    # First split based on NaNs (if any are present)
    x_split = [poly.split(';') for poly in x_string.replace(' ', '').split('NaN')]
    y_split = [poly.split(';') for poly in y_string.replace(' ', '').split('NaN')]

    # Remove any empty strings in our list of lists
    x = [[point for point in poly if point != ''] for poly in x_split]
    y = [[point for point in poly if point != ''] for poly in y_split]

    all_points = []

    for i in range(len(x)):
        if len(set(x[i])) >= 3 and len(set(y[i])) >= 3: # Needs to have at least three unique points to be a SQL polygon
            
            # Duplicate start point on end
            x[i].append(x[i][0])
            y[i].append(y[i][0])

            # Clump x's and y's together, add to running list
            all_points.append(zip(x[i],y[i]))

    if len(all_points) == 0: # If there are no polygons, return no string represetation
        return
    elif len(all_points) == 1: # Needs to be a POLYGON
        return 'POLYGON((' + ','.join([f'{x} {y}' for x, y in all_points[0]]) + '))'
    else: # Needs to be a MULTIPOLYGON
        polygon_str = 'MULTIPOLYGON('
        for points in all_points:
            polygon_str += '(('
            polygon_str += ', '.join([' '.join(map(str, p)) for p in points])
            polygon_str += ')), '
        polygon_str = polygon_str.rstrip(', ')
        polygon_str += ')'

        return polygon_str
    

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
                if type(cell_boundary) == str:
                # Save the new row!
                    data_writer.writerow([i, row[0], row[1], cell_boundary])

                