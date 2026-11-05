# 23. Job configuration

**In one line:** job configuration is the set of rules that makes each pipeline run safe and repeatable.

**Think of it like:** setting up a recurring alarm. You choose when it rings, how often it repeats and who gets woken.

<figure markdown="span">
  ![Job settings, and how a backfill uses them](../assets/diagrams/23-1-light.svg#only-light)
  ![Job settings, and how a backfill uses them](../assets/diagrams/23-1-dark.svg#only-dark)
  <figcaption>Job settings, and how a backfill uses them</figcaption>
</figure>

**Remember:** a job that can't take a date as a parameter is very hard to backfill.
