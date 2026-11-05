# 16. Physical layout

**In one line:** physical layout is how data sits on disk, and it strongly affects query speed and cost.

**Think of it like:** a filing cabinet. If each month has its own drawer, you open one drawer instead of searching them all.

<figure markdown="span">
  ![Partitioning and compaction](../assets/diagrams/16-1-light.svg#only-light)
  ![Partitioning and compaction](../assets/diagrams/16-1-dark.svg#only-dark)
  <figcaption>Partitioning and compaction</figcaption>
</figure>

<figure markdown="span">
  ![Partitioning, bucketing, clustering and indexes](../assets/diagrams/16-2-light.svg#only-light)
  ![Partitioning, bucketing, clustering and indexes](../assets/diagrams/16-2-dark.svg#only-dark)
  <figcaption>Partitioning, bucketing, clustering and indexes</figcaption>
</figure>

<figure markdown="span">
  ![Cardinality and data skipping](../assets/diagrams/16-3-light.svg#only-light)
  ![Cardinality and data skipping](../assets/diagrams/16-3-dark.svg#only-dark)
  <figcaption>Cardinality and data skipping</figcaption>
</figure>

The **small-files problem** is shown in the first picture: many tiny files slow reads, and **compaction** merges them, commonly into files of about 128 MB to 1 GB.

**Routine maintenance:** compact small files, remove old file versions after your recovery window, and keep statistics up to date.

**Remember:** partitioning by too many values creates the small-files problem it was meant to avoid.
