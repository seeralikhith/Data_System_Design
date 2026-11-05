# 6. Storage

**In one line:** keep the systems that run the business separate from the systems that analyze it, then organize analytical data by quality.

**Think of it like:** a shop. The checkout handles one sale at a time. The accountant looks at a whole year of sales.

**OLTP (Online Transaction Processing)** is the checkout, updating one order at a time. **OLAP (Online Analytical Processing)** is the accountant, totaling millions of orders.

<figure markdown="span">
  ![Row storage vs. columnar storage](../assets/diagrams/06-1-light.svg#only-light)
  ![Row storage vs. columnar storage](../assets/diagrams/06-1-dark.svg#only-dark)
  <figcaption>Row storage vs. columnar storage</figcaption>
</figure>

<figure markdown="span">
  ![Data warehouse, data lake and lakehouse](../assets/diagrams/06-2-light.svg#only-light)
  ![Data warehouse, data lake and lakehouse](../assets/diagrams/06-2-dark.svg#only-dark)
  <figcaption>Data warehouse, data lake and lakehouse</figcaption>
</figure>

**Open table formats** such as Delta Lake, Apache Iceberg and Apache Hudi are the table layer in a lakehouse:

<figure markdown="span">
  ![ACID transactions, schema enforcement and time travel](../assets/diagrams/06-3-light.svg#only-light)
  ![ACID transactions, schema enforcement and time travel](../assets/diagrams/06-3-dark.svg#only-dark)
  <figcaption>ACID transactions, schema enforcement and time travel</figcaption>
</figure>

**Medallion architecture** organizes tables by quality: **Bronze** is raw and append-only, **Silver** is clean, and **Gold** is business-ready and the only layer reports read from. Chapter 1 shows the flow.

**Storage tiers** save money: often-used data stays in a **hot** tier, and rarely used data moves to a cheaper **cold** tier.

**Remember:** Bronze, Silver and Gold are a way of organizing data, not a product you buy.
