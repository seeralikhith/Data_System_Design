# 8. Orchestration

**In one line:** orchestration runs the right steps, in the right order, at the right time, and reacts when one fails.

**Think of it like:** following a recipe. You can chop and boil at the same time, but you can't serve until both are done.

**A DAG (Directed Acyclic Graph)** is how pipelines are usually defined. "Directed" means each dependency points one way. "Acyclic" means there are no loops, so the run always finishes.

<figure markdown="span">
  ![A simple DAG for a sales report · 5 tasks](../assets/diagrams/08-1-light.svg#only-light)
  ![A simple DAG for a sales report · 5 tasks](../assets/diagrams/08-1-dark.svg#only-dark)
  <figcaption>A simple DAG for a sales report · 5 tasks</figcaption>
</figure>

<figure markdown="span">
  ![Four pipeline triggers](../assets/diagrams/08-2-light.svg#only-light)
  ![Four pipeline triggers](../assets/diagrams/08-2-dark.svg#only-dark)
  <figcaption>Four pipeline triggers</figcaption>
</figure>

Tools include Apache Airflow, Dagster, Azure Data Factory and Lakeflow Jobs. They handle scheduling, retries, alerts and run history, and they leave the heavy data work to engines such as Spark.

**Remember:** don't schedule a job at 02:00 and hope the earlier job has finished. Make it wait for that job.
