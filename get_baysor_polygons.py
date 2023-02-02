import pandas
import json
import math
from tqdm import tqdm

# Open the json file and parse it as json
f = open('poly_per_z.json')
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


for i in tqdm(range(1, 10)): # Go through each layer
    for j in range(1, len(data[i-1]['geometries'])+1): # Go through every cell there

        # Pull out just the coordinates comprising the boundary
        coordinates = str(data[i-1]['geometries'][j-1]['coordinates'][0])

        # Get rid of unnecesary brackets
        for char in ["[", "]"]:
            coordinates = coordinates.replace(char, "")

        # Remove every second comma to get in form X Y, instead of X, Y,
        coordinates = removeCommas(coordinates)

        # Add extra syntax needed for SQL
        coordinates = "POLYGON((" + coordinates + "))"

        # Append to running list of polygons
        polygons.append(coordinates)
        z_ids.append(i)
        cell_ids.append(j)

print(len(polygons)) # Check that we've got all of them...

# Move stuff into dataframe and save as csv!
df = pandas.DataFrame({'z': z_ids,
                       'cell': cell_ids,
                       'polygons':polygons},
                       index=None)
df.to_csv('baysor_SQL_polygons.csv')
