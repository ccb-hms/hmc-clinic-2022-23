USE MouseIleum;
CREATE TABLE [dbo].[Molecules](
  molecule_id int,
  gene nvarchar(8),
  x_pixel smallint,
  y_pixel smallint,
  z_pixel float,
  x_um float,
  y_um float,
  z_um float,
  area tinyint,
  total_mag float,
  brightness float, 
  qc_score float
);

BULK INSERT [dbo].[Molecules] FROM '/var/data/raw_data/molecules.csv'
WITH ( 
    FIRSTROW = 2, -- skip the column headers
    ROWS_PER_BATCH = 819665, -- however many total rows the data has
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '0x0a',
    KEEPNULLS
);