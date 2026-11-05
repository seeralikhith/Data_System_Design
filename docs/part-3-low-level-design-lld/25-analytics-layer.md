# 25. Analytics layer

**In one line:** the analytics layer turns clean tables into trusted answers, and every metric needs one agreed definition.

**Think of it like:** a shared dictionary. If two teams define "revenue" differently, their reports will never match.

<figure markdown="span">
  ![A KPI (key performance indicator) definition card](../assets/diagrams/25-1-light.svg#only-light)
  ![A KPI (key performance indicator) definition card](../assets/diagrams/25-1-dark.svg#only-dark)
  <figcaption>A KPI (key performance indicator) definition card</figcaption>
</figure>

**Metric grain** is the level of detail at which a metric is valid. Not every measure can simply be added up:

<figure markdown="span">
  ![Additive, semi-additive and non-additive measures](../assets/diagrams/25-2-light.svg#only-light)
  ![Additive, semi-additive and non-additive measures](../assets/diagrams/25-2-dark.svg#only-dark)
  <figcaption>Additive, semi-additive and non-additive measures</figcaption>
</figure>

<figure markdown="span">
  ![Metric definitions with and without a semantic model · made-up figures](../assets/diagrams/25-3-light.svg#only-light)
  ![Metric definitions with and without a semantic model · made-up figures](../assets/diagrams/25-3-dark.svg#only-dark)
  <figcaption>Metric definitions with and without a semantic model · made-up figures</figcaption>
</figure>

**Three more terms:**

- **Aggregate table:** pre-calculated totals, so dashboards don't scan every detail row.
- **Incremental refresh:** updating only recent data rather than rebuilding everything.
- **Import vs. live mode:** import copies data into the BI tool for speed, while live or DirectQuery mode queries the source for fresher data.

**For fast dashboards:** read from Gold or aggregate tables, set default date filters, and limit the visuals on each page, because each one usually sends its own query.

**Remember:** agree the definition first, because no dashboard can fix a disputed metric.
