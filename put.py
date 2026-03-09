import psycopg2

nodes = [
    {
        "name": "IloIlo Warehouse",
        "host": "192.168.20.173",
        "port": 1235,
        "dbname": "iloilo_warehouse",  
        "user": "postgres",
        "password": "032805",
        "table": "orders"
    },
    {
        "name": "Davao Southern Warehouse",
        "host": "192.168.20.173",
        "port": 1234,
        "dbname": "davao_southern_warehouse", 
        "user": "postgres",
        "password": "032805",
        "table": "orders"
    }
]

target_node_name = "Davao Southern Warehouse"
target_customer_id = 14

updated_info = {
    "fullName": " rasman ",
    "street_address": "456 New Blvd",
    "city": "Quezon City",
    "region": "NCR"
}

print(f"\n--- UPDATING CUSTOMER ID: {target_customer_id} ---\n")

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

        query = """
            UPDATE customers
            SET fullName = %s,
                street_address = %s,
                city = %s,
                region = %s
            WHERE customer_id = %s;
        """

        cur.execute(query, (
            updated_info["fullName"],
            updated_info["street_address"],
            updated_info["city"],
            updated_info["region"],
            target_customer_id
        ))

        conn.commit()

        if cur.rowcount > 0:
            print(f" Success! Updated on {node['name']}")
        else:
            print(f" No record found with ID {target_customer_id} on {node['name']}")

    except Exception as e:
        print(f" Failed on {node['name']}: {e}")

    finally:
        if conn:
            conn.close()

print("\n--- UPDATE DONE ---")