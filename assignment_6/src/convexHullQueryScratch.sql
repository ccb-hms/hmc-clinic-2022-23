
SELECT CellNames.cell_name, cell_id FROM master.dbo.CellNames
    INNER JOIN MoleculesWithPointsHead
    ON MoleculesWithPointsHead.Cell_Name = CellNames.cell_name
    WHERE Centroid_Z = 3 AND animal_id = 1 AND bregma = 0.26

SELECT DISTINCT Cell_name FROM MoleculesWithPointsHead

SELECT * FROM CellNames where cell_name = '76af6c69-f1a7-4413-abaa-bd69ccad1e31'

SELECT Count(*) FROM master.dbo.CellNames -- 5812

SELECT * From master.dbo.CellNames Where cell_id =972

SELECT * FROM MoleculesWithPoints where cell_name = '76af6c69-f1a7-4413-abaa-bd69ccad1e31'

SELECT COUNT(DISTINCT cell_name) FROM MoleculesWithPoints

SELECT max(cell_id) FROM master.dbo.CellNames

SELECT max(animal_id) from MoleculesWithPoints

SELECT DISTINCT bregma from MoleculesWithPoints
-- WHERE animal_id = 1
ORDER BY bregma ASC

SELECT max(Centroid_Z) From MoleculesWithPoints
where animal_id = 1 and bregma = 0.01