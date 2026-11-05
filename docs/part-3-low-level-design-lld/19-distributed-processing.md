# 19. Distributed processing

**In one line:** engines such as Apache Spark split work across many machines, and most slow jobs come from moving too much data between them.

**Think of it like:** a large kitchen. The head chef plans the work, the cooks do it, and carrying ingredients between stations is what slows everyone down.

<figure markdown="span">
  ![Driver, executors, tasks, partitions and shuffles](../assets/diagrams/19-1-light.svg#only-light)
  ![Driver, executors, tasks, partitions and shuffles](../assets/diagrams/19-1-dark.svg#only-dark)
  <figcaption>Driver, executors, tasks, partitions and shuffles</figcaption>
</figure>

A **partition** here is a chunk of data in memory, which is different from a table partition on disk.

**Lazy evaluation** means Spark builds a plan first and runs it only when a result is requested.

**Join strategies:**

<figure markdown="span">
  ![Broadcast join vs. shuffle join](../assets/diagrams/19-2-light.svg#only-light)
  ![Broadcast join vs. shuffle join](../assets/diagrams/19-2-dark.svg#only-dark)
  <figcaption>Broadcast join vs. shuffle join</figcaption>
</figure>

<figure markdown="span">
  ![Choosing between broadcast, sort-merge and shuffle hash joins](../assets/diagrams/19-3-light.svg#only-light)
  ![Choosing between broadcast, sort-merge and shuffle hash joins](../assets/diagrams/19-3-dark.svg#only-dark)
  <figcaption>Choosing between broadcast, sort-merge and shuffle hash joins</figcaption>
</figure>

**Data skew** means some keys hold far more data than others, like one checkout line with almost all the customers. One task runs much longer, and the whole job waits. Common fixes:

<figure markdown="span">
  ![A skewed job waiting on one task](../assets/diagrams/19-4-light.svg#only-light)
  ![A skewed job waiting on one task](../assets/diagrams/19-4-dark.svg#only-dark)
  <figcaption>A skewed job waiting on one task</figcaption>
</figure>

- Filter out junk keys, such as nulls.
- Broadcast the smaller table if it fits.
- Turn on **Adaptive Query Execution (AQE)**, which can split oversized partitions.
- Use **salting**, which adds a random value to spread busy keys across tasks.

**Signs to check when sizing a cluster:**

- **Out-of-memory (OOM) errors:** a worker ran out of memory, often because of skew.
- **Spill:** data overflowed from memory to disk, which slows the job.
- **Idle executors:** the cluster is bigger than the work needs.

**Remember:** filter early and select only the columns you need, so that less data has to move. That is the first step in **shuffle tuning**.
