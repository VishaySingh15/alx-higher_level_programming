-- Creates a new user and grants superuser privileges
-- Creates new user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant user_0d_1 superuser privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
