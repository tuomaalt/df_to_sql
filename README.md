# df_to_sql

Function takes pandas Dataframe and outputs an SQL-select statement with requested SQL-variant. Output SQL-statement produces a table containing the data in input dataframe when run. 

NOTE: More precies datatypes are left to user and all values in output SQL-statement are strings to mitigate datatype errors.

Potential usage:
Complex sequential queries where results of a previous query are used as inputs to next one. In some cases it might make sense to run queries independently, e.g say when data is in separate servers or database is 
not optimized properly, and more sophisticated ETL-tools are not available.
