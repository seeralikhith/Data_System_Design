# 24. Query performance

**In one line:** the fastest query reads the least data.

**Think of it like:** finding a book in a library. You go to the right shelf instead of reading every book.

<figure markdown="span">
  ![How query performance techniques reduce the data read](../assets/diagrams/24-1-light.svg#only-light)
  ![How query performance techniques reduce the data read](../assets/diagrams/24-1-dark.svg#only-dark)
  <figcaption>How query performance techniques reduce the data read</figcaption>
</figure>

How you write a query matters too. A function on a partition column can stop the engine from skipping data:

```sql
-- Slower: may scan every partition
WHERE YEAR(order_date) = 2026

-- Faster: the engine can skip other years
WHERE order_date >= '2026-01-01'
  AND order_date <  '2027-01-01'
```

**To fix a slow query:**

1. Read its plan with `EXPLAIN`.
2. Replace `SELECT *` with only the columns you need.
3. Filter early, on partition or clustering columns.
4. Look for joins that multiply rows.
5. Add clustering or an aggregate table only if it is still slow.

**Remember:** look at the query plan before adding hardware.
