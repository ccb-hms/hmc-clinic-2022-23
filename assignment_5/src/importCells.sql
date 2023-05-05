-- just import the data as one giant column
DECLARE @json VARCHAR(MAX)

SELECT @json = BulkColumn
  FROM OPENROWSET (BULK '/var/data/data_analysis/baysor/segmentation/poly_per_z.json', SINGLE_CLOB) as j

-- get appropriate columns from this
SELECT z_id as z, g.id as cell, c.x, c.y FROM OPENJSON(@json)
CROSS APPLY OPENJSON(@json)
WITH(
    z_id smallint, 
    geometries NVARCHAR(MAX) AS JSON,
    type nvarchar(18)
  ) as poly
 CROSS apply OPENJSON(poly.geometries) 
 WITH (
    coordinates nvarchar(MAX) AS JSON,
    type varchar(9)
    -- id int NOT NULL
  ) as g
  CROSS APPLY OPENJSON(g.coordinates)
  WITH (
    x int,
    y int
  ) as c

SELECT * FROM OPENJSON (@JSON)
WITH (
    z_id smallint, 
    geometries NVARCHAR(MAX) AS JSON,
    type nvarchar(18)) as poly;

USE MouseIleum
CREATE TABLE [dbo].[Cells](
  z TINYINT,
  cell SMALLINT,
  x SMALLINT,
  y SMALLINT
);

BULK INSERT Cells FROM '/var/data/baysor_polygons.csv' WITH (FIRSTROW = 2, FIELDTERMINATOR = ',');