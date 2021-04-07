from app import mysql
from .DBQuery import DBQuery
from .DBUpdate import DBUpdate

db_populate = DBPopulate(mysql)
db_query = DBQuery(mysql)
db_update= DBUpdate(mysql)