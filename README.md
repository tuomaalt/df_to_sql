# df_to_sql

Given pandas DataFrame, function outputs SQL-statement string. This string produces a table containing the data in input dataframe when run in SQL database. 

inputs: 
  df:pandas Dataframe,
  sql_variant:string 

output: 
  string 

NOTE: More precies datatypes are left to user and all values in output SQL-statement are strings to mitigate datatype errors.

    Usage example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1, 2, 3], "col2":[4, 5, 6]})
    >>> df_to_sql_statement(df, "TSQL")
    'SELECT t1.* FROM (VALUES(1, 4),(2, 5),(3, 6)) AS t1(col1, col2)'
    
    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1, 2, 3], "col2":[4, 5, 6]})
    >>> df_to_sql_statement(df, "MySQL")
    "SELECT t1.* FROM (VALUES('1' as col1, '4' as col2),('2', '5'),('3', '6')) AS t1"

Potential usage:
Complex sequential queries where results of a previous query are used as inputs to next one. In some cases it might make sense to run queries independently, e.g say when data is in separate servers or database is not optimized properly, and more sophisticated ETL-tools are not available.

Example: you need to fetch dates when a customer first filled some complex set of conditions (say, purchsed a particular combination of products) and then fetch a set of furhter records based on that date & customer-combination.

To lighten the query load you could run 

WITH
customer AS ("results of previous query as produced by df_to_sql-function"),
SELECT 
  *stuff*
FROM table1 AS t1
INNER JOIN customer AS t2 ON t1.customer_id = t2.customer_id AND t1.date = t2.date;

WITH
customer AS ("results of previous query as produced by df_to_sql-function"),
SELECT 
  *more stuff*
FROM table2 AS t1
INNER JOIN customer AS t2 ON t1.customer_id = t2.customer_id AND t1.date = t2.date;

instead of re-running expensive customer-query for both queries separately. This assumes that creation of temporary tables is not possible (e.g you are using Hadoop)

