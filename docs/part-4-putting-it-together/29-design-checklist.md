# 29. Design checklist

Tick these off for any new data system. The number in brackets is the chapter to read.

**Before you design**

- [ ]  Sources, users and questions are listed (3)
- [ ]  Freshness and compliance needs are agreed (3)
- [ ]  Data size is estimated (3)

**HLD**

- [ ]  Batch, micro-batch or streaming is chosen (4)
- [ ]  Each source has an ingestion method (5)
- [ ]  Storage and layers are chosen (6)
- [ ]  A modeling approach is chosen (7)
- [ ]  Orchestration tool and triggers are chosen (8)
- [ ]  Each user has a way to get data (9)
- [ ]  Owners and access rules are defined (10)
- [ ]  RPO and RTO are agreed (11)
- [ ]  There is a plan for growth (12)
- [ ]  SLOs and SLAs are written down (13)
- [ ]  Deployment and cost controls are set (14)

**LLD**

- [ ]  Every table has a grain and a key (15)
- [ ]  Partitioning or clustering is planned (16)
- [ ]  Loads handle deletes and schema changes (17)
- [ ]  Every write is idempotent (18)
- [ ]  Large joins and data skew are reviewed (19)
- [ ]  Streaming jobs have watermarks and checkpoints (20)
- [ ]  Each quality check has a failure action (21)
- [ ]  Retries and timeouts are set (22)
- [ ]  Jobs can be backfilled by date (23)
- [ ]  Key queries are fast enough (24)
- [ ]  Every KPI has a definition and an owner (25)
- [ ]  Masks, filters and secrets are in place (26)
- [ ]  Tests run automatically (27)

**Before launch**

- [ ]  A backfill has been tested
- [ ]  Recovery from a failure has been tested
- [ ]  Alerts reach the right owner
- [ ]  Users confirm the numbers look right
