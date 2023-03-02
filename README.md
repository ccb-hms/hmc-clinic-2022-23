# Leveraging Relational Databases for Spatial Transcriptomics

This is the repository for the 2022-2023 Harvey Mudd Clinic Team in collaboration with Harvard Center for Computational Biomedicine.

## Table of Contents
<ol>
<li> <a href="#description">Description</a> </li>
<li> <a href="#starting">Getting Started</a> </li>
	<ol type="a">
	<li>Dependencies</li>
</ol>
<li> <a href="#assignment1">Assignment 1</a> </li>
<li> <a href="#assignment2">Assignment 2</a> </li>
<li> <a href="#assignment3">Assignment 3</a> </li>
<li> <a href="#assignment4">Assignment 4</a> </li>
<li> <a href="#assignment5">Assignment 5</a> </li>
<li> <a href="#authors">Authors</a> </li>
<li> <a href="#acknowledgements">Acknowledgements</a> </li>
</ol>

## Description <a name="description"></a>

At Harvard CCB, researchers are pioneering the study of various biological and spatial genomic datasets using computational methods. These high-resolution biological datasets collected using imaging techniques can be quite large. Most workflows involve mainly Python and R, which cannot be effectively used to analyze such memory-intensive datasets. We aim to leverage relational database queries in SQL to improve scalability, add flexibility to analyze larger datasets, and eventually find additional underlying spatial relationships in the original data. 

## Getting Started <a name="starting"></a>

### Dependencies

To run our scripts and follow along with our process, you'll need to have the following installed.

* Python
* Some Python packages:
  * pandas
  * tqdm
* Azure Data Studio
* Git
* Docker

## Assignment 1 <a name="assignment1"></a>

Assignment 1 is an introduction to SQL Server consisting of a Coursera course on Relational Databases and a few corresponding exercises. \
For a breakdown of each step in assignment 1, see the [assignment 1 README.](assignment_1/README.md)

## Assignment 2 <a name="assignment2"></a>

Assignment 2 focuses on a few exercises with queries in SQL Server in order to gain practice in using the tools we learned about in assignment 1. The assignment uses some flight data and asks us to use queries to find information such as which plane logged the most flight miles. \
For a breakdown of each step in assignment 2, see the [assignment 2 README.](assignment_2/README.md)

## Assignment 3 <a name="assignment3"></a>

Assignment 3 consists of two subtasks: the first to read and present on recent reviews in spatially-resolved omics profiling, and the second to practice working with spatial omics data in SQL Server. This repository will focus only on the second subtask. \
For a breakdown of each step in this subtask of assignment 3, see the [assignment 3 README.](assignment_3/README.md)

## Assignment 4 <a name="assignment4"></a>

Assignment 4 serves as a transition into working with spatial data. We are tasked with analyzing two tables: one containing weather data along iwht latitude and longitude of the weather station, and one containing geographical information. Our goal was to answer questions such as the windiest stations in Massachusetts, or the rainiest statin in Washington, by performing spatial intersect queries on the tables. \
For a breakdown of each step of assignment 4, see the [assignment 4 README.](assignment_4/README.md)

## Assignment 5 <a name="assignment5"></a>

Assignment 5 finally brings our attention to spatial transcriptomics data in SQL Server. We are given multiple subtasks, such as creating a new gene-cell-molecule count table, reshaping that table into a gene expression matrix, and creating convex hulls around every molecule in a given cell. \
For a breakdown of each step of assignment 5, see the [assignment 5 README.](assignment_4/README.md)
You may also follow along in our [assignment 5 notebook.](Notebooks/Assignment5NotebookSummarized.ipynb)

## Authors <a name="authors"></a>

[Chris Couto](https://github.com/cgcouto)

[Alicia Lu](https://github.com/kunyanglu)

[Elizabeth Lucas-Foley](https://github.com/elucasfoley)

[Mads Mansfield](https://github.com/Paruhdoks)


## Acknowledgments <a name="acknowledgements"></a>

Ludwig Geistlinger

Robert Gentleman

Rafael Goncalves

Tyrone Lee

Nathan Palmer

Sunil Poudel

Sam Pullman
