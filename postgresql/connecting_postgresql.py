import psycopg2

# Database connection configuration
configconn = {
    "dbname": "testing_postgresql",
    "user": "highlander95",
    "password": "qazwsxedc12",
    "host": "localhost",
    "port": "5432"
}

try:
    # Connect to the database using the config dictionary
    conn = psycopg2.connect(**configconn)
    print("✅ Connected to the database!")

    cur = conn.cursor()

    # Create table if it doesn't exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        );
    """)
    conn.commit()
    print("✅ Table created or already exists.")

    # Insert sample data
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Alice", "alice@example.com"))
    conn.commit()
    print("✅ Data inserted.")

    # Fetch and display all rows
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()
    print("📋 Fetched rows:")
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    conn.close()
    print("✅ Connection closed.")

except Exception as e:
    print("❌ An error occurred:", e)