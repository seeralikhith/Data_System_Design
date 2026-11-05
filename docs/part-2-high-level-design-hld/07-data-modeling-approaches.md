# 7. Data modeling approaches

**In one line:** a modeling approach sets the overall shape of your data, and Kimball is the usual starting point for reporting.

**Think of it like:** organizing a library. The approach decides how books are grouped, so people can find them easily.

<figure markdown="span">
  ![Kimball, Inmon, Data Vault and One Big Table](../assets/diagrams/07-1-light.svg#only-light)
  ![Kimball, Inmon, Data Vault and One Big Table](../assets/diagrams/07-1-dark.svg#only-dark)
  <figcaption>Kimball, Inmon, Data Vault and One Big Table</figcaption>
</figure>

These can work together. For example, Silver can hold a Data Vault model while Gold offers Kimball star schemas.

**Remember:** pick the simplest model that answers your users' questions. Chapter 15 covers the table-level details.
