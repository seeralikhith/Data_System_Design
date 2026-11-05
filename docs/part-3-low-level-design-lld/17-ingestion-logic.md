# 17. Ingestion logic

**In one line:** good ingestion loads only what changed, remembers where it stopped and survives changes at the source.

**Think of it like:** reading a long book. A **full load** starts from page one every time. An **incremental load** uses a bookmark and reads only what is new.

<figure markdown="span">
  ![Incremental load using a high-watermark](../assets/diagrams/17-1-light.svg#only-light)
  ![Incremental load using a high-watermark](../assets/diagrams/17-1-dark.svg#only-dark)
  <figcaption>Incremental load using a high-watermark</figcaption>
</figure>

A **high-watermark** is that bookmark, usually the latest timestamp already loaded. Rows can arrive late, so many teams re-read a small overlap and remove duplicates afterward. A watermark can't see hard deletes, which is one reason to use CDC.

<figure markdown="span">
  ![CDC events, checkpoints, pagination, rate limits and ingestion metadata](../assets/diagrams/17-2-light.svg#only-light)
  ![CDC events, checkpoints, pagination, rate limits and ingestion metadata](../assets/diagrams/17-2-dark.svg#only-dark)
  <figcaption>CDC events, checkpoints, pagination, rate limits and ingestion metadata</figcaption>
</figure>

A delete event either removes the row or marks it deleted, which is called a **soft delete**.

**Schema evolution** is how a pipeline handles changes in source structure:

<figure markdown="span">
  ![Schema evolution · green is safe, red needs review](../assets/diagrams/17-3-light.svg#only-light)
  ![Schema evolution · green is safe, red needs review](../assets/diagrams/17-3-dark.svg#only-dark)
  <figcaption>Schema evolution · green is safe, red needs review</figcaption>
</figure>

**Remember:** assume sources will change without warning, and design for it.
