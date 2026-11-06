import sqlite3

# 1. Connect to database
connection = sqlite3.connect("shopping.db")

# 2. Create cursor
cursor = connection.cursor()

# 3. Enable foreign key constraints
cursor.execute("PRAGMA foreign_keys = ON")

# 4. Create Customers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INTEGER PRIMARY KEY,
    CustomerName TEXT NOT NULL,
    Email TEXT
)
""")

# 5. Create Orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders (
    OrderID INTEGER PRIMARY KEY,
    OrderDate TEXT,
    CustomerID INTEGER,
    TotalAmount REAL,
    FOREIGN KEY (CustomerID)
    REFERENCES Customers(CustomerID)
)
""")

# 6. Insert customers
customers = [
    (101, "Alice", "alice@email.com"),
    (102, "Bob", "bob@email.com")
]

cursor.executemany("""
INSERT OR IGNORE INTO Customers
VALUES (?, ?, ?)
""", customers)

# 7. Insert orders
orders = [
    (5001, "2026-11-01", 101, 25.00),
    (5002, "2026-11-03", 102, 150.00),
    (5003, "2026-11-05", 101, 45.00)
]

cursor.executemany("""
INSERT OR IGNORE INTO Orders
VALUES (?, ?, ?, ?)
""", orders)

connection.commit()

# 8. Display joined records
cursor.execute("""
SELECT
    Orders.OrderID,
    Orders.OrderDate,
    Customers.CustomerName,
    Orders.TotalAmount
FROM Orders
INNER JOIN Customers
ON Orders.CustomerID = Customers.CustomerID
""")

results = cursor.fetchall()

for row in results:
    print(row)

# 9. Close connection
connection.close()