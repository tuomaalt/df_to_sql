import pandas as pd

def _df_values_to_sql(df:pd.DataFrame) ->str:
    '''
    Sub-function to _df_to_plsql_string. 

    Usage example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({"col1":[1, 2, 3], "col2":[4, 5, 6]})
    >>> _df_values_to_plsql(df)
    "('1', '4'),('2', '5'),('3', '6')"
    '''

    if len(df.index) < 1:
        return ''

    rows_df = df.copy(deep=True)
    rows_df = rows_df.astype(str)
    rows_list = []

    for row in df.index:
        rows_string = "("+", ".join(["'"+str(x)+"'" for x in df.loc[row,:].astype(str).values])+")"
        rows_list.append(rows_string)
    
    rows_string = ",".join(rows_list)

    return rows_string