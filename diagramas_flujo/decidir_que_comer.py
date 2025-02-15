from graphviz import Digraph

# Crear un diagrama de flujo
dot = Digraph("Decidir_Que_Comer", format="png")

# Inicio
dot.node("Inicio", "Inicio", shape="oval")

# Preguntas iniciales
dot.node("P1", "¿Cuánta hambre tienes? (mucha/media/poca)", shape="parallelogram")
dot.node("P2", "¿Cuánto tiempo tienes en minutos?", shape="parallelogram")
dot.node("P3", "¿Cuánto dinero tienes? (mucho/poco/nada)", shape="parallelogram")

# Decisiones
dot.node("H1", "Hambre = 'mucha'", shape="diamond")
dot.node("H2", "Hambre = 'media'", shape="diamond")
dot.node("H3", "Hambre = 'poca'", shape="diamond")

dot.node("D1", "Dinero = 'mucho'", shape="diamond")
dot.node("D2", "Dinero = 'poco'", shape="diamond")

# Opciones de comida
dot.node("O1", "Come hamburguesa, pizza o comida completa", shape="rectangle")
dot.node("O2", "Come burrito, tacos o menú económico", shape="rectangle")
dot.node("O3", "Prepara algo en casa", shape="rectangle")
dot.node("O4", "Come fruta, yogurt o galletas", shape="rectangle")
dot.node("O5", "Haz ensalada, sándwich o sopa ligera", shape="rectangle")
dot.node("O6", "Bebe agua o un té", shape="rectangle")

# Fin
dot.node("Fin", "Fin", shape="oval")

# Conexiones
dot.edge("Inicio", "P1")
dot.edge("P1", "P2")
dot.edge("P2", "P3")
dot.edge("P3", "H1")

# Ramas de decisión
dot.edge("H1", "D1", label="Sí")
dot.edge("D1", "O1", label="Sí")
dot.edge("D1", "D2", label="No")
dot.edge("D2", "O2", label="Sí")
dot.edge("D2", "O3", label="No")

dot.edge("H1", "H2", label="No")
dot.edge("H2", "P2")
dot.edge("P2", "O4", label="< 15 min")
dot.edge("P2", "O5", label=">= 15 min")

dot.edge("H2", "H3", label="No")
dot.edge("H3", "O6")

dot.edge("O1", "Fin")
dot.edge("O2", "Fin")
dot.edge("O3", "Fin")
dot.edge("O4", "Fin")
dot.edge("O5", "Fin")
dot.edge("O6", "Fin")

# Renderizar la imagen
diagram_path = "../diagramas/decidir_que_comer"
dot.render(diagram_path)
#
# # Devolver la ruta de la imagen generada
# diagram_path + ".png"
