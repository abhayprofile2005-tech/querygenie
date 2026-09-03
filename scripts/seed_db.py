import sqlite3

conn = sqlite3.connect("data/sample.db")
cur = conn.cursor()

cur.executescript("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY, name TEXT, city TEXT, region TEXT
);
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY, customer_id INTEGER, amount REAL,
    order_date TEXT, FOREIGN KEY(customer_id) REFERENCES customers(id)
);
""")

cur.executemany("INSERT INTO customers VALUES (?,?,?,?)", [
    (1, "Rahul Verma", "Prayagraj", "North"),
    (2, "Sneha Iyer", "Chennai", "South"),
    (3, "Amit Das", "Kolkata", "East"),
])
cur.executemany("INSERT INTO orders VALUES (?,?,?,?)", [
    (1, 1, 2500.0, "2026-06-10"),
    (2, 2, 4800.0, "2026-06-15"),
    (3, 1, 1200.0, "2026-07-02"),
    (4, 3, 3300.0, "2026-07-20"),
])
conn.commit()
conn.close()
print("Seeded sample.db")