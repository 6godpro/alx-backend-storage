--  create a trigger that decreases the quantity of an item after adding a new order.
CREATE TRIGGER order_item_created
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE holberton.items SET quantity=(quantity - NEW.number) WHERE name=NEW.item_name;
END;
