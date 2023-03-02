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
	<ol type="a">
	<li>Description</li>
	<li>Coursera</li>
	<li>Running lab assignments in SQL Server</li>
	</ol>
<li> <a href="#assignment2">Assignment 2</a> </li>
<li> <a href="#assignment3">Assignment 3</a> </li>
<li> <a href="#assignment4">Assignment 4</a> </li>
<li> <a href="#assignment5">Assignment 5</a> </li>
	<ol type="a">
	<li>Description</li>
	<li>Anatomy of the MERFISH mouse ileum dataset</li>
	<li>Installation</li>
	<li>Scripts</li>
	<li>Tasks</li>
	<li>Execution</li>
	</ol>
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

### Description

If you are not already familiar with relational database systems and working with Microsoft SQL Server,  we recommend that you follow the steps below to familiarize yourself with them. 

Note: This section is adapted from the assignments provided to us by the Harvard CCB liaison team.

### Coursera 

You may audit the following course for free on Coursera: [Introduction to Relational Databases](https://www.coursera.org/learn/introduction-to-relational-databases#syllabus)

We completed the following parts of the Coursera course:
* **Week 1**
	* All videos in both modules
* **Week 2**
	* All videos in both modules
	* Lab assignments (one in each module)
		* See [note](#labAssign) below on running lab assignments in SQL Server
		* The second lab introduces primary and foreign keys, but for some reason stops short of having you implement a JOIN. See [this introduction to SQL joins](https://www.datacamp.com/tutorial/introduction-to-sql-joins) (ignore the first section on setting up PostgreSQL) And figure out how to join the tables that you ended up with at the end of the second lab based on their primary and foreign keys.
* **Week 3**
	* Videos:
		* “Using Keys and Constraints in MySQL”
		* “Views”
	* Exercise:
		* Create a view in the SQL Server database created in the Labs from Week 2 that returns the rows of the BookShop table where the price is < $100 and the book was published after year 2010.
* **Week 4**
	* Videos:
		* “Approach to Database Design (Including ERD)”

### Running lab assignments in SQL Server <a name="labAssign"></a>

Run the lab assignments in SQL Server in Docker instead of on IBM’s cloud platform. Follow [these instructions](https://www.sqlshack.com/how-to-set-up-and-run-sql-server-docker-image/) to get set up with SQL Server and Azure Data Studio. The SQL scripts in the labs should work in SQL Server, but you will need to add this to the top of the first script to create a new database called MyLabProject and use it for subsequent operations: 
```
CREATE DATABASE MyLabProject
 
USE MyLabProject
GO
```
Execute the statements in the scripts one-at-a-time in ADS.  The statements to DROP the tables will fail the first time you run the script.  MS's dialect of SQL, called Transact-SQL or T-SQL, has [syntactic sugar to work around this](https://learn.microsoft.com/en-us/sql/t-sql/statements/drop-table-transact-sql?view=sql-server-ver16) if you'd like to experiment.

Explore the ADS UI  to view table structure, etc. as they do in the IBM tool in the lab.
 

 


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
