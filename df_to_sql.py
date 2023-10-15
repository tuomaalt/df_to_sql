import pandas as pd

from mod.sql_variant_enum import sql_variant
from mod.func_repo import func_repo


def df_to_sql_statement(df:pd.DataFrame, sql_variant_name:str) -> str:
    '''
    Wrapper to SQL-variant specific functions
    Creates SQL-query string which replicates the contents of pandas DataFrame. 

    Usage example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1, 2, 3], "col2":[4, 5, 6]})
    >>> df_to_sql_statement(df, "TSQL")
    "SELECT t1.* FROM (VALUES('1', '4'),('2', '5'),('3', '6')) AS t1(col1, col2)"
    
    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1, 2, 3], "col2":[4, 5, 6]})
    >>> df_to_sql_statement(df, "MySQL")
    "SELECT t1.* FROM (VALUES('1' as col1, '4' as col2),('2', '5'),('3', '6')) AS t1"

    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1, 2, 3], "col2":[4, 5, 6]})
    >>> df_to_sql_statement(df, "Postgre")
    "SELECT t1.* FROM (VALUES('1', '4'),('2', '5'),('3', '6')) AS t1(col1, col2)"

    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1, 2, 3], "col2":[4, 5, 6]})
    >>> df_to_sql_statement(df, "SQLite")
    "SELECT t1.column1 AS col1, t1.column2 AS col2 FROM (VALUES('1', '4'),('2', '5'),('3', '6')) AS t1"

    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1, 2, 3], "col2":[4, 5, 6]})
    >>> df_to_sql_statement(df, "MongoDB")
    'Requested sql variant MongoDB has not been implemented'
    
    '''

    try:
        sql_variant_enum = sql_variant[sql_variant_name.lower()]
    except KeyError as ke:
        return f"Requested sql variant {sql_variant_name} has not been implemented"

    func = func_repo.get(sql_variant_enum)

    return func(df)