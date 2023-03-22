USE MouseHypothalamus;

-- Set up the table column types for bulk import
DROP TABLE IF EXISTS #TempCellBoundaries;
CREATE TABLE #TempCellBoundaries(
    feature_uID NVARCHAR(40),
    feature_ID int,
    fovID int,
    is_broken int,
    num_joined_features int,
    abs_volume float,
    abs_x_boundary_1 NVARCHAR(MAX),
    abs_y_boundary_1 NVARCHAR(MAX),
    abs_x_boundary_2 NVARCHAR(MAX),
    abs_y_boundary_2 NVARCHAR(MAX),
    abs_x_boundary_3 NVARCHAR(MAX),
    abs_y_boundary_3 NVARCHAR(MAX),
    abs_x_boundary_4 NVARCHAR(MAX),
    abs_y_boundary_4 NVARCHAR(MAX),
    abs_x_boundary_5 NVARCHAR(MAX),
    abs_y_boundary_5 NVARCHAR(MAX),
    abs_x_boundary_6 NVARCHAR(MAX),
    abs_y_boundary_6 NVARCHAR(MAX),
    abs_x_boundary_7 NVARCHAR(MAX),
    abs_y_boundary_7 NVARCHAR(MAX)
);

-- Do the bulk import from CSV
BULK INSERT #TempCellBoundaries FROM '/var/data/high_resolution_cell_boundaries.csv'
WITH ( 
    FIRSTROW = 2, -- skip the column headers
    ROWS_PER_BATCH = 1027849, -- however many total rows the data has
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '0x0a',
    KEEPNULLS
);

-- we haven't tested this yet
-- This should create the actual table, with a proper identity column
SELECT IDENTITY(int,1,1) as id,* INTO CellBoundaries FROM #TempCellBoundaries;
ALTER TABLE Molecules
    ADD CONSTRAINT id_PK PRIMARY KEY (id)