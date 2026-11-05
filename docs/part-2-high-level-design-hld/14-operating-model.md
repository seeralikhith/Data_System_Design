# 14. Operating model

**In one line:** the operating model decides who owns data and how changes safely reach production.

**Think of it like:** a company kitchen. One central kitchen can cook for everyone, or each department can run its own kitchen under shared food safety rules.

<figure markdown="span">
  ![Central data team vs. data mesh](../assets/diagrams/14-1-light.svg#only-light)
  ![Central data team vs. data mesh](../assets/diagrams/14-1-dark.svg#only-dark)
  <figcaption>Central data team vs. data mesh</figcaption>
</figure>

A central team is simple to start and keeps standards consistent, but it can become a bottleneck. A data mesh scales across many teams, but needs capable domain teams and strong shared rules. Many companies use a mix of both.

<figure markdown="span">
  ![Data mesh principles, data contracts, CI/CD, IaC and FinOps](../assets/diagrams/14-2-light.svg#only-light)
  ![Data mesh principles, data contracts, CI/CD, IaC and FinOps](../assets/diagrams/14-2-dark.svg#only-dark)
  <figcaption>Data mesh principles, data contracts, CI/CD, IaC and FinOps</figcaption>
</figure>

**Remember:** every dataset needs a named owner, whichever model you choose.
