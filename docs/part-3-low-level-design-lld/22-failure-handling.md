# 22. Failure handling

**In one line:** retries fix temporary problems, while permanent ones need a quarantine or a person.

**Think of it like:** a phone call. If the line is busy, you try again later. If the number is wrong, redialing won't help.

<figure markdown="span">
  ![Deciding how to handle a failure](../assets/diagrams/22-1-light.svg#only-light)
  ![Deciding how to handle a failure](../assets/diagrams/22-1-dark.svg#only-dark)
  <figcaption>Deciding how to handle a failure</figcaption>
</figure>

<figure markdown="span">
  ![Exponential backoff, dead-letter queues and other safeguards](../assets/diagrams/22-2-light.svg#only-light)
  ![Exponential backoff, dead-letter queues and other safeguards](../assets/diagrams/22-2-dark.svg#only-dark)
  <figcaption>Exponential backoff, dead-letter queues and other safeguards</figcaption>
</figure>

If a source file is simply late, wait up to a timeout and then alert the owner.

**Remember:** a failure should be noticed by you before it is noticed by your users.
