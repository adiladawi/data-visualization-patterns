

# A 6.2: TREE MAP


## Description

A tree map is an alternative representation of a tree structure and was proposed by Ben Shneiderman the early 1990s. While a conventional family tree displays the single elements and their family relations to each other, it doesn’t provide any information about these elements’ quantitative properties. The tree map arranges its items according to their position within the hierarchy and displays the magnitude of each items through
a visual property such as color or size (Behrens, 2008). 


## Required Data 

Use a tree map to display a list of items where each item is defined by one or more
properties. Several items from this list can be grouped to categories. More than three properties per item are not recommended for the sake of readability (Behrens, 2008).


## Usage

Sort the list containing your data by category. Each category now represents a first-level node of the tree structure. Each dataset within these categories are in turn child nodes of their respective categories. Create a rectangular structure as the container of your tree map. The resulting box represents the root node of your treemap. Divide this box into smaller boxes, one for each child node of the tree root. Split each box according to the number of child nodes and so on. As a result, you’ll get a graphic structure of nested boxes, with the smallest boxes representing the single data elements. Now adjust the elements according to the values they represent: Choose color as the graphic variables for one property, box size for the second, and so on (Behrens, 2008).


## Rationale


As mentioned above, the tree map does not invent a completely new way of structuring data. Instead, it provides an alternative way of accessing, reading and understanding complex data structures at a glance. Tree maps heavily rely on the concept of preattentive variables as its elements can vary in size, color or other graphic properties depending on their respective values. Thus, tree maps are a preferred method of displaying tree structures when the user needs an instant understanding about extreme values among the nodes(Behrens, 2008).


# Related Patterns

* A 5.2 Thread Arcs
* A 6.1 Tree Diagram 