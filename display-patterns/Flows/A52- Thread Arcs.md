# A 5.2 Thread Arcs 

## Description

“Threads” are mainly used in online communication systems such as email to describe a group of messages that relate to each other. When a person creates a message to which one or more other persons reply, all these messages form a thread as they relate to each other in respect of a common topic. Hence, a thread is a strictly ordinal structure, meaning that each element has is fixed place in a causal order.

Thread arcs were fi rst described as part of a research paper published for the experimental email client Remail [Kerr 2004]. Its main intention is to give the user better control over the messages in his email folders by sorting them according to their affi liations with a specific thread.

## Required Data 

Use thread arcs to display data that consist of items arranged as ordered elements within the overall data structure while single elements are associated with each other.

## Usage

Arrange the items of your data structure as simple graphic objects in a linear fashion with equal spacing and in their respective order from left to right. For each thread connection between a node and its successor or predecessor, connect them with an arc line.

## Rationale

Threads are often diffi cult to follow or traced back once they grow longer and more complex. The thread arc visualization helps to identify individual threads within the whole data structure. One major aspect to support this ability is the fact that thread arcs aim at keeping the intersection of connection lines at a minimum.

# Related Patterns

A 5.1 Sankey Diagram

A 6.1 Tree Diagram

A 6.2 Tree Map

A 7.1 Diagram Map

A 7.2 Relation Circle

A 7.3 Pearl Necklet