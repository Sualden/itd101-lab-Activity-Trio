import psycopg2

# 1. Define your Warehouse Nodes
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

new_customer = {
    "fullName": "Kimww mal",          
    "phone": "0990400999",             
    "street_address": "Rasman House",
    "city": "Bonago City",
    "region": "Barmm"
}


print(f"--- ADDING CUSTOMER: {new_customer['fullName']} ---\n")
 
for node in nodes:
    if node["name"] != target_node_name:
        continue
    
    conn = None
    try:
        # 3. Connect to the database
        conn = psycopg2.connect(
            host=node["host"],
            port=node["port"],
            dbname=node["dbname"],
            user=node["user"],
            password=node["password"],
            connect_timeout=5
        )
        
        cur = conn.cursor()

        insert_query = """
            INSERT INTO customers (fullName, phone, street_address, city, region)
            VALUES (%s, %s, %s, %s, %s);
        """
        
        cur.execute(insert_query, (
            new_customer["fullName"],     
            new_customer["phone"],          
            new_customer["street_address"],
            new_customer["city"],           
            new_customer["region"]          
        ))
        conn.commit() 

        print(f" Success! Added customer to {node['name']}")
    except Exception as e:
        print(f" Failed on {node['name']}: {e}")

    finally:
        if conn:
            conn.close()

print("\n--- DONE ---")
