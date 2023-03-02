import json
import matplotlib.pyplot as plt

# Takes the layer and id of a cell and plots its boundaries against the convex hull result
def compare_cell_and_hull(layer, id):

    # Load the cell data
    f = open('poly_per_z.json')
    data = json.load(f)

    # We'll have a csv of layer, id, and polygon string we'll need to import
    # Then we'll get the appropriate polygon from that
    # So this is just a test string for now
    hullString = "POLYGON((-5 -5, -5 5, 5 5, 5 -5, -5 -5)"

    hullString = hullString[9:len(hullString)-1] # Get just the points

    # Parse the points based on commas and spaces, get into nested list
    hull_split = [i.split(' ') for i in (hullString.split(', '))]

    # Convert each point to floats
    hull_points = [list(map(float, point)) for point in hull_split]

    # Add x's and y's to separate lists for plotting
    x_hull = [lst[0] for lst in hull_points]
    y_hull = [lst[1] for lst in hull_points]

    # Arrays for storing x and y-coordinates
    x_cell = []
    y_cell = []

    coordinates = data[layer]['geometries'][id]['coordinates'][0]

    # Fill up the x's and y's
    for point in coordinates:
        x_cell.append(point[0])
        y_cell.append(point[1])

    plt.plot(x_cell,y_cell)
    plt.plot(x_hull, y_hull)
    plt.show()

compare_cell_and_hull(0,0)