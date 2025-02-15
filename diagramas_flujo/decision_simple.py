from graphviz import Digraph

dot = Digraph()
dot.node('A', 'Inicio')
dot.node('B', 'Decisión')
dot.node('C', 'Resultado')

dot.edge('A', 'B')
dot.edge('B', 'C', label='Sí')
dot.edge('B', 'A', label='No')

dot.render('../diagramas/diagrama', format='png', view=True)