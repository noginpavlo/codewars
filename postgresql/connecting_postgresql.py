import psycopg2

# Database connection configuration
configconn = {
    "dbname": "testing_postgresql",
    "user": "highlander95",
    "password": "qazwsxedc12",
    "host": "localhost",
    "port": "5432",
}

try:
    # Connect to the database
    conn = psycopg2.connect(**configconn)
    print("✅ Connected to the database!")

    # Create a cursor object
    cur = conn.cursor()

    # Check current user
    cur.execute("SELECT current_user;")
    print("Current User:", cur.fetchone())

    # Check if the 'users' table exists
    cur.execute(
        "SELECT table_schema, table_name FROM information_schema.tables WHERE table_name = 'users';"
    )
    print("Table Schema and Name:", cur.fetchone())

    # Check table owner and privileges
    cur.execute(
        "SELECT tableowner, has_table_privilege('highlander95', 'public.users', 'select') "
        "FROM pg_tables WHERE tablename = 'users';"
    )
    print("Table Owner and Privileges:", cur.fetchone())

    # Insert sample data into public.users if table exists
    cur.execute(
        "INSERT INTO public.users (name, email) VALUES (%s, %s)",
        ("Alice", "alice@example.com"),
    )
    conn.commit()
    print("✅ Data inserted.")

    # Fetch and display all rows from public.users
    cur.execute("SELECT * FROM public.users;")
    rows = cur.fetchall()
    print("📋 Fetched rows:")
    for row in rows:
        print(row)

    # Clean up: Close the cursor and connection
    cur.close()
    conn.close()
    print("✅ Connection closed.")

except Exception as e:
    print("❌ An error occurred:", e)
