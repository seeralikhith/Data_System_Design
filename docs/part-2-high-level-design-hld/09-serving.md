# 9. Serving

**In one line:** the serving layer delivers data in the form each user or application needs.

**Think of it like:** a restaurant kitchen. The same food can be served at a table, packed for takeaway or sent for delivery.

<figure markdown="span">
  ![Six serving patterns and who uses them](../assets/diagrams/09-1-light.svg#only-light)
  ![Six serving patterns and who uses them](../assets/diagrams/09-1-dark.svg#only-dark)
  <figcaption>Six serving patterns and who uses them</figcaption>
</figure>

**Concurrency** means many users querying at once, which often limits dashboard speed.

**Remember:** analytical tables are built to scan many rows. Apps that need one row in milliseconds usually need a separate store.
