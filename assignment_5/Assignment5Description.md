# 5. Working with spatial transcriptomics data in SQL
## The MERFISH mouse ileum dataset
Spatial transcriptomics protocols based on in situ sequencing or multiplexed RNA fluorescent hybridization can reveal detailed tissue organization. However, distinguishing the boundaries of individual cells in such data is challenging. Current segmentation methods typically approximate cell positions using nuclei stains.

[Petukhov et al., 2021](https://doi.org/10.1038/s41587-021-01044-w), describe [Baysor](https://github.com/kharchenkolab/Baysor), a segmentation method, which optimizes 2D or 3D cell boundaries considering joint likelihood of transcriptional composition and cell morphology. Baysor can also perform segmentation based on the detected transcripts alone.
Petukhov et al., 2021, compare the results of Baysor segmentation (mRNA-only) to the results of a deep learning-based segmentation method called [Cellpose](https://github.com/MouseLand/cellpose) from [Stringer et al., 2021](https://doi.org/10.1038/s41592-020-01018-x). Cellpose applies a machine learning framework for the segmentation of cell bodies, membranes and nuclei from microscopy images.
Petukhov et al., 2021 apply Baysor and Cellpose to MERFISH data from cryosections of mouse ileum. The MERFISH encoding probe library was designed to target 241 genes, including previously defined markers for the majority of gut cell types.

Def. ileum: the final and longest segment of the small intestine.

Samples were also stained with anti-Na+/K+-ATPase primary antibodies, oligo-labeled secondary antibodies and DAPI. MERFISH measurements across multiple fields of view and nine z planes were performed to provide a volumetric reconstruction of the distribution of the targeted mRNAs, the cell boundaries marked by Na+/K+-ATPase IF and cell nuclei stained with DAPI.

The dataset can be obtained from the official [datadryad data publication](https://doi.org/10.5061/dryad.jm63xsjb2).

## Anatomy of the MERFISH mouse ileum dataset
Raw data  
* mRNA molecule data: 820k observations for 241 genes  
* Image data: stitched 9-frame z-stacks (DAPI / Membrane, 500 MB)  
Processed data  
* 3 different segmentations (Baysor, Cellpose, Baysor/Cellpose)  
* Cell clusters based on expression similarity  
\* Cell type labels based on marker gene expression in the clusters

## Assignment 5: Spatial overlap operations for gene expression quantification
1. Obtain the dataset from [datadryad](https://doi.org/10.5061/dryad.jm63xsjb2) and inspect the contents of the data release. Use the contained README for an orientation. There are two relevant parts here for us in the beginning: 1) the molecule data table in raw_data /molecules.csv, and 2) the cell polygon coordinates from the Baysor segmentation in data_analysis/baysor/segmentation/poly_per_z.json.
2. Create an SQL table for both data components, i.e. 1) one table representing the molecules as spatial points given their x, y, and z-coordinates (using the pixel coordinates), and 2) one table representing the cells as polygons. It is a good exercise to create the cell polygon table directly from the json format. Alternatively, the cell polygon coordinates in a flattened 2D table format can be obtained from [dropbox](https://www.dropbox.com/s/n6rf3sastdo9fn5/baysor_polygons.csv?dl=0). 
3. Perform spatial overlap queries between the molecule table and the cell polygon table to create a new SQL table. The resulting table should contain three columns (gene, cell, molecule count) and store for each gene the number of molecules overlapping with each cell. Also record the execution time of your queries to produce this molecule count table (best to calculate average execution time from performing queries repeatedly).
4. Reshape the molecule count table to a two-dimensional expression matrix (gene x cell). The resulting expression matrix should store for each gene the number of molecules overlapping with each cell. This will involve a pivot operation in the database and can alternatively also performed in R/Python based on the molecule count table produced in 3.
5. We proceed by inspecting the molecule to cell assignment for the Baysor segmentation in data_analysis/baysor/segmentation/segmentation.csv. One issue with the polygon coordinates in the json file is that there is no 1:1 mapping between these polygons and the cell metadata. We therefore aim to reconstruct the cell boundaries by computing [convex hulls](https://learn.microsoft.com/en-us/sql/t-sql/spatial-geometry/stconvexhull-geometry-data-type?view=sql-server-ver16) around all molecules assigned to a cell. As before: record the average execution time of your queries to produce a table of convex hull geometries for each of the 5800 cells in the segmentation csv file. 
