import psycopg2

nodes = [
    {
        "name": "IloIlo Warehouse",
        "host": "192.168.20.173",
        "port": 1235,
        "dbname": "iloilo_warehouse",
        "user": "postgres",
        "password": "032805"
    },
    {
        "name": "Davao Southern Warehouse",
        "host": "192.168.20.173",
        "port": 1234,
        "dbname": "davao_southern_warehouse",
        "user": "postgres",
        "password": "032805"
    }
]

target_node_name = "Davao Southern Warehouse"
target_customer_id = 14

print(f"\n--- DELETING CUSTOMER ID: {target_customer_id} ---\n")

for node in nodes:
    if node["name"] != target_node_name:
        continue

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

        query = "DELETE FROM customers WHERE customer_id = %s;"
        cur.execute(query, (target_customer_id,))

        conn.commit()

        if cur.rowcount > 0:
            print(f" Success! Deleted from {node['name']}")
        else:
            print(f" No record found with ID {target_customer_id} on {node['name']}")

    except Exception as e:
        print(f" Failed on {node['name']}: {e}")

    finally:
        if conn:
            conn.close()

print("\n--- DELETE COMPLETE ---")