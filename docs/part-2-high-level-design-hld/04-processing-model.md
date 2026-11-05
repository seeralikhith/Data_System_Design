# 4. Processing model

**In one line:** the processing model decides how often data moves, so choose the slowest option that still meets the need.

**Think of it like:** sending messages. Batch is a daily mail delivery, micro-batch is a courier every few minutes, and streaming is a phone call.

<figure markdown="span">
  ![Batch, micro-batch and streaming over the same events](../assets/diagrams/04-1-light.svg#only-light)
  ![Batch, micro-batch and streaming over the same events](../assets/diagrams/04-1-dark.svg#only-dark)
  <figcaption>Batch, micro-batch and streaming over the same events</figcaption>
</figure>

<figure markdown="span">
  ![Comparing batch, micro-batch and streaming](../assets/diagrams/04-2-light.svg#only-light)
  ![Comparing batch, micro-batch and streaming](../assets/diagrams/04-2-dark.svg#only-dark)
  <figcaption>Comparing batch, micro-batch and streaming</figcaption>
</figure>

**Lambda architecture** and **Kappa architecture** are two classic ways to combine these models:

<figure markdown="span">
  ![Lambda vs. Kappa architecture](../assets/diagrams/04-3-light.svg#only-light)
  ![Lambda vs. Kappa architecture](../assets/diagrams/04-3-dark.svg#only-dark)
  <figcaption>Lambda vs. Kappa architecture</figcaption>
</figure>

Many modern platforms use one engine for both batch and streaming, so the same logic can serve both.

**Remember:** a dashboard read once each morning does not need streaming.
