# 15. Schema design

**In one line:** schema design starts with the **grain**, which is what one row in a table represents.

**Think of it like:** a shop receipt. Each line on the receipt is a row in a **fact table**. Details about the customer and product live in **dimension tables**.

<figure markdown="span">
  ![Star schema for order lines · 1 fact table and 4 dimensions](../assets/diagrams/15-1-light.svg#only-light)
  ![Star schema for order lines · 1 fact table and 4 dimensions](../assets/diagrams/15-1-dark.svg#only-dark)
  <figcaption>Star schema for order lines · 1 fact table and 4 dimensions</figcaption>
</figure>

In a **star schema**, each dimension joins directly to the fact table, as shown above. In a **snowflake schema**, dimensions are split into more tables, which reduces repetition but adds joins. Start with a star for BI.

<figure markdown="span">
  ![Transaction, periodic snapshot and accumulating snapshot facts](../assets/diagrams/15-2-light.svg#only-light)
  ![Transaction, periodic snapshot and accumulating snapshot facts](../assets/diagrams/15-2-dark.svg#only-dark)
  <figcaption>Transaction, periodic snapshot and accumulating snapshot facts</figcaption>
</figure>

<figure markdown="span">
  ![Surrogate, natural and foreign keys](../assets/diagrams/15-3-light.svg#only-light)
  ![Surrogate, natural and foreign keys](../assets/diagrams/15-3-dark.svg#only-dark)
  <figcaption>Surrogate, natural and foreign keys</figcaption>
</figure>

**Slowly changing dimensions (SCD)** decide what happens when details change:

<figure markdown="span">
  ![SCD Types 1, 2 and 3 for the same change](../assets/diagrams/15-4-light.svg#only-light)
  ![SCD Types 1, 2 and 3 for the same change](../assets/diagrams/15-4-dark.svg#only-dark)
  <figcaption>SCD Types 1, 2 and 3 for the same change</figcaption>
</figure>

Use Type 2 when reports must show past values. Its rows usually carry a surrogate key and `valid_from` and `valid_to` dates. **Type 0** never changes, which suits fixed values such as date of birth.

**Two more choices:**

- **Data types:** use `DECIMAL` for money, because `FLOAT` causes rounding errors. Store timestamps in UTC.
- **Normalization vs. denormalization:** normalization stores each fact once, which suits updates. Denormalization repeats data to avoid joins, which suits analytics.

**Remember:** decide the grain first, because mixing grains causes double counting.
