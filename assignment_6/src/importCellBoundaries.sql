USE MouseHypothalamus;

-- Set up the table column types for bulk import
DROP TABLE IF EXISTS #TempCellBoundaries;

-- import for the original columns in csv
-- CREATE TABLE #TempCellBoundaries(
--     feature_uID NVARCHAR(40),
--     feature_ID int,
--     fovID int,
--     is_broken int,
--     num_joined_features int,
--     abs_volume float,
--     abs_x_boundary_1 NVARCHAR(MAX),
--     abs_y_boundary_1 NVARCHAR(MAX),
--     abs_x_boundary_2 NVARCHAR(MAX),
--     abs_y_boundary_2 NVARCHAR(MAX),
--     abs_x_boundary_3 NVARCHAR(MAX),
--     abs_y_boundary_3 NVARCHAR(MAX),
--     abs_x_boundary_4 NVARCHAR(MAX),
--     abs_y_boundary_4 NVARCHAR(MAX),
--     abs_x_boundary_5 NVARCHAR(MAX),
--     abs_y_boundary_5 NVARCHAR(MAX),
--     abs_x_boundary_6 NVARCHAR(MAX),
--     abs_y_boundary_6 NVARCHAR(MAX),
--     abs_x_boundary_7 NVARCHAR(MAX),
--     abs_y_boundary_7 NVARCHAR(MAX)
-- );

-- import for the preprocessed csv
CREATE TABLE #TempCellBoundaries(
    layer tinyint,
    feature_uid NVARCHAR(40), 
    feature_id int,
    geometry_string NVARCHAR(MAX)
)

-- Do the bulk import from CSV
-- BULK INSERT #TempCellBoundaries FROM '/var/data/cell_boundaries_reformatted.csv'
BULK INSERT #TempCellBoundaries FROM '/var/data/cell_boundaries_reformatted.csv' -- first 1000 rows of reformatted data
-- BULK INSERT #TempCellBoundaries FROM '/var/data/high_resolution_cell_boundaries.csv' -- original data
-- BULK INSERT #TempCellBoundaries FROM '/var/data/high_resolution_cell_boundaries_head.csv' -- first 1000 rows of original data
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

-- DROP TABLE IF EXISTS CellBoundariesWithGeometryStrings;
-- SELECT IDENTITY(int,1,1) as id,* INTO CellBoundariesWithGeometryStrings FROM #TempCellBoundaries;
-- ALTER TABLE CellBoundariesWithGeometryStrings
--     ADD CONSTRAINT CellBoundariesWithGeometryStrings_id_PK PRIMARY KEY (id);