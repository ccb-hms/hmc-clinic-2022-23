import pandas as pd
import numpy as np


# Read in table that contains the gene and cell counts
data_path = "../data/counts.csv"
df = pd.read_csv(data_path)

# Reshape the table into a matrix
pivoted_df = df.pivot(index="cells",
                      columns="genes",
                      values="counts")

# Sanity checks
correct_num_genes = len(np.unique(list(df["genes"])))
correct_num_cells = len(np.unique(list(df["cells"])))

if "cells" in list(pivoted_df.columns):
    genes = list(pivoted_df.columns).remove("cells")
else: genes = list(pivoted_df.columns)
num_cells = len(pivoted_df.index)

assert len(genes) == correct_num_genes, f"Expect {num_genes} genes, but our table has {len(genes)}"
assert num_cells == correct_num_cells, f"Expect {num_cells} cells, but our table has {len(cells)}"

# Save pivoted table to new .CSV file
pivoted_df.to_csv("../data/gene_cell_matrix.csv")
print("Successfully saved gene cell matrix data :)")
