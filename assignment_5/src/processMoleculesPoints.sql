USE MouseIleum;

DROP TABLE IF EXISTS MoleculesWithPoints;
SELECT molecule_id, gene, x_pixel, y_pixel, z_pixel INTO MoleculesWithPoints FROM Molecules;

ALTER TABLE MoleculesWithPoints
    ADD z_layer tinyint,
        point geometry;

UPDATE MoleculesWithPoints
    SET z_layer = CAST(ROUND(z_pixel /13.76819064, 0) AS int) + 1;

UPDATE MoleculesWithPoints
    SET point = geometry::STGeomFromText('POINT(' + CONVERT(VARCHAR(5), x_pixel) + ' ' + CONVERT(VARCHAR(5), y_pixel) + ')', 0)