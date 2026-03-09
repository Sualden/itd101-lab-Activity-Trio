import psycopg2

nodes = [
    {
        "name": "Manila Warehouse",
        "host": "192.168.88.133",
        "port": 5435,
        "dbname": "manila_werehouse",   # <--- 1. Lowercase, 2. Spelled 'warehouse'
        "user": "ken2",
        "password": "pass2",
        "table": "orders"
    },
    {
        "name": "Pasig Warehouse",
        "host": "192.168.88.133",
        "port": 5434,
        "dbname": "pasig_werehouse", 
        "user": "ken1",
        "password": "pass1",
        "table": "orders"
    }
]
for node in nodes:
    conn = None 
    try:
        conn = psycopg2.connect(
            host=node["host"],
            port=node["port"],
            dbname=node["dbname"],
            user=node["user"],
            password=node["password"],
            connect_timeout=5
        )

        cur = conn.cursor()
        
        query = f"""
            SELECT o.order_id, c.fullName, o.order_total, o.order_status 
            FROM {node['table']} o
            JOIN customers c ON o.customer_id = c.customer_id
        """
        cur.execute(query)
        rows = cur.fetchall()

        print(f" Data from: {node['name']} ({node['host']}:{node['port']})")
        print(f"{'Order ID':<10} {'Customer Name':<20} {'Total':<10} {'Status'}")
        print("-" * 50)
        
        for r in rows:
            print(f"{str(r[0]):<10} {r[1]:<20} {r[2]:<10} {r[3]}")
        
        print("\n")

    except Exception as e:
        print(f" Failed to connect to {node['name']}: {e}\n")
    
    finally:
        if conn:
            conn.close()
