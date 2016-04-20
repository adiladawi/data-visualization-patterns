# A 5.1 Sankey Diagram 

## Description

The sankey diagram visualizes complex systems of material or energy flows. It describes isolated systems by means of their input and output flows, and describes the proportional magnitudes of the single flows as they contribute to the entire system. The input portions of such a system are depicted as arrows leading into a main flow (usually flowing from left to right), while outputs are drawn as arrows leading away from the system. The proportional magnitude of each contribution is displayed through the width of the respective arrow.

## Required Data 

Use the sankey diagram to display quantitative data that are characterized by a sequential nature where the main focus is on the proportional amount of each data class. You want to describe an isolated system on the basis of input and output components and your main objective is the amount of “material” that goes into the system from different sources, or leaves it in different ways.

## Usage

Create a graphic object to represent a flow, e.g. a big arrow pointing from left to right across the display, at a width that correlates to the total amount of the system. Draw a set of branches leading to the system, and a set that leads away from it, with one branch for each contribution to the system, and at a proportional width. If applicable, arrange the branches in the causal order in which they contribute to the system.

## Rationale

Sankey diagrams clearly depict the proportional amount a flow channel adds to a whole system. Similarly to pie or bar charts, a graphic element’s width is directly linked to the one-dimensional data value it represents, making the major contributors instantly visible.

# Related Patterns

A 2.3 Stacked Area Chart

A 4.1 Simple Pie Chart

A 5.2 Thread Arcs