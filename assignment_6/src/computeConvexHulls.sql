Use MouseHypothalamus;

DROP TABLE IF EXISTS ConvexHullsAnimal1Bregma1Z0;
CREATE TABLE ConvexHullsAnimal1Bregma1Z0 (
    cell_id int,
    animal_id int,
    bregma float,
    z_layer float,
    hull geometry
)
SET NOCOUNT ON;
-- Loop through the animals
DECLARE @a INTEGER;
-- SET @a = 1;
-- WHILE @a <= 36
SET @a = 4;
-- BEGIN
--     -- Loop through the bregma points
    DECLARE @b FLOAT;
    -- SET @b = -0.29;
--     WHILE @b <= 0.26
    SET @b = -0.14;
--     BEGIN
--         -- Loop through the z layers
        DECLARE @z FLOAT;
        SET @z = 0;
--         WHILE @z <=9
--         BEGIN
            -- Loop through the cell ids (yes, this does needlessly check ids that may not exist)
            DECLARE @c INTEGER;
            SET @c = 1;
            -- WHILE @c <= 1123833
            WHILE @c <= 1037
            BEGIN
                DROP TABLE IF EXISTS #CellPoints;
                SELECT xy_point, cell_name
                    INTO #CellPoints
                    FROM MoleculesWithPointsWithCellIdsHead
                    WHERE feature_id = @c AND centroid_z = @z AND animal_id = @a AND bregma = @b;
                IF EXISTS(SELECT 1 FROM #CellPoints) -- check if there are any points to make a convex hull out of
                    BEGIN 
                    INSERT INTO ConvexHullsAnimal1Bregma1Z0
                        SELECT @c as cell_id, @a as animal_id, @b as bregma, @z as z_layer, geometry::ConvexHullAggregate(xy_point) as hull from #CellPoints;
                    END;
            SET @c = @c + 1;
            END;
--         SET @z = @z + 1.5;
--         END;
--     SET @b = @b + 0.05;
--     END;
-- SET @a = @a + 1;
-- END;





-- DROP TABLE IF EXISTS #CellPoints
-- SELECT point as xy_point, m.Cell_name as Cell_name
--     INTO #CellPoints
--     FROM MoleculesWithPoints as m 
--     INNER JOIN [master].[dbo].[CellNames] as n 
--     ON m.Cell_name = n.cell_name
--     WHERE m.centroid_z = 3 AND m.animal_id = 1 AND m.bregma = 0.26 AND n.cell_id = 422024;
-- INSERT INTO ConvexHulls
--     SELECT 422024 as cell_id, 1 as animal_id, 0.26 as bregma, 3 as z_layer, geometry::ConvexHullAggregate(xy_point) as hull from #CellPoints


-- DROP TABLE IF EXISTS #CellPoints
-- SELECT point as xy_point
--     INTO #CellPoints
--     FROM MoleculesWithPoints
--     WHERE centroid_z = 3 AND cell_name = '6813aa30-d82c-4580-8d83-24d88dc47045' AND animal_id = 1 AND bregma = 0.21
-- INSERT INTO ConvexHulls
--     SELECT '6813aa30-d82c-4580-8d83-24d88dc47045' as cell_name, 1 as animal_id, 0.21 as bregma, 3 as z_layer, geometry::ConvexHullAggregate(xy_point) as hull from #CellPoints
