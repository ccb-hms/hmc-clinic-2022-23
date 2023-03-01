import pandas
import json
import math
import csv
from tqdm import tqdm

# Edit this so the code knows where your json file is!
JSON_PATHNAME = "C:/Users/elflu/OneDrive/Desktop/clinic/data_release_baysor_merfish_gut/data_analysis/baysor/segmentation/poly_per_z.json"
#'/Users/cgcouto/Downloads/data_release_baysor_merfish_gut/poly_per_z.json'

# Open the json file and parse it as json
f = open(JSON_PATHNAME)
data = json.load(f)

polygons = []
z_ids = []
cell_ids = []

# Function that removes every second comma in the coordinates
def removeCommas(s):
    counter = 0
    for num in range(len(s)-(math.floor((s.count(',')+1)/2))):
        if s[num] == ',':
            counter += 1
            if counter%2 == 1:
                s = s[:num] + s[num+1:]
    return s


for layer in tqdm(range(0, 9)): # Go through each layer
    for id in range(0, len(data[layer]['geometries'])): # Go through every cell there

        # Pull out just the coordinates comprising the boundary
        coordinates = str([[int(val[0]), int(val[1])] for val in data[layer]['geometries'][id]['coordinates'][0]])

        # Get rid of unnecesary brackets
        for char in ["[", "]"]:
            coordinates = coordinates.replace(char, "")

        # Remove every second comma to get in form X Y, instead of X, Y,
        coordinates = removeCommas(coordinates)

        # Add extra syntax needed for SQL
        coordinates = "POLYGON((" + coordinates + "))"

        # Append to running list of polygons
        polygons.append(coordinates)
        z_ids.append(layer+1)
        cell_ids.append(id+1)

print(len(polygons)) # Check that we've got all of them...

# Move stuff into dataframe and save as csv!
df = pandas.DataFrame({'z': z_ids,
                       'cell': cell_ids,
                       'polygons':polygons},
                       index=None)
df.to_csv('baysor_SQL_polygons.csv', quoting=csv.QUOTE_NONE)
