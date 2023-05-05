
SELECT *
    INTO NewTable
    FROM [MouseIleum].[dbo].[Cells]
    WHERE z = 1 AND cell = 1

SELECT *
    INTO MoleculesLayer0
    FROM [MouseIleum].[dbo].[Molecules]
    WHERE z_pixel = 0

DECLARE @BuildString NVARCHAR(MAX)
SELECT @BuildString = COALESCE(@BuildString + ',', '') + CAST([x] AS NVARCHAR(50)) + ' ' + CAST([y] AS NVARCHAR(50))
FROM [MouseIleum].[dbo].[NewTable]

SET @BuildString = 'POLYGON((' + @BuildString + '))';
DECLARE @PolygonFromPoints geometry = geometry::STPolyFromText(@BuildString, 0);
SELECT @PolygonFromPoints.STIsValid();


SELECT *
    FROM (
        SELECT Top(1) *
        FROM [MouseIleum].[dbo].[MoleculesLayer0]) AS b
    WHERE @PolygonFromPoints.STIntersects(geometry::Point(b.[x_pixel], b.[y_pixel],0)) = 1
