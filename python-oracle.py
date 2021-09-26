import sqlalchemy
import cx_Oracle
from decouple import config

DP_ORACLE_HOST = "172.26.180.99"
DP_ORACLE_PORT = "1521"
DP_ORACLE_SID = "cdcout"
DP_ORACLE_USER = "CAR"
DP_ORACLE_PASSWORD = "ZEP[fzXHZ"


def oracle_conn():
	sid = cx_Oracle.makedsn(DP_ORACLE_HOST, DP_ORACLE_PORT, sid=DP_ORACLE_SID)

	DB_URL= f"oracle://{DP_ORACLE_USER}:{DP_ORACLE_PASSWORD}@{sid}"
	engine = sqlalchemy.create_engine(DB_URL)
	print(engine)
