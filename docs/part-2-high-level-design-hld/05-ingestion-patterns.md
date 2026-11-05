# 5. Ingestion patterns

**In one line:** ingestion brings data into the platform, and the best method depends on the source.

**Think of it like:** buying vegetables. ETL washes them on the farm before delivery. ELT delivers them first, and you wash them in your own kitchen.

<figure markdown="span">
  ![ETL vs. ELT · where the transform step happens](../assets/diagrams/05-1-light.svg#only-light)
  ![ETL vs. ELT · where the transform step happens](../assets/diagrams/05-1-dark.svg#only-dark)
  <figcaption>ETL vs. ELT · where the transform step happens</figcaption>
</figure>

ELT is the common default today, because storage is cheap and the raw copy allows rebuilds. ETL still suits cases where sensitive data must be masked before it leaves the source.

<figure markdown="span">
  ![CDC, pull and push, and event brokers](../assets/diagrams/05-2-light.svg#only-light)
  ![CDC, pull and push, and event brokers](../assets/diagrams/05-2-dark.svg#only-dark)
  <figcaption>CDC, pull and push, and event brokers</figcaption>
</figure>

**Log-based CDC** reads the database's transaction log and catches deletes. **Query-based CDC** looks for recently updated rows, which is simpler but misses deletes.

<figure markdown="span">
  ![Ingestion methods by source type](../assets/diagrams/05-3-light.svg#only-light)
  ![Ingestion methods by source type](../assets/diagrams/05-3-dark.svg#only-dark)
  <figcaption>Ingestion methods by source type</figcaption>
</figure>

**Remember:** copying whole tables every run works at first, then gets slow and expensive as they grow.
