import pandas as pd

def _df_to_postgre_string(df:pd.DataFrame) ->str:
    '''
    Sub-function fo df_to_sql_query. Meant to be internal to _df_to_tsql_string-function
    
    Usage example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1, 2, 3], "col2":[4, 5, 6]})
    >>> _df_to_postgre_string(df)
    "SELECT t1.* FROM (VALUES('1', '4'),('2', '5'),('3', '6')) AS t1(col1, col2)"
    '''

    values = _df_values_to_postgre(df)
    names = _df_names_to_postgrel(df)

    return f"SELECT t1.* FROM (VALUES{values}) AS t1({names})"


def _df_values_to_postgre(df:pd.DataFrame) ->str:
    '''
    Sub-function fo _df_to_postgre_string.
    
    Usage example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1, 2, 3], "col2":[4, 5, 6]})
    >>> _df_values_to_postgre(df)
    '('1', '4'),('2', '5'),('3', '6')'
    '''

    if len(df.index) < 1:
        return ''

    rows_df = df.copy()
    rows_df = rows_df.astype(str)
    rows_list = []

    for row in df.index:
        rows_string = "("+", ".join(["'"+str(x)+"'" for x in df.loc[row,:].astype(str).values])+")"
        rows_list.append(rows_string)
    
    other_rows_string = ",".join(rows_list)

    return other_rows_string

def _df_names_to_postgrel(df:pd.DataFrame) -> str:
    '''
    Sub-function fo _df_to_postgre_string.
    
    Usage example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1, 2, 3], "col2":[4, 5, 6]})
    >>> _df_names_to_postgrel(df)
    'col1, col2'
    '''
    
    return ", ".join(df.columns.tolist())