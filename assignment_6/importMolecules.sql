USE MouseHypothalamus;

-- Set up the table column types for bulk import
DROP TABLE IF EXISTS #TempMolecules;
CREATE TABLE #TempMolecules(
    Gene_name NVARCHAR(10) NOT NULL,
    Cell_name NVARCHAR(40),
    Animal_ID int,
    Bregma float,
    Animal_sex nvarchar(6) NOT NULL,
    Behavior nvarchar(10),
    Centroid_X float NOT NULL,
    Centroid_Y float NOT NULL,
    Centroid_Z float NOT NULL,
    Total_brightness float,
    Area int,
    Error_bit tinyint,
    Error_direction tinyint
);

-- Do the bulk import from CSV
BULK INSERT #TempMolecules FROM '/var/data/merfish_barcodes.csv'
WITH ( 
    FIRSTROW = 2, -- skip the column headers
    ROWS_PER_BATCH = 467052741, -- however many total rows the data has
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '0x0a',
    KEEPNULLS
);

-- we haven't tested this yet
-- This should create the actual table, with a proper identity column
SELECT IDENTITY(int,1,1) as id,* INTO Molecules FROM #TempMolecules;
ALTER TABLE Molecules
    ADD CONSTRAINT id_PK PRIMARY KEY (id)