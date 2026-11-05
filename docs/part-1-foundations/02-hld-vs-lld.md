# 2. HLD vs. LLD

**In one line:** high-level design (HLD) decides what parts the system has, and low-level design (LLD) decides how each part works.

**Think of it like:** building a house. HLD is the floor plan. LLD is the wiring, pipes and materials.

<figure markdown="span">
  ![HLD and LLD for an orders pipeline](../assets/diagrams/02-1-light.svg#only-light)
  ![HLD and LLD for an orders pipeline](../assets/diagrams/02-1-dark.svg#only-dark)
  <figcaption>HLD and LLD for an orders pipeline</figcaption>
</figure>

<figure markdown="span">
  ![From need to HLD choice to LLD work](../assets/diagrams/02-2-light.svg#only-light)
  ![From need to HLD choice to LLD work](../assets/diagrams/02-2-dark.svg#only-dark)
  <figcaption>From need to HLD choice to LLD work</figcaption>
</figure>

**A simple design order:**

1. Agree what people need.
2. Draw the HLD and note each trade-off.
3. Write the LLD, starting with the riskiest part.
4. Build a small version, learn from it, and improve the design.

**Remember:** HLD mistakes are expensive to fix later, so spend time on them early.
