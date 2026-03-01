# SQL Reporting Dashboard

This project is a small reporting dashboard built on top of a relational database. The point is to turn raw tables into decision-friendly metrics: KPIs, trends, filters, and exports. It’s meant to be fast to run locally and easy to extend with new queries.

The UI will be intentionally simple. The value is in the data model and the SQL.

## Tech stack
PostgreSQL (Docker)
Python
Streamlit (dashboard UI)

## What it will show (MVP)
A handful of business-style KPIs and drilldowns, such as:
Revenue or volume over time
Top customers or products
Breakdowns by category
A filtered table view
CSV export for reports

The underlying dataset can be either:
A classic “orders/products/customers” dataset
Or data reused from my TicketFlow/MiniERP projects later on

## Quickstart (local)
Prerequisites:
Docker and Python 3.10+.

1) Start the database
docker compose up -d

2) Create a virtual environment and install deps
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

3) Seed the database (example)
psql postgresql://postgres:postgres@localhost:5432/reporting -f seed/seed.sql

4) Run the dashboard
streamlit run app.py

## Configuration
The app will read a DATABASE_URL.

Example:
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/reporting

You can set it in your shell or use a .env file depending on your setup.

## Repo layout (planned)
app.py
requirements.txt
sql/
kpis.sql
reports.sql
seed/
seed.sql
docker-compose.yml

## KPIs and reports (planned)
Examples of queries this project will include:
Revenue or ticket volume in the last 7/30/90 days
Top 10 products/customers
Average order value
Resolution time distribution (if using ticket data)
Week-over-week changes and spikes

## Roadmap
- [ ] Finalize dataset and schema
- [ ] Seed script with realistic sample data
- [ ] MVP dashboard pages and filters
- [ ] Add caching for faster queries
- [ ] Safe parameterized queries
- [ ] CSV export
- [ ] “Anomalies” page for unusual spikes/drops (optional)

## License
MIT
