CREATE TABLE "SHOE_DB"."ALL_SHOE_SCHEMA"."ALL_SHOES" ("ASINS" VARCHAR ),
 "BRAND" STRING, "CATEGORIES" STRING, "COLORS" STRING, "COUNT" VARCHAR (20), 
 "DATEADDED" VARCHAR (50), "DESCRIPTIONS" OBJECT, "DIMENSION" VARCHAR (30), "DOMIANS" OBJECT, 
 "EAN" FLOAT, "FEATURES" FLOAT, "FLAVORS" FLOAT, "IMAGEURLS" VARCHAR (1000), "KEYS" OBJECT, "MANUFACTURER" STRING,
 "MANUFACTURERNUMBER" VARCHAR (50), "MERCHANTS" OBJECT, "NAME" STRING, "prices.amountMin" FLOAT, "prices.amountMax" FLOAT, 
 "prices.availability" BOOLEAN, "prices.color" STRING, "prices.condition" STRING, "prices.count" INTEGER, "prices.currency" STRING,
 "prices.dateAdded" VARCHAR (200), "prices.flavor" STRING, "prices.isSale" BOOLEAN, "prices.merchant" STRING, "prices.offer" VARCHAR (50),
 "prices.returnPolicy" VARCHAR (50), "prices.shipping" STRING, "prices.size" STRING, "prices.source" STRING, "prices.sourceURLs" VARCHAR (300),
 "prices.warranty" STRING, "QUANTITIES" VARIANT, "REVIEWS" OBJECT, "SIZES" VARCHAR (200), "SKUS" OBJECT, "SOURCEURLS" VARCHAR (500), 
"UPC" FLOAT, "VIN" FLOAT, "WEBSITEIDS" FLOAT, "WEIGHT" VARIANT);



CREATE OR REPLACE TABLE MEN_SHOES ("id" VARCHAR ,
 "asins" VARCHAR, 
 "BRAND" VARCHAR,
 "CATEGORIES" VARCHAR,
 "COLORS" STRING, 
 "COUNT" VARCHAR ,
 "DATEADDED" VARCHAR ,
 "DATEUPDATED" VARCHAR,
 "DESCRIPTIONS" VARIANT, 
 "DIMENSION" VARCHAR , 
 "EAN" VARCHAR,
 "FEATURES_ONE" VARIANT, 
 "FEATURES_TWO" VARIANT,
 "FLAVORS"  VARCHAR, 
 "imageURLs" VARCHAR,
 "isbin" VARCHAR,
 "KEYS" VARCHAR,
 "MANUFACTURER" VARCHAR,
 "MANUFACTURERNUMBER" VARCHAR,
 "MERCHANT" VARIANT,
 "NAME" VARCHAR,
 "prices.amountMin"  FLOAT,
 "prices.amountMax" FLOAT,
 "prices.availability" STRING,
 "prices.color" STRING,
 "prices.condition" STRING,
 "prices.count" FLOAT, 
 "prices.currency" STRING,
 "prices.dateAdded" VARCHAR,
 "prices.dateSeen" VARCHAR,
 "prices.flavor" STRING,
"prices.isSale" BOOLEAN,
"prices.merchant" STRING,
"prices.offer" STRING,
"prices.returnPolicy" VARCHAR,
"prices.shipping" VARCHAR,
"prices.size" VARCHAR,
"prices.source" STRING,
"prices.sourceURLs" STRING,
"prices.warranty" STRING,
"quantities" STRING,
"reviewsone" VARIANT,
"reviewstwo"  VARIANT, 
"sizes" VARCHAR,
"skus" VARIANT,
"sourceURLs" VARCHAR,
"UPC" STRING,
"VIN" STRING,
"WEBSITEIDS" STRING,
"WEIGHT" STRING
 )
 
 
 
 
create or replace file format mycsvformat
  type = 'CSV'
  skip_header = 1
  FIELD_OPTIONALLY_ENCLOSED_BY='"'; 

create or replace stage my_csv_stage
  file_format = mycsvformat;
  

  
put file://g:\NEU\ADM\Assignmentone\manshoesdata.csv @my_csv_stage auto_compress = True;


copy into MEN_SHOES
 from @my_csv_stage/manshoesdata.csv.gz
 file_format = (format_name = mycsvformat)
 on_error = 'CONTINUE';
 
 
 create or replace table save_copy_errors as select * from table(validate(MEN_SHOES, job_id=>'019ab63d-00e4-d1e9-0000-81210001c036'));

 019ab63d-00e4-d1e9-0000-81210001c036

 
 
 
 
 
 
 
 
 
 
 
 
 "DOMIANS" OBJECT, 
 "EAN" FLOAT, "FEATURES" FLOAT, "FLAVORS" FLOAT, "IMAGEURLS" VARCHAR (1000), "KEYS" OBJECT, "MANUFACTURER" STRING,
 "MANUFACTURERNUMBER" VARCHAR (50), "MERCHANTS" OBJECT, "NAME" STRING, "prices.amountMin" FLOAT, "prices.amountMax" FLOAT, 
 "prices.availability" BOOLEAN, "prices.color" STRING, "prices.condition" STRING, "prices.count" INTEGER, "prices.currency" STRING,
 "prices.dateAdded" VARCHAR (200), "prices.flavor" STRING, "prices.isSale" BOOLEAN, "prices.merchant" STRING, "prices.offer" VARCHAR (50),
 "prices.returnPolicy" VARCHAR (50), "prices.shipping" STRING, "prices.size" STRING, "prices.source" STRING, "prices.sourceURLs" VARCHAR (300),
 "prices.warranty" STRING, "QUANTITIES" VARIANT, "REVIEWS" OBJECT, "SIZES" VARCHAR (200), "SKUS" OBJECT, "SOURCEURLS" VARCHAR (500), 
"UPC" FLOAT, "VIN" FLOAT, "WEBSITEIDS" FLOAT, "WEIGHT" VARIANT);