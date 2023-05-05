Use MouseHypothalamus;

DROP TABLE IF EXISTS ConvexHullsAnimal4BregmaM14Z0;
CREATE TABLE ConvexHullsAnimal4BregmaM14Z0 (
    cell_id int,
    animal_id int,
    bregma float,
    z_layer float,
    hull geometry
)
SET NOCOUNT ON;
-- Loop through the animals
DECLARE @a INTEGER;
SET @a = 4;
    DECLARE @b FLOAT;
    SET @b = -0.14;
        DECLARE @z FLOAT;
        SET @z = 0;
            -- Loop through the cell ids (yes, this does needlessly check ids that may not exist)
            DECLARE @c INTEGER;
            SET @c = 1;
            WHILE @c <= 6048
            BEGIN
                DROP TABLE IF EXISTS #CellPoints;
                SELECT xy_point, cell_name
                    INTO #CellPoints
                    FROM MoleculesWithPointsWithCellIds
                    WHERE feature_id = @c AND centroid_z = @z AND animal_id = @a AND bregma = @b;
                IF EXISTS(SELECT 1 FROM #CellPoints) -- check if there are any points to make a convex hull out of
                    BEGIN 
                    INSERT INTO ConvexHullsAnimal4BregmaM14Z0
                        SELECT @c as cell_id, @a as animal_id, @b as bregma, @z as z_layer, geometry::ConvexHullAggregate(xy_point) as hull from #CellPoints;
                    END;
            SET @c = @c + 1;
            END;