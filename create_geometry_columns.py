"""
create_geometry_columns.py
Create new columns of geometry strings to be used in SQL commands
@ Alicia Lu, Jan. 31 2023
"""
import pandas as pd
from tqdm import tqdm


def create_point_column(f_name):
    molecule = pd.read_csv(f_name)
    molecule['point'] = molecule.apply(lambda x: "POINT(" + str(x['x_pixel']) +
            " " + str(x['x_pixel']) + ")", axis=1)
    molecule['z_pixel_int'] = molecule.apply(lambda x: int(x['z_pixel'] /
        13.76819064), axis=1)
    molecule.to_csv(f_name)
    print(f"File {f_name} modified!")


def create_polygon_column(f_toread, f_towrite):
    df = pd.read_csv(f_toread)
    new_df = pd.DataFrame(index=None)
    new_df.assign(cell="", z="", polygon="")

    for z in range(1, 10):
        num_cells = len(df.loc[df['z'] == z])
        for cell in tqdm(range(1, num_cells+1)):
            polygon = make_polygon(z, cell, df)
            new_df = new_df.append({"cell": str(cell), "z": str(z), "polygon": polygon}, ignore_index=True)
            new_df.to_csv(f_towrite, index=False)


def make_polygon(z, cell, df):
    z_df = df.loc[df['z'] == z] # select z
    z_df['point'] = z_df[['x', 'y']].apply(lambda x: str(x['x']) + " " + str(x['y']), axis=1)
    return 'POLYGON((' + z_df.loc[z_df['cell'] == cell]['point'].str.cat(sep=',') + '))'


if __name__ == "__main__":
    #create_point_column("MoleculeGeometryTest.csv")
    create_polygon_column("baysor_polygons.csv", "polygon.csv")
