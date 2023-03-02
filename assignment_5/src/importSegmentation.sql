USE MouseIleum;

DROP TABLE IF EXISTS Segmentation;
CREATE TABLE Segmentation (
    mol_id int NOT NULL,
    x_raw FLOAT,
    y_raw FLOAT,
    z_raw FLOAT,
    gene NVARCHAR(8),
    area tinyint,
    brightness float,
    total_magnitude	float,
    qc_score float,
    x float, -- has to be float not smallint bc the values are stored as floats eg 1705.0 
    y float,
    z float,
    id INT PRIMARY KEY NOT NULL,
    confidence float,
    compartment	NVARCHAR(20),
    nuclei_probs float,
    cell int NOT NULL,
    assignment_confidence float,
    is_noise nvarchar(5),
    ncv_color NVARCHAR(7)
);

BULK INSERT Segmentation FROM '/var/data/data_analysis/baysor/segmentation/segmentation.csv' WITH (
    FIRSTROW = 2, -- skip the column headers
    ROWS_PER_BATCH = 819665, -- however many total rows the data has
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '0x0a',
    KEEPNULLS
);

