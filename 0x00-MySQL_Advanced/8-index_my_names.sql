-- Create an index idx_name_first on the table names and the first letter of name.

-- Requirements:
--    Only the first letter of name must be indexed

CREATE INDEX `idx_name_first` ON names ((LEFT(name, 1)));