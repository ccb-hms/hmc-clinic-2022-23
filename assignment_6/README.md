# Assignment 6 <a name="assignment6"></a>

Note: Some portions of this README are adapted from the assignments provided to us by the Harvard CCB liaison team.

## Contents

<ol>
<li><a href="#desc">Description</a></li>
<li><a href="#anat">Anatomy of the MERFISH mouse hypothalamus dataset</a></li>
<li><a href="#inst">Installation</a></li>
<li><a href="#scripts">Scripts</a></li>
<li><a href="#tasks">Tasks</a></li>
<li><a href="#exec">Execution</a></li>
</ol>

## Description <a name="desc"></a>

Note: This section is adapted from the assignments provided to us by the Harvard CCB liaison team.

For this assignment, we return to the MERFISH mouse hypothalamus dataset that we started to work on in Assignment 3.

Moffitt et al., 2018 developed an imaging-based cell type identification and mapping method and combined it with single-cell
RNA-sequencing to create a molecularly annotated and spatially resolved cell atlas of the mouse hypothalamic preoptic region.
Cell segmentation was carried out based on total polyadenylated mRNA and DAPI nuclei costains. Combinatorial smFISH imaging 
was used for the identification and spatial expression profiling of 161 genes in 1,027,848 cells from 36 mice (16 female, 20 male).
For each mouse, the preoptic region has been sectioned into twelve tissue slices from anterior to posterior position of the preoptic region.

Definitions:
* **hypothalamic preoptic region**: part of the anterior hypothalamus that controls essential social behaviors and homeostatic functions.
* **bregma**: the anatomical point on the skull at which the coronal suture is intersected perpendicularly by the sagittal suture. 
Used here as a reference point for the twelve 1.8- by 1.8-mm imaged slices along the z-axis.
*(Note: The anterior position of the preoptic region is at Bregma +0.26.)*

In Assignment 3, we worked with the segmented and quantified expression table as available from the datadryad data publication.
For Assignment 6, we will go back to the unprocessed data (molecule data and cell polygons), which is not publicly available, 
but has been obtained in-house from Jeffrey Moffitt's lab.
The goal is to largely reproduce the tasks of Assignment 5 for a much bigger dataset, and to evaluate the scalability of the 
geometry operations in the spatial SQL setting.

## Anatomy of the MERFISH mouse hypothalamus dataset <a name="anat"></a>
<ul>
<li> Data </li>  
<ul>
  <li> mRNA molecule data: ~500 M observations for 135 genes (15 GB csv file) </li>
  <li> Cell polygons obtained from Watershed segmentation: ~1 M cells from 36 mice (16 female, 20 male, 7 GB csv file). </li>
</ul>
</ul>

## Scripts <a name="scripts"></a>

Here follows a list of the source code we've included for this assignment.

* [compare_convex_hulls.py](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_6/src/compare_convex_hulls.py) - 
Python script that generates plots for the convex hull for a polygon and the original cell boundary, given an id number

* [computeConvexHulls.sql](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_6/src/ComputeConvexHulls.sql) - 
SQL script that computes the convex hulls for all cells in a specific animal, layer, bregma

* [count_nans.sql](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_6/src/count_nans.py) - 
Python script that analyzes how many NaNs are in the original segmentation data

* [display_nans.sql](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_6/src/display_nans.sql) - 
Python script that plots a distribution of how many NaNs are in the original segmentation data

* [get_cell_borders.py](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_6/src/get_cell_borders.py) - 
Important Python script for processing the raw cell boundaries data into a format that can be understood by SQL.

* [getCellNames.sql](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_6/src/getCellNames.sql) - 
Deprecated

* [importAllData.sql](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_6/src/importAllData.sql) - 
SQL script for doing a bulk import of the Molecules table and the (already preprocessed) CellPolygons table (with polygons represented as strings). 
  Also creates a primary key id column for both. Handy for running all imports at the same time and walking away

* [importCellBoundaries.sql](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_6/src/importCellBoundaries.sql) - 
SQL script for doing a bulk import of the (already preprocessed) CellPolygons table (with polygons represented as strings). Also creates a primary key id column

* [importMolecules.sql](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_6/src/importMolecules.sql) -
SQL script for doing a bulk import of the Molecules table. Also creates a primary key id column

* [pull_out_high_nans.py](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_5/src/pull_out_high_nans.py)
Python script that creates a CSV describing all cells with more than 10% NaNs.


## Tasks <a name="tasks"></a>

Note: This section is adapted from the assignments provided to us by the Harvard CCB liaison team.
  
1. Obtain the molecule data and the cell polygon data from CCB's AWS S3 bucket using the AWS command line interface (note: these are big files - best carried out on an institutional computer cluster):
  a. aws s3 cp https://LINK-REDACTED-FOR-SECURITY/merfish_barcodes.csv /<destination>/merfish_barcodes.csv
  b. aws s3 cp https://LINK-REDACTED-FOR-SECURITY/high_resolution_cell_boundaries.csv /<destination>/high_resolution_cell_boundaries.csv


Repeat subtasks 2-5 from Assignment 5 for the MERFISH mouse hypothalamus dataset.
Note that in addition to the 7 z-frames for each tissue slice, we now have 12 tissue slices
(at different bregma positions) for each of the 36 mice. This needs to be taken into account for all geometry operations.

  
2. Create an SQL table for both data components, i.e. 1) one table representing the molecules as spatial points given their x, y, and z-coordinates (using the pixel coordinates), and 2) one table representing the cells as polygons. It is a good exercise to create the cell polygon table directly from the json format. Alternatively, the cell polygon coordinates in a flattened 2D table format can be obtained from [dropbox](https://www.dropbox.com/s/n6rf3sastdo9fn5/baysor_polygons.csv?dl=0). 

3. Perform spatial overlap queries between the molecule table and the cell polygon table to create a new SQL table. The resulting table should contain three columns (gene, cell, molecule count) and store for each gene the number of molecules overlapping with each cell. Also record the execution time of your queries to produce this molecule count table (best to calculate average execution time from performing queries repeatedly).

4. Reshape the molecule count table to a two-dimensional expression matrix (gene x cell). The resulting expression matrix should store for each gene the number of molecules overlapping with each cell. This will involve a pivot operation in the database and can alternatively also be performed in R/Python based on the molecule count table produced in 3.

5. Proceed by inspecting the molecule to cell assignment for the Baysor segmentation in data_analysis/baysor/segmentation/segmentation.csv. One issue with the polygon coordinates in the json file is that there is no 1:1 mapping between these polygons and the cell metadata. We therefore aim to reconstruct the cell boundaries by computing [convex hulls](https://learn.microsoft.com/en-us/sql/t-sql/spatial-geometry/stconvexhull-geometry-data-type?view=sql-server-ver16) around all molecules assigned to a cell. As before: record the average execution time of your queries to produce a table of convex hull geometries for each of the 5800 cells in the segmentation csv file. 

## Execution <a name="exec"></a>

To run our code for this assignment, follow along in [our Notebook](Notebooks/Assignment6Notebook.ipynb). 

