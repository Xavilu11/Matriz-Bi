# Crear el diccionario de información ficticia
informacion_personal = {
    "nombre": "Jhon Rambo",
    "edad": 45,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}
# Acceder y modificar el valor de ciudad
informacion_personal["ciudad"] = "Quito"
# Agregar una nueva clave para "profesion"
informacion_personal["profesion_secundaria"] = "Comando"
# Verificar existencia de telefono y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0953478019"
# Eliminar la edad
if "edad" in informacion_personal:
    del informacion_personal["edad"]
# Imprimir
print(informacion_personal)