python3 manage.py runserver -> strat server

python3 manage.py startapp NAME -> vytvorime si novu app a ptm ju musime pridat do settings.py

SOURCE 
https://www.youtube.com/watch?v=PtQiiknWUcI


start db in docker
docker run -d --name my_postgres_db \
  -e POSTGRES_DB=postgres-db \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=root \
  -v /postgres-data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13

docker exec -it my_postgres_db psql -U admin -d postgres-db

Some basics for communication with postgresDB in command line
Exit psql:
Exit the psql command-line tool:
\q
List all the available databases:
\l
Connect to a specific database:
\c database_name
List all tables in the current database:
\dt
Display the structure of a specific table:
\d table_name
Query Data:
Run a SQL query to retrieve data from a table:
SELECT * FROM table_name;
Insert Data:
Insert a new row into a table:
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
Update Data:
Update existing rows in a table:
UPDATE table_name SET column1 = new_value1, column2 = new_value2 WHERE condition;
Delete Data:
Delete rows from a table based on a condition:
DELETE FROM table_name WHERE condition;
Create Table:
Create a new table with specified columns:
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);
Drop Table:
Delete a table (irreversible action):
DROP TABLE table_name;
