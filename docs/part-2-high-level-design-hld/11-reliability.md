# 11. Reliability

**In one line:** a reliable system expects failures and makes recovery quick and safe.

**Think of it like:** writing a long document. RPO is how much work you can lose since your last save. RTO is how long you can wait before you can type again.

<figure markdown="span">
  ![RPO and RTO on a timeline](../assets/diagrams/11-1-light.svg#only-light)
  ![RPO and RTO on a timeline](../assets/diagrams/11-1-dark.svg#only-dark)
  <figcaption>RPO and RTO on a timeline</figcaption>
</figure>

For example, an RPO of 1 hour and an RTO of 4 hours means losing at most 1 hour of data and being back within 4 hours.

<figure markdown="span">
  ![Eight reliability terms](../assets/diagrams/11-2-light.svg#only-light)
  ![Eight reliability terms](../assets/diagrams/11-2-dark.svg#only-dark)
  <figcaption>Eight reliability terms</figcaption>
</figure>

**Remember:** keep raw data, make pipelines safe to rerun (chapter 18), and test your backups, because an untested backup is only a hope.
