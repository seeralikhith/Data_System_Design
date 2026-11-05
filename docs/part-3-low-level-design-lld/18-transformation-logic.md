# 18. Transformation logic

**In one line:** transformation logic must be **idempotent**, meaning that running it twice gives the same result as running it once.

**Think of it like:** an elevator button. Pressing it twice still takes you to the same floor once.

<figure markdown="span">
  ![Idempotent vs. non-idempotent writes](../assets/diagrams/18-1-light.svg#only-light)
  ![Idempotent vs. non-idempotent writes](../assets/diagrams/18-1-dark.svg#only-dark)
  <figcaption>Idempotent vs. non-idempotent writes</figcaption>
</figure>

**MERGE**, also called an **upsert**, updates rows that match a key and inserts the rest:

```sql
MERGE INTO silver.orders AS target
USING new_orders AS source
  ON target.order_id = source.order_id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *;
```

Overwriting a whole partition, such as one date, is another safe pattern.

**Deduplication** keeps one copy of each record, usually the newest. Do this before a `MERGE`, because duplicate keys can make it fail or give wrong results.

<figure markdown="span">
  ![ROW_NUMBER, RANK, LAG and SUM() OVER on the same data](../assets/diagrams/18-2-light.svg#only-light)
  ![ROW_NUMBER, RANK, LAG and SUM() OVER on the same data](../assets/diagrams/18-2-dark.svg#only-dark)
  <figcaption>ROW_NUMBER, RANK, LAG and SUM() OVER on the same data</figcaption>
</figure>

<figure markdown="span">
  ![Late facts and early facts](../assets/diagrams/18-3-light.svg#only-light)
  ![Late facts and early facts](../assets/diagrams/18-3-dark.svg#only-dark)
  <figcaption>Late facts and early facts</figcaption>
</figure>

**Refresh strategy:** a **full refresh** rebuilds the whole table, which suits small tables. **Incremental refresh** processes only new data, which suits large tables.

**Remember:** pass the run date in as a parameter, because logic that uses the current time gives different answers on a rerun.
