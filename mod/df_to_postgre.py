import pandas as pd
from mod.df_values_to_sql import _df_values_to_sql

def _df_to_postgre_string(df:pd.DataFrame) ->str:
    '''
    postgre specific implementation of df_to_sql_query. 

    Usage example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1, 2, 3], "col2":[4, 5, 6]})
    >>> _df_to_postgre_string(df)
    "SELECT t1.* FROM (VALUES('1', '4'),('2', '5'),('3', '6')) AS t1(col1, col2)"
    '''

    _values_ = _df_values_to_postgre(df)
    _names_ = _df_names_to_postgrel(df)

    return f"SELECT t1.* FROM (VALUES{_values_}) AS t1({_names_})"


def _df_values_to_postgre(df:pd.DataFrame) ->str:
    '''
    Sub-function fo _df_to_postgre_string.
    
    Usage example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1, 2, 3], "col2":[4, 5, 6]})
    >>> _df_values_to_postgre(df)
    '('1', '4'),('2', '5'),('3', '6')'
    '''

    return _df_values_to_sql(df)

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