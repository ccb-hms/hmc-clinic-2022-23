-- just import the data as one giant column
SELECT @json = BulkColumn
  FROM OPENROWSET (BULK '/Users/clinic2022/Desktop/Assignment5/data_release_baysor_merfish_gut/data_analysis/baysor/segmentation/poly_per_z.json', SINGLE_CLOB) as j

CREATE DATABASE MouseIleum
USE DATABASE MouseIleum

-- get appropriate columns from this
select z_id as z, g.id as cell, c.x, c.y
from @json
CROSS APPLY OPENJSON(BulkColumn)
WITH(
    z_id small int, 
    geometries NVARCHAR(MAX) AS JSON,
    type nvarchar(18)
  ) as poly
 CROSS apply OPENJSON(poly.geometries) 
 WITH (
    coordinates nvarchar(MAX) AS JSON,
    type varchar(7) 
  ) as g
  CROSS APPLY OPENJSON(coordinates)
  WITH (
    x int,
    y int
  ) as c

-- TODO then save as a file 