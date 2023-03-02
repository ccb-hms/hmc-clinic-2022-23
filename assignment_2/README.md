# Assignment 2 <a name="assignment2"></a>

Note: This section is adapted from the assignments provided to us by the Harvard CCB liaison team.

## Contents

<ol>
<li>Introduction</li>
<li>Guidance</li>
<li>Tasks</li>
</ol>

## Introduction

We will be working with the nycflights13 data set [described in Chapter 13 of R for Data Science](https://r4ds.had.co.nz/relational-data.html#exercises-30).
 
If you wish to read through it, that chapter provides a nice overview of the semantics of working with relational data, along with a comprehensive treatment of the contemporary syntax for manipulating relational data natively in R data frames.  This reading is entirely optional, and provided as a point of reference, since we will make use of the example data set, but manipulate it in SQL Server instead of R data frames.
 
You will export the nycflights13 dataset from R and load it into SQL Server running in a container, where you will write SQL queries to answer a variety of questions about the flights, planes, etc.

## Guidance

### Export the data from R

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

### Make the exported files available to the SQL Server container

Once you have the five tables exported to delimited text files, you need to load them into SQL Server running in a container.  You should use the -v argument to the docker run invocation for the SQL Server container to bind mount the directory on your local file system that contains the text files into a file system location inside the container.  This will make them available for SQL Server to read when you are ready to load them into the database (see below).
 

### Create the destination tables in SQL Server

You should review the table definitions in R, and use them to write `CREATE TABLE` SQL statements to establish the structure of the tables (names and data types of the columns) where the data will land in SQL Server.  Once you are confident that you have the individual tables laid out correctly, spend some time thinking about which columns in each table represent primary and foreign keys.

### Import the data from exported files into SQL Server

Once you've created the tables in SQL Server, you are ready to `BULK INSERT` the exported data into the database tables.  [See here for documentation](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-bulk-data-by-using-bulk-insert-or-openrowset-bulk-sql-server?view=sql-server-ver16)
 
Pay particular attention to:
* File system locations of the bind mount volumes where you are exposing the exported files to the SQL Server container
* How you've delimited (both rows and columns) the exported data, and how you are asking `BULK INSERT` to read it
* How you've quoted the strings in the data on export, and how you are asking `BULK INSERT` to read it
* Whether or not you asked R to export column names, and whether you are asking `BULK INSERT` to expect them in the file
 
### Sanity Check

Take a look at the data in the original R tibbles and your SQL Server version... does it look right?

## Tasks

Once you have successfully loaded the data tables into SQL Server, you will need to perform a number of `JOIN` and `GROUP` BY aggregate queries to answer the following questions.  The queries to answer these questions can all be written as "one-liners", or you can make use of [temporary tables in TempDB](https://www.sqlservertutorial.net/sql-server-basics/sql-server-temporary-tables/) to store intermediate results.  Sometimes, using temporary tables allows you the opportunity to incrementally solve a problem and sanity-check the results along the way.
 
Along with temporary tables, it is often useful to [alias table names](https://en.wikipedia.org/wiki/Alias_(SQL)) when writing anything more complicated than `SELECT *...`
 
### Questions

<ol> 
<li>Which plane (tail number) logged the most flights?</li>
<li>Which plane (tail number) logged the most miles?</li>
<li>Which airline experienced the highest average temperature at departure time of its respective flights?</li>
</ol>

(TODO: add our sample code for our solution to the assignment)
