
ITD101 Lab Activity: Distributed Database CRUD 🚀

Team Members (Trio):
1. Sualden Sala
2. Rasman Julsali
3. Ryan-ken Bagiuo

Topic: Distributed Database Systems  

## 📖 Overview
This repository contains Python scripts that demonstrate how to connect to and interact with multiple distributed PostgreSQL database nodes. The activity simulates a distributed warehouse system across the Philippines and performs cross-node CRUD (Create, Read, Update, Delete) operations using the `psycopg2` library.

## 🗄️ Database Nodes & Assignments
The scripts are configured to interact with 6 warehouse nodes across different IP addresses, divided among the team members:

Sualden S. Sala
  * Tawi-Tawi Warehouse
  * Cagayan de Oro Warehouse
Rasman Julsali
  * IloIlo Warehouse
  * Davao Southern Warehouse
Ryan-ken Bagiuo
  * Manila Warehouse
  * Pasig Warehouse

## ⚙️ Included Scripts & How They Work
We have mapped our Python scripts to standard RESTful operations (CRUD):

1. Create (`post.py` / `inserts.py`)
* Connects to a target warehouse (e.g., Davao Southern Warehouse) and inserts a new customer record into the `customers` table.

2. Read (`get.py` / `labassignment.py` / `second.py`)
* Iterates through multiple warehouse nodes, performs an SQL `JOIN` query between the `orders` and `customers` tables, and prints a formatted summary of Order IDs, Customer Names, Totals, and Statuses.

3. Update (`put.py` / `update.py`)
* Locates a specific `customer_id` on a target node and updates their details (Name, Address, City, Region).

4. Delete (`delete.py`)
* Locates a specific `customer_id` on a target node and removes their record from the database.

 🛠️ Setup Instructions

To run these scripts, you must have Python installed along with the PostgreSQL database adapter.

1. Install the required Python library:**
Open your terminal and run:

bash
pip install psycopg2
2. Ensure Network Access:
Make sure you are connected to the correct local network or VPN to access the specific database IP addresses for each warehouse.
🔄 Connecting to a Different Database
If you want to connect to a different database or your own local PostgreSQL server, you just need to change the IP address in the script!
Open any of the Python files and look for the nodes list. Simply change the "host" value to your new IP address:
Python


nodes = [
    {
        "name": "My Custom Warehouse",  #<--- CHANGE THIS NAME!
        "host": "192.168.X.X",  # <--- CHANGE THIS IP ADDRESS!
        "port": 5432, #<--- CHANGE THIS PORT!
        "dbname": "my_database", #<--- CHANGE THIS DATABASE NAME!
        "user": "postgres", #<--- CHANGE THIS USER!
        "password": "my_password" #<--- CHANGE THIS PASSWORD!
    }
]


▶️ Usage Instructions
You can run any of the scripts directly from the terminal. Navigate to the folder containing the scripts and execute them using Python:
To view all orders across the warehouses (Read):

``bash
python get.py
To add a new customer to a warehouse (Create):

``bash
python post.py
To update a customer's information (Update):

``bash
python put.py
To delete a customer (Delete):
Bash
python delete.py


