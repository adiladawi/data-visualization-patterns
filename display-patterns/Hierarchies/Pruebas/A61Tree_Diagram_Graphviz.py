from graphviz import Digraph
from datos import data

d=data('mtcars')
subset1= d[d.cyl==6]
dot = Digraph(comment='Tree Diagram', format='png')
dot.attr('node', shape='box')
dot.node_attr.update(color='lightblue2', style='filled')
dot.node('A', 'Car Distribution by Cylindres')
dot.node('B', '6 cylindres')
j=67;
for i in subset1.index:
    dot.node(unichr(j), str(i))   
    j=j+1

dot.edge('A', 'B')
dot.edges(['BC','BD','BE','BF','BG','BH','BI'])
dot.body.append(r'label = "\n\nTree Diagram"')
dot.body.append('fontsize=20')
dot.render('diagram')