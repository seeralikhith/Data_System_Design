# 28. Worked example: a retail sales report

**In one line:** a made-up online store wants a trusted sales dashboard every morning, and a daily batch lakehouse meets that need without the cost of streaming.

<figure markdown="span">
  ![Daily retail sales run · 3 sources and 1 audit gate](../assets/diagrams/28-1-light.svg#only-light)
  ![Daily retail sales run · 3 sources and 1 audit gate](../assets/diagrams/28-1-dark.svg#only-dark)
  <figcaption>Daily retail sales run · 3 sources and 1 audit gate</figcaption>
</figure>

**Step 1: Requirements**

- **Sources:** orders database, payment API and daily product files.
- **Users:** sales managers reading a dashboard.
- **Question:** what is net revenue by day, store and product?
- **Freshness:** yesterday's data by 07:00 each day.
- **Volume:** 200,000 orders a day at about 1 KB each, or about 200 MB a day.
- **Compliance:** customer emails are PII.

**Step 2: HLD**

| Area | Decision | Why |
| --- | --- | --- |
| Processing | Daily batch | Managers check results each morning |
| Ingestion | CDC, scheduled pull and file arrival | Each method fits its source |
| Storage | Lakehouse with medallion layers | Keeps raw data for rebuilds |
| Modeling | Kimball star schema | Best fit for BI |
| Orchestration | One DAG with retries and alerts | Steps run in order, and failures are visible |
| Serving | SQL warehouse and dashboard | Everyone sees the same numbers |
| Governance | Managers read Gold only, emails masked | Protects PII |
| Reliability | RPO of 1 day, RTO of 4 hours | Matches a daily report's needs |

**Step 3: LLD**

<figure markdown="span">
  ![LLD for the retail example](../assets/diagrams/28-2-light.svg#only-light)
  ![LLD for the retail example](../assets/diagrams/28-2-dark.svg#only-dark)
  <figcaption>LLD for the retail example</figcaption>
</figure>

**Step 4: A normal day**

1. At 05:00, new data loads into Bronze.
2. Silver cleans and merges it, and quarantines failed rows.
3. Gold builds in hidden staging tables.
4. The audit runs, including a reconciliation against the source.
5. If it passes, Gold publishes and the dashboard refreshes before 07:00.

**Step 5: A bad day**

The payment API is down at 05:00. The task retries with exponential backoff, then alerts the team. Gold doesn't publish, so managers still see the last correct numbers. When the API recovers, the team reruns that date, and idempotent writes prevent duplicates.
