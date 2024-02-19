import pandas as pd
import sqlite3
import pandas_datareader.data as web
import yfinance as yf

db_name = "stock_proces.db"
conn = sqlite3.connect(db_name)

start_date = "2024-01-01"
end_date = "2024-02-15"

ticker = "CRNC"

# df = web.DataReader(ticker, data_source = "yahoo", start = start_date, end = end_date)
data = yf.download("CRNC", start='2024-01-01', end='2024-02-15')
print(data)

data.to_sql("stock_data", conn, if_exists="replace", index=False)

conn.close
