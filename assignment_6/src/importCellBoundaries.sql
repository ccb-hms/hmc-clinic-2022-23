USE MouseHypothalamus;

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
BULK INSERT #TempCellBoundaries FROM '/var/data/cell_boundaries_reformatted.csv' -- first 1000 rows of reformatted data
WITH ( 
    FIRSTROW = 2, -- skip the column headers
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '0x0a',
    KEEPNULLS
);

-- Create the actual table, with a proper identity column

DROP TABLE IF EXISTS CellBoundariesWithGeometryStrings;
SELECT IDENTITY(int,1,1) as id,* INTO CellBoundariesWithGeometryStrings FROM #TempCellBoundaries;
ALTER TABLE CellBoundariesWithGeometryStrings
    ADD CONSTRAINT CellBoundariesWithGeometryStrings_id_PK PRIMARY KEY (id);