-- create database holberton on the server
CREATE DATABASE IF NOT EXISTS holberton;
-- switch to the holberton db
USE holberton;
-- create a table called users
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255)
);