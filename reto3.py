#Ejercicio 3
productos = [
    {
        "id": 123,
        "nombre": "libreta",
        "precio": 12.500,
        "id_cat": 1
    },
    {
        "id": 345,
        "nombre": "Jabon",
        "precio": 10.500,
        "id_cat": 2
    }
]
categorias = [
    {
        "id_cat": 1,
        "nombre": "Utiles escolares"
    },
    {
        "id_cat": 2,
        "nombre": "Aseo"
    }
]

diccionario_3 = []

for x in productos:
    for categoria in categorias:
        if x["id_cat"] == categoria["id_cat"]:
            producto_con_categoria = {
                "id": x["id"],
                "nombre": x["nombre"],
                "Categoria": categoria["nombre"]
            }
            diccionario_3.append(producto_con_categoria)

print("Diccionario nuevo")

for i in diccionario_3:
    print(i)