# SQL vs. NoSQL: The Great Database Debate

Choosing between a Relational (SQL) and Non-Relational (NoSQL) database is one of the most important decisions in system design. It’s a trade-off between strict structure and flexible scaling.

### 📊 Comparison at a Glance

| Feature | SQL (Relational) | NoSQL (Non-Relational) |
| :--- | :--- | :--- |
| **Schema** | Rigid, predefined. | Flexible, dynamic. |
| **Scaling** | Vertical (Bigger server). | Horizontal (More servers). |
| **Data Model** | Tables with rows/columns. | Document, Key-Value, Graph. |
| **Integrity** | ACID Compliance. | BASE (Eventual Consistency). |

```mermaid
graph LR
    subgraph SQL_Table
    R1["Row 1: ID, Name, Email"]
    R2["Row 2: ID, Name, Email"]
    end

    subgraph NoSQL_Document
    D1["JSON: {id, name, contacts: [...]}"]
    D2["JSON: {id, name, preferences: {...}}"]
    end
