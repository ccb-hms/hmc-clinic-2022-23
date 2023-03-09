import pandas as pd

# Load in the data
df = pd.read_csv('/Users/cgcouto/Downloads/data_release_baysor_merfish_gut/data_analysis/baysor/segmentation/segmentation.csv')


# Use groupby to sort the molecules into clusters based on z-layer and cell id, then apply
# makeMultiPoint to those rows to get MULTIPOINT strings

# multipoint_array = df.groupby()


# Function that takes in rows of data, produces a valid MULTIPOINT for SQL Server
def makeMultiPoint(x):

    return 0