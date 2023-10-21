from mod.sql_variant_enum import sql_variant
from mod.df_to_mysql import _df_to_mysql_string
from mod.df_to_tsql import _df_to_tsql_string
from mod.df_to_postgre import _df_to_postgre_string
from mod.df_to_sqlite import _df_to_sqlite_string
from mod.df_to_plsql import _df_to_plsql_string

func_repo = {    
    sql_variant.mysql:_df_to_mysql_string,
    sql_variant.tsql:_df_to_tsql_string,
    sql_variant.pgsql:_df_to_postgre_string,
    sql_variant.sqlite:_df_to_sqlite_string,
    sql_variant.plsql:_df_to_plsql_string
    }