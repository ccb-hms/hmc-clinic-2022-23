# Assignment 3 
Note: This section is adapted from the assignments provided to us by the Harvard CCB liaison team.

## Contents

	<ol>
	<li>Description</li>
	<li>Tasks</li>
	<li>Installing</li>
	<li>Executing Program</li>
	</ol>

## Description

Recreate a part of the SummarizedExperiment paradigm for storing and representing gene expression data in a relational database setting by linking two data tables (expression data and cell metadata).

## Tasks
 
Obtain the segmented expression data from the [MERFISH mouse hypothalamus dataset from DataDryad](https://doi.org/10.5061/dryad.8t8s248). Divide the obtained csv file into 1) columns storing expression levels of individual genes, and 2) cell metadata such as animal ID, animal sex, and cell class. Create a SQL table for both data components, with the two tables being linked by the cell ID.
Perform a number of select queries to obtain eg. 
a) all cells of a certain cell type, 
b) all cells of female mice, and 
c) all pericytes with non-zero expression of the Ace2 gene.

## Installing

The segmented expression data can be downloaded from [datadryad](https://doi.org/10.5061/dryad.8t8s248).

## Executing program

(TODO: add our sample execution code)

