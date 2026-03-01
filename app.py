import os
import pandas as pd
import psycopg2
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="SQL Reporting Dashboard", layout="wide")

DATABASE_URL = os.getenv("DATABASE_URL")

st.title("SQL Reporting Dashboard")
st.caption("Simple UI. Serious SQL. Built as a portfolio project.")

if not DATABASE_URL:
    st.warning("DATABASE_URL is not set. Copy .env.example to .env and fill it in.")
    st.stop()

@st.cache_data(ttl=30)
def run_query(sql: str) -> pd.DataFrame:
    with psycopg2.connect(DATABASE_URL) as conn:
        return pd.read_sql_query(sql, conn)

st.subheader("KPIs")

kpi_sql = """
SELECT
  COUNT(*) AS total_orders,
  COALESCE(SUM(total_cents), 0) AS total_revenue_cents
FROM orders;
"""

df = run_query(kpi_sql)

col1, col2 = st.columns(2)
col1.metric("Total orders", int(df.iloc[0]["total_orders"]))
col2.metric("Revenue", f"${df.iloc[0]['total_revenue_cents'] / 100:,.2f}")

st.subheader("Recent orders")
orders_sql = """
SELECT id, customer_name, total_cents, created_at
FROM orders
ORDER BY created_at DESC
LIMIT 20;
"""
st.dataframe(run_query(orders_sql), use_container_width=True)
