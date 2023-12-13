# Postgres for storing and retrieving data

---

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)

---
## General info
This Folder contain second task for job interview. 
The task consist of loading data to Postgres database and finding suitable query for each question.
There are three `.python` file and four `.sql` file in this directory.


The *postgres_connection_test.py* file is simple script to check whether the connection to postgres database is OK or not. 

The *import_paytype_data.py* , first creates a connection to DB, then reads data from an `.xlsx` file, then create a table and import data to created table as `paytype`. 

IN *script_for_inserting_REF_CBS_SMS2_data.py* file, We also read file then define the data types for each data entry, then we create a connection and create table with mentioned data types, at last we insert our data into `REF_CBS_SMS2` table.

---
## Technologies
Project is created with:
* Python: 3.10
* Postgres: 14


