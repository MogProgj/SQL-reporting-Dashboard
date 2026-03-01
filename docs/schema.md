# Database Schema

## orders

| Column          | Type          | Constraints                       |
|-----------------|---------------|-----------------------------------|
| id              | BIGSERIAL     | PRIMARY KEY                       |
| customer_name   | TEXT          | NOT NULL                          |
| total_cents     | INTEGER       | NOT NULL, CHECK (total_cents >= 0)|
| created_at      | TIMESTAMPTZ   | NOT NULL, DEFAULT now()           |

Monetary values are stored in cents to avoid floating-point rounding issues.

## Intended expansion

Future tables may include:

- **customers** – normalise customer data out of orders.
- **products** / **line_items** – support multi-item orders.
- **categories** – enable breakdowns by product category.
- **tickets** – if integrated with TicketFlow/MiniERP data.
