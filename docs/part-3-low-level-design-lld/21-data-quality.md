# 21. Data quality

**In one line:** quality checks catch bad data before it reaches a decision, and each check needs a planned response.

**Think of it like:** airport security. Everything is checked before boarding, and anything suspicious is set aside rather than waved through.

<figure markdown="span">
  ![Sample rows that fail quality checks](../assets/diagrams/21-1-light.svg#only-light)
  ![Sample rows that fail quality checks](../assets/diagrams/21-1-dark.svg#only-dark)
  <figcaption>Sample rows that fail quality checks</figcaption>
</figure>

**Key terms:**

- **Reconciliation:** comparing totals between systems, such as Gold revenue against the source system.
- **Quarantine table:** a holding area for rows that failed checks, so they can be reviewed instead of lost.
- **Write-Audit-Publish (WAP):** write new data to a hidden staging table, audit it, then publish only if it passes. Chapter 28 shows this as a diagram.

<figure markdown="span">
  ![Quality checks at each medallion layer](../assets/diagrams/21-2-light.svg#only-light)
  ![Quality checks at each medallion layer](../assets/diagrams/21-2-dark.svg#only-dark)
  <figcaption>Quality checks at each medallion layer</figcaption>
</figure>

**Remember:** Bronze should never lose data, and Gold should never publish wrong numbers. Tools include dbt tests, Great Expectations and Databricks pipeline expectations.
