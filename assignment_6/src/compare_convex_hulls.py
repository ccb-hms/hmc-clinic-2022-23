import json
import pandas as pd
import matplotlib.pyplot as plt


# Load the convex hull data
hull_csv = pd.read_csv('/Users/clinic2022/Desktop/convexhullsA6.csv', header=0) 
# Load the cell segmentation data
points_csv = pd.read_csv('/Users/clinic2022/Desktop/high_resolution_cell_boundaries_head.csv', header=0)

# Takes the layer and id of a cell and plots its boundaries against the convex hull result
# layer (float) : The layer of the desired cell/hull, ranging from 0 to 9 in increments of 1.5
# id (int) : The cell id of the starting cell/hull, starting from 1
# showCell (bool) : Whether you want to plot the matching cell or not
def compare_cell_and_hull(id, animal, bregma, layer, showCell):
    fname = "/Users/clinic2022/Desktop/convex_hull_images/convex_hull_cell_"+str(id)+".png"

    # Find the right row in the table
    hullString = hull_csv.loc[(hull_csv['cell_id'] == id)
                                & (hull_csv['animal_id'] == animal)
                                & (hull_csv['bregma'] == bregma)
                                & (hull_csv['z_layer'] == layer), 
                               ['hull']].values[0][0]

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

    # Add it to the final plot
    plt.plot(x_hull, y_hull)

    if showCell:
            
        # Find the points that make up the boundary of the cell
        x_points = points_csv.loc[(points_csv['feature_ID'] == id), ['abs_x_boundary_1']].values[0][0].split(";")[:-1]
        y_points = points_csv.loc[(points_csv['feature_ID'] == id), ['abs_y_boundary_1']].values[0][0].split(";")[:-1]

        x_points = [float(x) for x in x_points]
        y_points = [float(y) for y in y_points]

        # Add it to the final plot
        plt.plot(x_points, y_points)
    
    plt.xlabel('x')
    plt.ylabel('y')

    plt.savefig(fname)
    plt.show()

# Run some examples!
compare_cell_and_hull(1, 4, -0.14, 0, True)
compare_cell_and_hull(2, 4, -0.14, 0, True)
compare_cell_and_hull(5, 4, -0.14, 0, True)
compare_cell_and_hull(6, 4, -0.14, 0, True)
compare_cell_and_hull(7, 4, -0.14, 0, True)
compare_cell_and_hull(9, 4, -0.14, 0, True)
compare_cell_and_hull(10, 4, -0.14, 0, True)
