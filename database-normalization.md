# Database Normalization: The 3 Golden Rules

Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity. The most common "Normal Forms" are 1NF, 2NF, and 3NF.

### 1. First Normal Form (1NF)
* **Rule:** Each column must contain atomic (indivisible) values, and there should be no repeating groups of data.
* *Example:* Don't store `phone_numbers` as a comma-separated list. Use a separate row for each number.

### 2. Second Normal Form (2NF)
* **Rule:** Must be in 1NF + all non-key attributes must depend on the **entire** primary key.
* *Example:* If you have a composite key (OrderID, ProductID), the "ProductPrice" should be in its own table, not the "OrderDetails" table, because price depends only on the ProductID.

### 3. Third Normal Form (3NF)
* **Rule:** Must be in 2NF + no "transitive dependencies."
* *Example:* If you have `ZipCode` and `City`, the `City` depends on the `ZipCode`, which depends on the `ID`. To reach 3NF, move `ZipCode/City` to their own table so `City` doesn't depend on the `ID` via the `ZipCode`.
