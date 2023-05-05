DROP TABLE IF EXISTS ConvexHullsAll
CREATE TABLE ConvexHullsAll(
    cell_id int,
    z_layer tinyint,
    hull geometry
    );

DECLARE @maxId INTEGER;
SET @maxId = 5800; -- This is the maximum cell ID found across any layer; some layers have fewer than 5800 resulting in null entries

SET NOCOUNT ON;
-- Outer loop: Loop through z layers
DECLARE @z INTEGER;
SET @z = 1;
WHILE @z <= 9
    BEGIN
        -- Inner loop: Loop through cells
        DECLARE @id INTEGER;
        SET @id = 1;
        WHILE @id <= @maxId
            BEGIN
                -- Creating a table of cell in z-layer 
                DROP TABLE IF EXISTS #SegmentationCell;
                SELECT xy_point 
                    INTO #SegmentationCell
                    FROM SegmentationWithPoints
                    WHERE z_layer= @z AND cell_id= @id;
                -- Computing the convex hull around the molecules within that cell
                INSERT INTO ConvexHullsAll
                    SELECT @id AS cell_id, @z as z_layer, geometry::ConvexHullAggregate(xy_point) AS hull FROM #SegmentationCell;
                SET @id = @id + 1;
            END;
    END;
SET NOCOUNT OFF;