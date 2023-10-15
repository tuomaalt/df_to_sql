import pandas as pd

def _df_to_sqlite_string(df:pd.DataFrame) -> str:
    '''
    sqlite specific implementation of df_to_sql_query. 

    Usage example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1, 2, 3], "col2":[4, 5, 6]})
    >>> _df_to_sqlite_string(df)
    "SELECT t1.column1 AS col1, t1.column2 AS col2 FROM (VALUES('1', '4'),('2', '5'),('3', '6')) AS t1"
    '''

    _values_ = _df_values_to_sqlite(df)
    _names_ = df_names_to_sqlite(df)

    return f"SELECT {_names_} FROM (VALUES{_values_}) AS t1"    
    

def _df_values_to_sqlite(df:pd.DataFrame) ->str:
    '''
    Sub-function fo _df_to_sqlite_string. 
    
    Usage example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1, 2, 3], "col2":[4, 5, 6]})
    >>> _df_values_to_sqlite(df)
    "('1', '4'),('2', '5'),('3', '6')"
    '''

    if len(df.index) < 1:
        return ''

    rows_df = df.copy()
    rows_df = rows_df.astype(str)
    rows_list = []

    for row in df.index:
        rows_string = "("+", ".join(["'"+str(x)+"'" for x in df.loc[row,:].astype(str).values])+")"
        rows_list.append(rows_string)
    
    rows_string = ",".join(rows_list)

    return rows_string


def df_names_to_sqlite(df:pd.DataFrame) -> str:
    '''
    Sub-function fo _df_to_sqlite_string. 
    
    Usage example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1, 2, 3], "col2":[4, 5, 6]})
    >>> df_names_to_sqlite(df)
    "t1.column1 AS col1, t1.column2 AS col2"
    '''
    col_list = [f"t1.column{i+1} AS {x}" for i, x in enumerate(df.columns.to_list())]
    
    return ", ".join(col_list)
