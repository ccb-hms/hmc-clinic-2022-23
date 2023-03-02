USE MouseIleum;

DROP TABLE IF EXISTS SegmentationWithPoints;
SELECT mol_id, gene, x as x_pixel, y as y_pixel, z as z_pixel, id, cell as cell_id, assignment_confidence, is_noise INTO SegmentationWithPoints FROM Segmentation;

ALTER TABLE SegmentationWithPoints
    ADD z_layer tinyint,
        xy_point geometry;

UPDATE SegmentationWithPoints
    SET z_layer = CAST(ROUND(z_pixel /13.76819064, 0) AS int) + 1;

UPDATE SegmentationWithPoints
    SET xy_point = geometry::STGeomFromText('POINT(' + CONVERT(VARCHAR(5), x_pixel) + ' ' + CONVERT(VARCHAR(5), y_pixel) + ')', 0)

ALTER TABLE SegmentationWithPoints
    DROP COLUMN z_pixel;