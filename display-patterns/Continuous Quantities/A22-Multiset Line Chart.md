# A 2.2: Multiset Line Chart

## Description 

In most cases, a line chart is used to display the behavior of one single value over an interval. However, there are situations in which it is important to let the user directly compare several variables and their development over the same interval. Instead of drawing several charts next to each other with each one displaying one single graph, create a single coordinate system that fosters the requirements of each variable within the same system. The Multiple Line Chart pattern incorporates several simple line charts within the same coordinate base.

## Required Data 

Use this type of diagram to display several quantitative variables and their development over a shared regular interval, for instance time. The variables you want to display may express different quantities, so that the y-axis might adopt more than one scale. But they all share the same reference variable, and here should lie within the same interval. If not, you have to choose appropriate interval boundaries to foster all variables you want to display.

## Usage

Create a two-dimensional Cartesian coordinate system. Label and subdivide the x-axis according to the variable expressing the interval, while the y-axis carries the labels for those variables you want to display. If your dataset contains variables of different scale and unit, attach several scales to the y-axis, and make them clearly distinguishable. For each data item, draw a point at the corresponding locations in the coordinate pane. Connect points that belong to the same set with each other through a continuous line from left to right. The result of this process is a set of lines or curves that reflects an approximation of the dependent variables’ developments over the examined interval. The smaller the distance between two neighboring points, the higher the graph’s accuracy.	

## Rationale

Obviously, the advantages of the simple line chart apply to the multivariate extension as well. Furthermore, the user is given a powerful tool to directly compare different variables within the same chart. And last but not least, combining several variables within one single chart can save you a substantial amount of space compared to drawing a separate diagram for each variable.

# Related Patterns

A 2.1 Simple Line Chart
A 2.3 Stacked Area Chart