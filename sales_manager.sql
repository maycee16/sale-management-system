-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS 'sales_management';
CREATE USER IF NOT EXISTS 'sales_manager'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `sales_management`.* TO 'sales_manager'@'localhost';
FLUSH PRIVILEGES;