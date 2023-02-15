USE MouseIleum;

DROP TABLE IF EXISTS CellPolygons;
CREATE TABLE CellPolygons (
    id int, 
    z tinyint,
    cell smallint,
    polygon_string NVARCHAR(MAX),
);

BULK INSERT CellPolygons FROM '/var/data/processed_data/baysor_SQL_polygons.csv' WITH ( FIRSTROW = 2, FIELDTERMINATOR = ',');

UPDATE [dbo].[CellPolygons]
    SET polygon_string = SUBSTRING(polygon_string, 2, LEN(polygon_string))
    WHERE LEFT(polygon_string,1) = '"';
UPDATE [dbo].[CellPolygons]
    SET polygon_string = SUBSTRING(polygon_string, 1, LEN(polygon_string)-2);
    -- WHERE RIGHT(polygon_string,2) = '" ';  -- for some reason this wasn't working as expected