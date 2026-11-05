# 20. Streaming

**In one line:** streaming logic must handle data that arrives late, out of order or more than once.

**Think of it like:** posted letters. A letter written on Monday may arrive on Friday, and letters don't always arrive in the order they were written.

**Event time** is when something actually happened. **Processing time** is when the system handled it. If a phone goes offline, a 10:00 sale may arrive at 10:20, so sales reports should group by event time.

A **watermark** sets how long to wait for late events. A longer wait is more complete, but results come later and use more memory.

<figure markdown="span">
  ![How a watermark handles late events](../assets/diagrams/20-1-light.svg#only-light)
  ![How a watermark handles late events](../assets/diagrams/20-1-dark.svg#only-dark)
  <figcaption>How a watermark handles late events</figcaption>
</figure>

**Windows** split a never-ending stream into time-based groups:

<figure markdown="span">
  ![Three window types over the same events](../assets/diagrams/20-2-light.svg#only-light)
  ![Three window types over the same events](../assets/diagrams/20-2-dark.svg#only-dark)
  <figcaption>Three window types over the same events</figcaption>
</figure>

Use **tumbling** windows for sales per 5 minutes, **sliding** windows for sales in the last 10 minutes, and **session** windows for one user's website visit.

<figure markdown="span">
  ![Topics, partitions, offsets and consumer groups](../assets/diagrams/20-3-light.svg#only-light)
  ![Topics, partitions, offsets and consumer groups](../assets/diagrams/20-3-dark.svg#only-dark)
  <figcaption>Topics, partitions, offsets and consumer groups</figcaption>
</figure>

**Three more terms:**

- **State:** what a stream remembers between events, such as running totals. It needs checkpoints and an expiry rule.
- **Backpressure:** data arriving faster than it can be processed.
- **Consumer lag:** how far a reader has fallen behind the newest event.

<figure markdown="span">
  ![At-most-once, at-least-once and exactly-once delivery](../assets/diagrams/20-4-light.svg#only-light)
  ![At-most-once, at-least-once and exactly-once delivery](../assets/diagrams/20-4-dark.svg#only-dark)
  <figcaption>At-most-once, at-least-once and exactly-once delivery</figcaption>
</figure>

**Remember:** at-least-once delivery with idempotent writes is a common, practical choice, because duplicates then cause no harm.
