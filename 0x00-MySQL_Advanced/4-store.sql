-- Active: 1694002041516@@127.0.0.1@3306@holberton
--  create a trigger that decreases the quantity of an item after adding a new order.
CREATE TRIGGER order_item_created
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = (quantity - NEW.number) WHERE name=NEW.item_name;
