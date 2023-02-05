import math
import json
import matplotlib.pyplot as plt
from shapely.geometry import LineString
import os

# Function uses the shapely is_simple method to find which cell boundaries
# intersect itself (making them invalid in SQL)
def check_cells(savePics):
    # Get the data
    f = open('poly_per_z.json')
    data = json.load(f)

    # Counters for the strange cells we find
    totalCount = 0
    weirdCount = 0

    # Stores layer and id for each weird cell
    badOnes = []

    for layer in range(0,9): # Go through each layer
        for id in range(len(data[layer]['geometries'])): # Go through every cell there
            # Load the relevant boundary points
            coordinates = data[layer]['geometries'][id]['coordinates'][0]

            # Pack the points into a shapely LineString
            polygon = LineString(coordinates)

            # Pull out all the x and y-coordinates (to test for lines)
            x = []
            y = []
            for point in coordinates:
                x.append(point[0])
                y.append(point[1])
            
            # If it's not simple, then it's either weird or a straight line
            if (not polygon.is_simple):
                totalCount += 1
                # This test filters out the straight lines
                if (not all(val == x[0] for val in x) and not all(val == y[0] for val in y)):
                    weirdCount += 1
                    badOnes.append([layer,id]) 

    numCells = 33861 # Let's compare against the total number of cells in the data!

    print("Number of off cells (including straight line cells): " + \
        str(totalCount) + " (" + str(round((totalCount/numCells)*100,3)) + "% of total)")
    print("Without the straight line cells: " + str(weirdCount) + \
        " (" + str(round((weirdCount/numCells)*100,3)) + "% of total)")

    # Save all the weird ones (not straight lines) as images if we want
    if (savePics):
        os.chdir('/Users/cgcouto/Downloads/data_release_baysor_merfish_gut/weirdcells')

        for cell in badOnes:
            filename = "layer" + str(cell[0]) + "cell" + str(cell[1]) + ".png"
            x = []
            y = []

            coordinates = data[cell[0]]['geometries'][cell[1]]['coordinates'][0]
            for point in coordinates:
                x.append(point[0])
                y.append(point[1])
        
            plt.plot(x,y)
            plt.savefig(filename)
            plt.clf()

check_cells(False)