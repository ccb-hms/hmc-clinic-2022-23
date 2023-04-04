-- SELECT DISTINCT cell_name, IDENTITY(int,1,1) as cell_id
--     INTO CellNamesOneAnimalOneBregmaOneZ
--     FROM [MouseHypothalamus].[dbo].[MoleculesWithPoints]
--     where 1 = Animal_ID and bregma = 0.21 and Centroid_Z = 3

SELECT DISTINCT cell_name, IDENTITY(int,1,1) as cell_id
    INTO CellNames
    FROM [MouseHypothalamus].[dbo].[MoleculesWithPoints]