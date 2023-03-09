USE MouseIleum;
DROP TABLE IF EXISTS MoleculesAndCellsWithGeometries;
CREATE TABLE MoleculesAndCellsWithGeometries (
    molecule_id int NOT NULL,
    gene NVARCHAR(8),
    xy_point geometry,
    z_layer tinyint not null,
    cell_id smallINT not null,
    cell_polygon geometry
)

DECLARE @z tinyint;
SET @z = 1;

WHILE @z <= 9
    BEGIN
        DECLARE @startTime DATETIME
        declare @endTime DATETIME
        Set @starttime = getdate()
        INSERT INTO MoleculesAndCellsWithGeometries
            SELECT mol.molecule_id, mol.gene, mol.point, @z as z_layer, poly.cell as cell_id, poly.polygon as cell_polygon FROM (
                SELECT * FROM [MouseIleum].[dbo].[MoleculesWithPoints] 
                    WHERE z_layer=@z ) as mol
                INNER JOIN (   
                    SELECT * FROM [MouseIleum].[dbo].[CellPolygons] 
                    WHERE z=@z ) as poly
                ON poly.polygon.STIntersects(mol.point) = 1 -- =1 is needed bc output is 0 or 1 instead of T/F

        Set @endTime = GETDATE()
        SELECT @EndTime - @StartTime;
        SET @z = @z + 1;
    END