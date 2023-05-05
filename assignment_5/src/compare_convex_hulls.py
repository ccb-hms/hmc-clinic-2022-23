import json
import pandas as pd
import matplotlib.pyplot as plt

# Takes the layer and id of a cell and plots its boundaries against the convex hull result
# layer (int) : The layer of the desired cell/hull, starting from 0
# id (int) : The cell id of the starting cell/hull, starting from 0
# showCell (bool) : Whether you want to plot the matching cell or not
def compare_cell_and_points(layer, id, showCell):

    # Load the convex hull data (stored as a csv of unprocessed SQL POLYGONS)
    hull_csv = pd.read_csv('Layer1ConvexHulls.csv', header=0) 

    # Find the right row in the table
    hullString = hull_csv.loc[(hull_csv['layer_id'] == layer) & (hull_csv['cell_id'] == id), ['hull_string']].values[0][0]

    # We need to determine whether resulting hull is a POLYGON, LINESTRING, POINT, or NULL
    if type(hullString) == float: # Type of float means that our string was read as nan, and is NULL
        print("Sorry, no convex hull was computed.")
        return
    elif hullString[:7] == "POLYGON":
        hullString = hullString[10:len(hullString)-2] # Remove text, get just the points
    elif hullString[:5] == 'POINT':
        hullString = hullString[8:len(hullString)-2] # Remove text, get just the points
    elif hullString[:10] == 'LINESTRING':
        hullString = hullString[12:len(hullString)-2] # Remove text, get just the points

    # Parse the points based on commas and spaces, get into nested list
    hull_split = [i.split(' ') for i in (hullString.split(', '))]

    # Convert each point to floats
    hull_points = [list(map(float, point)) for point in hull_split]

    # Add x's and y's to separate lists for plotting
    x_hull = [lst[0] for lst in hull_points]
    y_hull = [lst[1] for lst in hull_points]

    # Load the segmentation molecule data
    # Change this location as needed!
    points_csv = pd.read_csv('/Users/cgcouto/Downloads/data_release_baysor_merfish_gut/data_analysis/baysor/segmentation/segmentation.csv', header=0)
        
    # Find the proper points that (should) make up the convex hull
    # Need to use id+1 because cell id's start at 1 in this file (0 is reserved for noisy data points)
    x_molecules = points_csv.loc[(points_csv['z'] == 0) & (points_csv['cell'] == id+1) & (points_csv['is_noise'] == False), ['x']].values.tolist()
    y_molecules = points_csv.loc[(points_csv['z'] == 0) & (points_csv['cell'] == id+1) & (points_csv['is_noise'] == False), ['y']].values.tolist()

    # Add it to the final plot

    plt.plot(x_hull, y_hull)
    plt.scatter(x_molecules, y_molecules)

    if showCell:

        # Load the cell data
        f = open('poly_per_z.json')
        data = json.load(f)

        # Arrays for storing x and y-coordinates
        x_cell = []
        y_cell = []

        coordinates = data[layer]['geometries'][id]['coordinates'][0]

        # Fill up the x's and y's
        for point in coordinates:
            x_cell.append(point[0])
            y_cell.append(point[1])

        plt.plot(x_cell,y_cell)
    
    plt.show()

# Run some examples!
compare_cell_and_points(0, 0, False)
# compare_cell_and_hull(0, 51, False)
# compare_cell_and_hull(0, 0, True)
# compare_cell_and_hull(0, 51, True)
