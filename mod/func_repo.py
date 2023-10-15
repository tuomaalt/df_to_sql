from mod.sql_variant_enum import sql_variant
from mod.df_to_mysql import _df_to_mysql_string
from mod.df_to_tsql import _df_to_tsql_string
from mod.df_to_postgress import _df_to_postgress_string

func_repo = {    
    sql_variant.mysql:_df_to_mysql_string,
    sql_variant.tsql:_df_to_tsql_string,
    sql_variant.postgre:_df_to_postgress_string
    }