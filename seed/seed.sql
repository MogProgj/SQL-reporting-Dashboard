CREATE TABLE IF NOT EXISTS orders (
  id BIGSERIAL PRIMARY KEY,
  customer_name TEXT NOT NULL,
  total_cents INTEGER NOT NULL CHECK (total_cents >= 0),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

INSERT INTO orders (customer_name, total_cents)
VALUES
  ('Acme Foods', 129900),
  ('Bluebird Cafe', 45900),
  ('Northside Deli', 78500)
ON CONFLICT DO NOTHING;
