# Las tuplas se pueden ocupar como keys en diccionarios

ubicaciones = {
    (35.6, 39.6): "Tokio Office",
    (40.7, 74.0): "New York Office",
    (37.7, 122.4): "San Francisco Office"
}

print("Mostrar ubicación de Oficina de San Francisco")
print(ubicaciones[(37.7, 122.4)])
