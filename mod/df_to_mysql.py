import pandas as pd

def _df_to_mysql_string(df:pd.DataFrame) ->str:
    '''
    mysql specific implementation of df_to_sql_query. 
    
    Usage example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1, 2, 3], "col2":[4, 5, 6]})
    >>> _df_to_mysql_string(df)
    "SELECT t1.* FROM (VALUES('1' as col1, '4' as col2),('2', '5'),('3', '6')) AS t1"
    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1], "col2":[4]})
    >>> _df_to_mysql_string(df)
    "SELECT t1.* FROM (VALUES('1' as col1, '4' as col2)) AS t1"
    
    '''
    
    _row1_ =  _df_first_row_to_mysql(df)
    _rest_ =  _df_other_rows_to_mysql(df) 

    return f"SELECT t1.* FROM (VALUES{_row1_}{_rest_}) AS t1"


def _df_first_row_to_mysql(df:pd.DataFrame) -> str:
    '''
    Sub-function fo _df_to_mysql_string.
    
    Usage example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1, 2, 3], "col2":[4, 5, 6]})
    >>> _df_first_row_to_mysql(df)
    "('1' as col1, '4' as col2)"
    '''

    first_row_df = df.loc[0,:].copy()
    first_row_df = first_row_df.astype(str)
    first_row_zip = zip(first_row_df.values, first_row_df.index)
    first_row_string = ", ".join([f"'{v}' as {c}" for v, c in first_row_zip])
    
    return "(" + first_row_string + ")"


def _df_other_rows_to_mysql(df:pd.DataFrame) ->str:
    '''
    Sub-function fo df_to_sql_query. Meant to be internal to _df_to_tsql_string-function
    
    Usage example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1, 2, 3], "col2":[4, 5, 6]})
    >>> _df_other_rows_to_mysql(df)
    ",('2', '5'),('3', '6')"
    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1], "col2":[4]})
    >>> _df_other_rows_to_mysql(df)
    ''
    '''

    if len(df.index) < 2:
        return ""

    other_rows_df = df.loc[1:,:].copy()
    other_rows_df = other_rows_df.astype(str)
    other_rows_list = []

    for row in other_rows_df.index:
        rows_string = "("+", ".join(["'" + str(x) + "'" for x in other_rows_df.loc[row,:].astype(str).values])+")"
        other_rows_list.append(rows_string)
    
    other_rows_string = "," + ",".join(other_rows_list)

    return other_rows_string