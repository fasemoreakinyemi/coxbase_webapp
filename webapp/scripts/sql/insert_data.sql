
USE MLVA;

LOAD DATA LOCAL INFILE '/home/travis/build/foerstner-lab/CoxBase-Webapp/webapp/scripts/sql/sql_tables/adaA_analyses.csv'
INTO TABLE adaAProfile
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/travis/build/foerstner-lab/CoxBase-Webapp/webapp/scripts/sql/sql_tables/is1111_analyses.csv'
INTO TABLE is1111Profile
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/travis/build/foerstner-lab/CoxBase-Webapp/webapp/scripts/sql/sql_tables/mlva_analyses.csv'
INTO TABLE ProductLengthISPCR
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/travis/build/foerstner-lab/CoxBase-Webapp/webapp/scripts/sql/sql_tables/mst_analyses.csv'
INTO TABLE mstSpacerResultTable
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/travis/build/foerstner-lab/CoxBase-Webapp/webapp/scripts/sql/sql_tables/isolates.csv'
INTO TABLE isolates
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/travis/build/foerstner-lab/CoxBase-Webapp/webapp/scripts/sql/sql_tables/mlva_query.csv'
INTO TABLE mlva_normalized
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/travis/build/foerstner-lab/CoxBase-Webapp/webapp/scripts/sql/sql_tables/mst_query.csv'
INTO TABLE mstgroups2
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/travis/build/foerstner-lab/CoxBase-Webapp/webapp/scripts/sql/sql_tables/geotables.csv'
INTO TABLE isolates_geolocation
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
