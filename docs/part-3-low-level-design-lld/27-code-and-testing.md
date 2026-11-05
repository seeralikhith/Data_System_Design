# 27. Code and testing

**In one line:** treat pipelines like software, so changes are safe to make.

**Think of it like:** a restaurant's standard recipes. Everyone follows the same written steps, changes are reviewed, and dishes are tasted before serving.

<figure markdown="span">
  ![Modular, config-driven pipelines and audit columns](../assets/diagrams/27-1-light.svg#only-light)
  ![Modular, config-driven pipelines and audit columns](../assets/diagrams/27-1-dark.svg#only-dark)
  <figcaption>Modular, config-driven pipelines and audit columns</figcaption>
</figure>

**Version control** with Git tracks every change. The next picture shows how a change reaches production.

<figure markdown="span">
  ![From code change to production, with five kinds of test](../assets/diagrams/27-2-light.svg#only-light)
  ![From code change to production, with five kinds of test](../assets/diagrams/27-2-dark.svg#only-dark)
  <figcaption>From code change to production, with five kinds of test</figcaption>
</figure>

**Remember:** if a change can't be tested and reviewed before it reaches production, it isn't ready.
