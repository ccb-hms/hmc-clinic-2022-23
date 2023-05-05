USE MouseHypothalamus;

--------------Molecules--------------

DROP TABLE IF EXISTS #TempMolecules;
CREATE TABLE #TempMolecules(
    Gene_name NVARCHAR(10) NOT NULL,
    Cell_name NVARCHAR(40),
    Animal_ID int,
    Bregma float,
    Animal_sex nvarchar(6) NOT NULL,
    Behavior nvarchar(20),
    Centroid_X float NOT NULL,
    Centroid_Y float NOT NULL,
    Centroid_Z float NOT NULL,
    Total_brightness float,
    Area int,
    Error_bit tinyint,
    Error_direction tinyint
);

BULK INSERT #TempMolecules FROM '/var/data/merfish_barcodes.csv'
WITH ( 
    FIRSTROW = 2, -- skip the column headers
    --ROWS_PER_BATCH = 467052741, -- however many total rows the data has
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '0x0a',
    KEEPNULLS
);

SELECT IDENTITY(int,1,1) as id,* INTO Molecules FROM #TempMolecules;
ALTER TABLE Molecules
    ADD CONSTRAINT Molecules_id_PK PRIMARY KEY (id)

--------------Cell Boundaries--------------

-- Set up the table column types for bulk import
DROP TABLE IF EXISTS #TempCellBoundaries;

-- import for the preprocessed csv
CREATE TABLE #TempCellBoundaries(
    layer tinyint,
    feature_uid NVARCHAR(40), 
    feature_id int,
    geometry_string NVARCHAR(MAX)
)

-- Do the bulk import from CSV
BULK INSERT #TempCellBoundaries FROM '/var/data/cell_boundaries_reformatted.csv'
WITH ( 
    FIRSTROW = 2, -- skip the column headers
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '0x0a',
    KEEPNULLS
);

-- Create the actual table, with a proper identity column
DROP TABLE IF EXISTS CellBoundaries;
SELECT IDENTITY(int,1,1) as id,* INTO CellBoundaries FROM #TempCellBoundaries;
ALTER TABLE CellBoundaries
    ADD CONSTRAINT CellBoundaries_id_PK PRIMARY KEY (id)