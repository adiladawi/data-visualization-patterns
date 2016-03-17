# A 1.2: BUBBLE CHART


## Description

Bubble charts share certain similarities with scatterplots: They are drawn into a Cartesian coordinate system and provide information about the correlation between quantitative attributes as represented by the two coordinate axes.
But in opposition to a scatterplot, the raw data of a bubble chart does not consist of an array of anonymous pairs of variates that only become meaningful in the context of a larger group of items. Instead, each dataset has a unique label assigned, usually a plain-text name to identify the corresponding object in the coordinate grid (Behrens, 2008).

While two numerical variables can be derived from its x and y coordinates in the representation, the remaining data attributes are displayed by the bubbles’ graphic features, including object size, fill color, brightness etc. Their choice depends on the format of the raw data. While quantitative values can be displayed by the position of the bubbles within the coordinate grid, object size or brightness, qualitative (or categorical) values are usually distinguished by the object’s fill color. These considerations are crucial to the correct use of the bubble chart and refer to Jacques Bertin’s theory of graphic variables (Bertin, 1973).


## Required Data

Use a bubble chart to display tabular data. Each dataset is identifiable by a unique label, and consists of a an array of variables. At least two of these variables must be quantitative.
The other attributes can be of any scale of measurement  it doesn’t matter whether they represent quantitative or qualitative values (Behrens, 2008).


## Usage

Create a two-dimensional Cartesian coordinate system. Choose two of the quantitative variables from your data table, and apply them to the axes. For each row in the table, draw a circle with its center at the corresponding coordinates. Determine which and how many graphic variables you need to express the remaining variables from your table, and apply them to each bubble accordingly.The most common graphic attributes here are the bubble’s size or, for non-numeric variables, fill color and brightness.

When you use the bubble size to express a value, keep in mind the two competing concepts of how to translate the represented attribute into a geometric value. The problem here is that a one-dimensional value is represented by a two-dimensional graphical object. The “traditional“ way to perform this task is to draw the circle’s diameter proportionally to the numerical value. As a result, an object that doubles in diameter (in width and height, that is) appears four times as big - if the value triples, the area even grows to the ninefold size! This is why the technique is drawing much criticism for a long time and is often cited as a prime example for the visual distortion of facts (Bertin,  1973) (Hartmann, 2006 ).


## Rationale

The Bubble Chart pattern is a convenient alternative to pseudo-3D diagrams that aim to display data of three variables in two-dimensional environments such as a book page or a computer screen. In some cases, the bubble chart can even bear more than three variables to display. Set in a conventional Cartesian coordinate system, it appears familiar to the user while extending the possibilities of standard scatterplots.(Behrens, 2008).


## Related Patterns

![](imagenes/A12Bubble_Chart.png)


----------
