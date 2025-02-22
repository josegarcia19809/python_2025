# lista con 10 ciudades, incluyendo algunas repetidas:
ciudades = ["Madrid", "Buenos Aires", "Ciudad de México", "Londres", "París",
            "Madrid", "Nueva York", "Ciudad de México", "Berlín", "Tokio"]
print(ciudades)
print("-" * 100)

# convertir la lista en un conjunto eliminando las duplicadas
ciudades_unicas = set(ciudades)
print(ciudades_unicas)
print("-" * 100)

# convertir nuevamente a una lista
ciudades_lista = list(ciudades_unicas)
print(ciudades_lista)
