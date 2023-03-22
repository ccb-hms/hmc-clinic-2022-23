import pandas as pd

# Load in the data
ds_path = "/Users/kunyangalicialu/Documents/mudd/senior/clinic/data_release_baysor_merfish_gut/data_analysis/baysor/segmentation/segmentation.csv"

df = pd.read_csv(ds_path)

# Use groupby to sort the molecules into clusters based on z-layer and cell id, then apply
# makeMultiPoint to those rows to get MULTIPOINT strings
scaler = 13.768190639243800
# Get the z_layer label
df['z'] /= scaler

## it turns out we probably need to use a combination of `df.groupby` and
## `pd.cut` here is a toy example below. I'd like to model based on that (AL)
## the code snippet below categorize numbers (randomly generated) into the
## specified bins
df= pd.DataFrame({'number': np.random.randint(1, 100, 10)})
df['bins'] = pd.cut(x=df['number'], bins=[1, 20, 40, 60,
                                          80, 100])


# Function that takes in rows of data, produces a valid MULTIPOINT for SQL Server
def makeMultiPoint(x):

    return 0
