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
	<ol type="a">
	<li>Introduction</li>
	<li>Guidance</li>
	<li>Tasks</li>
	</ol>
<li> <a href="#assignment3">Assignment 3</a> </li>
	<ol type="a">
	<li>Description</li>
	<li>Tasks</li>
	</ol>
<li> <a href="#assignment4">Assignment 4</a> </li>
	<ol type="a">
	<li>Setup</li>
	<li>Data</li>
	<li>Exercises</li>
	</ol>
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

Note: This section is adapted from the assignments provided to us by the Harvard CCB liaison team.

### Introduction

We will be working with the nycflights13 data set [described in Chapter 13 of R for Data Science](https://r4ds.had.co.nz/relational-data.html#exercises-30).
 
If you wish to read through it, that chapter provides a nice overview of the semantics of working with relational data, along with a comprehensive treatment of the contemporary syntax for manipulating relational data natively in R data frames.  This reading is entirely optional, and provided as a point of reference, since we will make use of the example data set, but manipulate it in SQL Server instead of R data frames.
 
You will export the nycflights13 dataset from R and load it into SQL Server running in a container, where you will write SQL queries to answer a variety of questions about the flights, planes, etc.

### Guidance

#### Export the data from R

The first step will be to export the data from R to text files.  You can add the data library to your R installation with:
``` 
>install.packages("nycflights13")
 ```
There are five tables in the `nycflights13` dataset: planes, airlines, airports, flights, weather.  In R, you can learn more about these tables via the help system, e.g.:
 ```
>?nycflights13::flights
```
You can use the `write.table(...)` function in R to create delimited text files that contain the data from an R dataframe, tibble, matrix, etc.  For example:
 ```
>write.table(nycflights13::flights, file="flights.txt", sep="\t")
 ```
will create a file named flights.txt in the current R working directory, containing the data in the flights table, with columns separated by tabs, and strings double-quoted.

#### Make the exported files available to the SQL Server container

Once you have the five tables exported to delimited text files, you need to load them into SQL Server running in a container.  You should use the -v argument to the docker run invocation for the SQL Server container to bind mount the directory on your local file system that contains the text files into a file system location inside the container.  This will make them available for SQL Server to read when you are ready to load them into the database (see below).
 

#### Create the destination tables in SQL Server

You should review the table definitions in R, and use them to write `CREATE TABLE` SQL statements to establish the structure of the tables (names and data types of the columns) where the data will land in SQL Server.  Once you are confident that you have the individual tables laid out correctly, spend some time thinking about which columns in each table represent primary and foreign keys.

#### Import the data from exported files into SQL Server

Once you've created the tables in SQL Server, you are ready to `BULK INSERT` the exported data into the database tables.  [See here for documentation](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-bulk-data-by-using-bulk-insert-or-openrowset-bulk-sql-server?view=sql-server-ver16)
 
Pay particular attention to:
* File system locations of the bind mount volumes where you are exposing the exported files to the SQL Server container
* How you've delimited (both rows and columns) the exported data, and how you are asking `BULK INSERT` to read it
* How you've quoted the strings in the data on export, and how you are asking `BULK INSERT` to read it
* Whether or not you asked R to export column names, and whether you are asking `BULK INSERT` to expect them in the file
 
#### Sanity Check

Take a look at the data in the original R tibbles and your SQL Server version... does it look right?

### Tasks

Once you have successfully loaded the data tables into SQL Server, you will need to perform a number of `JOIN` and `GROUP` BY aggregate queries to answer the following questions.  The queries to answer these questions can all be written as "one-liners", or you can make use of [temporary tables in TempDB](https://www.sqlservertutorial.net/sql-server-basics/sql-server-temporary-tables/) to store intermediate results.  Sometimes, using temporary tables allows you the opportunity to incrementally solve a problem and sanity-check the results along the way.
 
Along with temporary tables, it is often useful to [alias table names](https://en.wikipedia.org/wiki/Alias_(SQL)) when writing anything more complicated than `SELECT *...`
 
#### Questions

<ol> 
<li>Which plane (tail number) logged the most flights?</li>
<li>Which plane (tail number) logged the most miles?</li>
<li>Which airline experienced the highest average temperature at departure time of its respective flights?</li>
</ol>

(TODO: add our sample code for our solution to the assignment)

## Assignment 3 <a name="assignment3"></a>

Note: This section is adapted from the assignments provided to us by the Harvard CCB liaison team.

### Description

Recreate a part of the SummarizedExperiment paradigm for storing and representing gene expression data in a relational database setting by linking two data tables (expression data and cell metadata).

### Tasks
 
Obtain the segmented expression data from the [MERFISH mouse hypothalamus dataset from DataDryad](https://doi.org/10.5061/dryad.8t8s248). Divide the obtained csv file into 1) columns storing expression levels of individual genes, and 2) cell metadata such as animal ID, animal sex, and cell class. Create a SQL table for both data components, with the two tables being linked by the cell ID.
Perform a number of select queries to obtain eg. 
a) all cells of a certain cell type, 
b) all cells of female mice, and 
c) all pericytes with non-zero expression of the Ace2 gene.

### Installing

The segmented expression data can be downloaded from [datadryad](https://doi.org/10.5061/dryad.8t8s248).

### Executing program

(TODO: add our sample execution code)

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Assignment 4 <a name="assignment4"></a>

### Background

Here we will be analyzing [NOAA's Integrated Surface Database]
(https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database).
 
The Integrated Surface Database (often abbreviated to ISD) is a large collection of hourly and sub-hourly weather observations collected from around the world. The result is a large database of weather information in a consistent, text-based format. There are multiple ISD datasets available spawithin the ISD product set.

For the purposes of this exercise we will be focusing on the Global Daily Summary data, for the United States only. Daily summaries consist of daily averages computed from ISD data. Daily weather elements include mean values of temperature, dew point temperature, sea level pressure, station pressure, visibility, precipitation, and wind

### Setup

Clone the ISD_HMC repo to your Desktop.
Follow the instructions in the README.md file to download and set up the ISD database
Clone the tiger2sql repo to your Desktop
Use the following instructions to add the tiger shapefiles to your existing database. DO NOT follow the instructions in the README.md file for setting up the tigerfiles. Since we want the tiger data to load through the same SQL server instance.
Navigate into the tiger2sql directory, checkout the `tiger_hmc` branch NOT main!
```
git checkout tiger_hmc​
docker \
run \
--rm \
--name tiger-hmc \
-v ~/dev/tiger2sql:/HostData \
-i -t hmsccb/tiger-hmc:latest
```
An interactive shell will open, paste in the following python call to run the code​
```
python3 -u < HostData/tiger2sql.py - --year "2020" --uid "sa" --pwd "Str0ngp@ssworD" --ipaddress "172.17.0.2" --zcta
```
***NOTE*** the only value you may need to change in the above command is the ip address, which you can find by typing `docker network inspect bridge` and finding the ip address in the highlighted area below.​

(TODO: insert image)
​
 ​
Open Azure Data Studio (if using)
Connect to the database using the login uid and pwd you created the SQL Server container with:
​
(TODO: insert image)
​
Congratulations! You're now set up to query the database.
 
### Data

#### ISD_Spatial Table Column Definitions

**STATION:** Station number (WMO/DATSAV3 number) for the location.

**DATE:** Given in mm/dd/yyyy format

**LATITUDE:** Given in decimated degrees (Southern Hemisphere values are negative)

**LONGITUDE:** Given in decimated degrees (Western Hemisphere values are negative)

**ELEVATION:** Given in meters

**NAME:** Station Name (plain text)

**TEMP:** Mean temperature for the day in degrees Fahrenheit to tenths.  Missing = 9999.9

**DEWP:** Mean dew point for the day in degrees Fahrenheit to tenths.  Missing = 9999.9

**SLP:** Mean sea level pressure for the day in millibars to tenths.  Missing = 9999.9

**STP:** Mean station pressure for the day in millibars to tenths.  Missing = 9999.9

**VISIB:** Mean visibility for the day in miles to tenths.  Missing = 999.9

**WDSP:** Mean wind speed for the day in knots to tenths.  Missing = 999.9

**PRCP:** Total precipitation (rain and/or melted snow) reported during the day in inches and hundredths; “0” indicates no measurable precipitation (includes a trace). Missing = 99.99

**GeographyLocationIsd:** A spatial index
 
**Source:**

https://www.ncei.noaa.gov/data/global-summary-of-the-day/doc/

#### TIGERFiles Database Structure

**dbo.geometry_columns:** A helper table to define the geometry columns. 

**dbo.spatial_ref_sys:** A helper table to define the spatial reference system.

**dbo.tl_2020_us_zcta:** TIGER shapefile data table, columns are defined below

#### ZCTA Column Definitions

**ogr_fid**: ​A unique ID for each row​
**GeographyLocation**: ​A geography-type column created from the latitude and longitude values (intptlat10 and intptlon10, respectively). You can think of this value asa code representing a POLYGON which covers a bounding region around the zipcode.​
**zcta5ce20**: ​Zip code tabulated area (5 digit) for Census 2020​
**geoid20**: ​Census block identifier, a concatenation of 2020​ Census state FIPS code, 2020​ Census county FIPS code, 2020​ Census tract code, and 2020​ Census block number​
**classfp20**: ​2020​ Census FIPS ƒ55 class code​
**mtfcc20**: ​MAF/TIGER feature class code (G6350)​
**funcstat20**: ​2020​ Census functional status​
**aland20**: ​2020​ Census land area​
**awater20**: ​2020​ Census water area​
**intptlat20**: ​2020​ Census latitude of the internal point of the zipcode​
**intptlon20**: ​2020​ Census longitude of the internal point of the zipcode​​
 
**Sources and further reading:**
* https://www2.census.gov/geo/pdfs/maps-data/data/tiger/tgrshp2020/TGRSHP2020_TechDoc.pdf

* https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html


### Exercises

(TODO: Create a Notebook for Assignment 3 and reference it here)

#### Background

The ISD_Spatial Table contains weather data, and the latitude and longitude values of the station where that data was collected. The TIGER table contains geographical information like latitudes and longitudes, zipcodes, and a polygon feature which serves as a bounding region around the zipcode. To identify the zipcode of a specific weather station, you'll need to complete a JOIN to find the GeographyLocation (a POLYGON type) which contains the Geographical point representation of Latitude/Longitude (POINT type) for the station you're looking up information for.  Hint: review the documentation for Geography data type operations https://learn.microsoft.com/en-us/sql/t-sql/spatial-geography/ogc-methods-on-geography-instances?view=sql-server-ver16

 

#### Instructions

Complete the following querying exercises, noting the time it takes for each query. If you are executing your queries via Python, you can use the time library to time your queries. If you are using Azure Data Studio, a timer is present in the base toolbar.

​
None of the following queries should take longer than a minute to execute once written, thanks to the use of spatial indexes. Recall that a spatial index differs from an ordinary index in that spatial objects are not 1D data points, instead they are in a higher dimensional space (e.g. 2D) and thus ordinary indexes are not appropriate for indexing such data. By creating a spatial index in these tables (this has already been completed for you) the spatial operations complete in seconds, as opposed to minutes. Sam's Note: I ran these queries with and without using ​spatial indexe​s. Without the indexes, even the simplest operation took 17+ minutes on average. With the index, it took less than a second.​
 
#### Tasks

1. Write a query to combine the ISD_Spatial table with the TIGER table (hint: Read the above paragraph, the goal is to combine the tables such that the Polygon from the zcta table Contains the Point represented in the ISD data)

 

2. Find the average annual temperature in Boston.

 

3. Find the top 5 windiest station in Massachusetts.

 

4. Where is the rainiest station in Washington State located?
 
 
5. How many weather stations are there per state? Which state has the most weather stations? The least? 
 
 
6. Get the Latitude and Longitude values for a station of your choosing
 
 
7. Calculate the distance between the latitude and longitude values you chose in Q6 and every station in the surrounding state, in both miles and meters
 

Free Answer:

1. How did you verify your answers to the above questions?

 

2. Are there any data quality issues with the tables that you accounted for in your queries?


## Assignment 5 <a name="assignment5"></a>

### Description

Note: This section is adapted from the assignments provided to us by the Harvard CCB liaison team.

Spatial transcriptomics protocols based on in situ sequencing or multiplexed RNA fluorescent hybridization can reveal detailed tissue organization. However, distinguishing the boundaries of individual cells in such data is challenging. Current segmentation methods typically approximate cell positions using nuclei stains.

[Petukhov et al., 2021](https://doi.org/10.1038/s41587-021-01044-w), describe [Baysor](https://github.com/kharchenkolab/Baysor), a segmentation method, which optimizes 2D or 3D cell boundaries considering joint likelihood of transcriptional composition and cell morphology. Baysor can also perform segmentation based on the detected transcripts alone.
Petukhov et al. compare the results of Baysor segmentation (mRNA-only) to the results of a deep learning-based segmentation method called [Cellpose](https://github.com/MouseLand/cellpose) from [Stringer et al., 2021](https://doi.org/10.1038/s41592-020-01018-x). Cellpose applies a machine learning framework for the segmentation of cell bodies, membranes and nuclei from microscopy images.
Petukhov et al. apply Baysor and Cellpose to MERFISH data from cryosections of mouse ileum (‘ileum’ is the final and longest segment of the small intestine). The MERFISH encoding probe library was designed to target 241 genes, including previously defined markers for the majority of gut cell types.

Samples in this dataset were stained with anti-Na+/K+-ATPase primary antibodies, oligo-labeled secondary antibodies and DAPI. MERFISH measurements across multiple fields of view and nine z planes were performed to provide a volumetric reconstruction of the distribution of the targeted mRNAs, the cell boundaries marked by Na+/K+-ATPase IF and cell nuclei stained with DAPI.

### Anatomy of the MERFISH mouse ileum dataset
<ul>
<li> Raw data </li>  
<ul>
<li> mRNA molecule data: 820k observations for 241 genes  </li>
<li> Image data: stitched 9-frame z-stacks (DAPI / Membrane, 500 MB) </li>
</ul>

<li> Processed data </li>
<ul>
<li> 3 different segmentations (Baysor, Cellpose, Baysor/Cellpose) </li>
<li> Cell clusters based on expression similarity  </li>
<li> Cell type labels based on marker gene expression in the clusters </li>
</ul>
</ul>

### Installation

The dataset can be obtained from the official [datadryad data publication](https://doi.org/10.5061/dryad.jm63xsjb2).

### Scripts

Here follows a list of the source code we've included for this assignment.

* [find_invalid_cells.py](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_5/src/find_invalid_cells.py) - 
Python script for identifying cells whose polygon representation is not a simple polygon

* [get_baysor_polygons.py](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_5/src/get_baysor_polygons.py) - 
Python script for parsing the given Baysor cell segmentation data JSON into a CSV

* [importCellPolygons.sql](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_5/src/importCellPolygons.sql) - 
SQL script for importing the cell polygons CSV (generated by `get_baysor_polygons.py`) into a SQL database 

* [importCells.sql](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_5/src/importCells.sql) - 
Deprecated

* [importMolecules.sql](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_5/src/importMolecules.sql) - 
SQL script for importing the `molecules.csv` raw data into a SQL database

* [pivot.py](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_5/src/pivot.py) - 
Python script for ‘pivoting’ the gene expression table into a gene expression matrix

* [polygonProcessing.sql](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_5/src/polygonProcessing.sql) - 
Deprecated

* [processCellPolygons.sql](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_5/src/processCellPolygons.sql) - 
SQL script for parsing the imported CellPolygons table (with polygons represented as strings) and creating a geometry type polygon column

* [processMoleculesPoints.sql](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_5/src/processMoleculesPoints.sql) -
SQL script for parsing the imported Molecules table (with points represented as strings) and creating a geometry type point column

* [visualize_cells.py](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_5/src/visualize_cells.py)
Python script that uses `poly_per_z.json` to draw plots of cell polygons from the Baysor segmentation


### Tasks 

Note: This section is adapted from the assignments provided to us by the Harvard CCB liaison team.

1. Obtain the dataset from [datadryad](https://doi.org/10.5061/dryad.jm63xsjb2) and inspect the contents of the data release. Use the contained README for an orientation. There are two relevant parts here for us in the beginning: 1) the molecule data table in raw_data /molecules.csv, and 2) the cell polygon coordinates from the Baysor segmentation in `data_analysis/baysor/segmentation/poly_per_z.json`.

2. Create an SQL table for both data components, i.e. 1) one table representing the molecules as spatial points given their x, y, and z-coordinates (using the pixel coordinates), and 2) one table representing the cells as polygons. It is a good exercise to create the cell polygon table directly from the json format. Alternatively, the cell polygon coordinates in a flattened 2D table format can be obtained from [dropbox](https://www.dropbox.com/s/n6rf3sastdo9fn5/baysor_polygons.csv?dl=0). 

3. Perform spatial overlap queries between the molecule table and the cell polygon table to create a new SQL table. The resulting table should contain three columns (gene, cell, molecule count) and store for each gene the number of molecules overlapping with each cell. Also record the execution time of your queries to produce this molecule count table (best to calculate average execution time from performing queries repeatedly).

4. Reshape the molecule count table to a two-dimensional expression matrix (gene x cell). The resulting expression matrix should store for each gene the number of molecules overlapping with each cell. This will involve a pivot operation in the database and can alternatively also be performed in R/Python based on the molecule count table produced in 3.

5. We proceed by inspecting the molecule to cell assignment for the Baysor segmentation in data_analysis/baysor/segmentation/segmentation.csv. One issue with the polygon coordinates in the json file is that there is no 1:1 mapping between these polygons and the cell metadata. We therefore aim to reconstruct the cell boundaries by computing [convex hulls](https://learn.microsoft.com/en-us/sql/t-sql/spatial-geometry/stconvexhull-geometry-data-type?view=sql-server-ver16) around all molecules assigned to a cell. As before: record the average execution time of your queries to produce a table of convex hull geometries for each of the 5800 cells in the segmentation csv file. 

### Execution

To run our code for this assignment, follow along in our [Notebook](https://github.com/kunyanglu/harvard-ccb-hmc-clinic/blob/main/assignment_5/Notebooks/Assignment5NotebookSummarized.ipynb)

(TODO: add details with how to run using scripts)

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

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
