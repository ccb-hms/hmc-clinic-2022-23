# Assignment 4 <a name="assignment4"></a>
Note: This section is adapted from the assignments provided to us by the Harvard CCB liaison team.

## Contents

<ol>
<li><a href="#background">Background</a></li>
<li><a href="#setup">Setup</a></li>
<li><a href="#data">Data</a></li>
<li><a href="#exercises">Exercises</a></li>
<li><a href="work">Our work</a></li>
</ol>
  
## Background <a name="background"></a>

Here we will be analyzing [NOAA's Integrated Surface Database](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database).
 
The Integrated Surface Database (often abbreviated to ISD) is a large collection of hourly and sub-hourly weather observations collected from around the world. The result is a large database of weather information in a consistent, text-based format. There are multiple ISD datasets available spawithin the ISD product set.

For the purposes of this exercise we will be focusing on the Global Daily Summary data, for the United States only. Daily summaries consist of daily averages computed from ISD data. Daily weather elements include mean values of temperature, dew point temperature, sea level pressure, station pressure, visibility, precipitation, and wind

## Setup <a name="setup"></a>

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
 
## Data <a name="data"></a>

### ISD_Spatial Table Column Definitions

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

### TIGERFiles Database Structure

**dbo.geometry_columns:** A helper table to define the geometry columns. 

**dbo.spatial_ref_sys:** A helper table to define the spatial reference system.

**dbo.tl_2020_us_zcta:** TIGER shapefile data table, columns are defined below

### ZCTA Column Definitions

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


## Exercises <a name="exercises"></a>

(TODO: Create a Notebook for Assignment 3 and reference it here)

### Background

The ISD_Spatial Table contains weather data, and the latitude and longitude values of the station where that data was collected. The TIGER table contains geographical information like latitudes and longitudes, zipcodes, and a polygon feature which serves as a bounding region around the zipcode. To identify the zipcode of a specific weather station, you'll need to complete a JOIN to find the GeographyLocation (a POLYGON type) which contains the Geographical point representation of Latitude/Longitude (POINT type) for the station you're looking up information for.  Hint: review the documentation for Geography data type operations https://learn.microsoft.com/en-us/sql/t-sql/spatial-geography/ogc-methods-on-geography-instances?view=sql-server-ver16

 

### Instructions

Complete the following querying exercises, noting the time it takes for each query. If you are executing your queries via Python, you can use the time library to time your queries. If you are using Azure Data Studio, a timer is present in the base toolbar.

​
None of the following queries should take longer than a minute to execute once written, thanks to the use of spatial indexes. Recall that a spatial index differs from an ordinary index in that spatial objects are not 1D data points, instead they are in a higher dimensional space (e.g. 2D) and thus ordinary indexes are not appropriate for indexing such data. By creating a spatial index in these tables (this has already been completed for you) the spatial operations complete in seconds, as opposed to minutes. Sam's Note: I ran these queries with and without using ​spatial indexe​s. Without the indexes, even the simplest operation took 17+ minutes on average. With the index, it took less than a second.​
 
### Tasks

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

## Our work <a name="work"></a>

Our writeup began its life as a Google Doc, so we've included a pdf of that, as it includes images that might be useful. We've also translated this work into a SQL notebook for your convenience!