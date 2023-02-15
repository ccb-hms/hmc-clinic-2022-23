USE MouseIleum;

ALTER TABLE CellPolygons
ADD polygon geometry;

GO
UPDATE CellPolygons
    SET polygon = geometry::STGeomFromText(polygon_string, 0);

ALTER TABLE CellPolygons
    DROP COLUMN polygon_string;