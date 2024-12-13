import pymongo
import sys

try:
  client = pymongo.MongoClient(<Tu Cadena de Conexión de Atlas>)
  
except pymongo.errors.ConfigurationError:
  print("Oe causa, hubo un error con la conexión. ¿Estás seguro que la dirección de Atlas es correcta?")
  sys.exit(1)

db = client.miBaseDeDatos

mi_coleccion = db["recetas"]

documentos_recetas = [{ "nombre": "ceviche", "ingredientes": ["pescado", "limón", "cebolla", "ají", "culantro"], "tiempo_prep": 30 },
                    { "nombre": "lomo saltado", "ingredientes": ["lomo", "cebolla", "tomate", "sillao", "papa", "arroz"], "tiempo_prep": 45 },
                    { "nombre": "ají de gallina", "ingredientes": ["gallina", "ají amarillo", "pan", "leche", "queso", "nueces"], "tiempo_prep": 60 },
                    { "nombre": "causa rellena", "ingredientes": ["papa amarilla", "limón", "ají amarillo", "pollo", "mayonesa", "aguacate"], "tiempo_prep": 50 }]

try:
  mi_coleccion.drop()  

except pymongo.errors.OperationFailure:
  print("Oe causa, parece que hay un problema con la autenticación. ¿Estás seguro que tu usuario y contraseña son correctos?")
  sys.exit(1)

try: 
 resultado = mi_coleccion.insert_many(documentos_recetas)

except pymongo.errors.OperationFailure:
  print("Oe causa, parece que no tienes permiso para escribir en la base de datos. ¿Estás seguro que tu usuario tiene los permisos necesarios?")
  sys.exit(1)
else:
  cantidad_insertada = len(resultado.inserted_ids)
  print("Chévere, he insertado %x documentos." %(cantidad_insertada))

  print("\n")

resultado = mi_coleccion.find()

if resultado:    
  for doc in resultado:
    mi_receta = doc['nombre']
    cantidad_ingredientes = len(doc['ingredientes'])
    tiempo_prep = doc['tiempo_prep']
    print("El %s tiene %x ingredientes y se demora %x minutos en prepararse." %(mi_receta, cantidad_ingredientes, tiempo_prep))
    
else:
  print("No encontré ningún documento, causa.")

print("\n")

mi_doc = mi_coleccion.find_one({"ingredientes": "papa amarilla"})

if mi_doc is not None:
  print("Manya, encontré una receta que usa papa amarilla:")
  print(mi_doc)
else:
  print("Pucha, no encontré ninguna receta que use papa amarilla como ingrediente.")
print("\n")

mi_doc = mi_coleccion.find_one_and_update({"ingredientes": "papa amarilla"}, {"$set": { "tiempo_prep": 65 }}, new=True)
if mi_doc is not None:
  print("Mira pe, aquí está la receta actualizada:")
  print(mi_doc)
else:
  print("Pucha, no encontré ninguna receta que use papa amarilla como ingrediente.")
print("\n")

mi_resultado = mi_coleccion.delete_many({ "$or": [{ "nombre": "ceviche" }, { "nombre": "causa rellena" }]})
print("Bacán, eliminé %x registros." %(mi_resultado.deleted_count))
print("\n")

print("Chau causa, nos vemos. Atentamente, Farley Viveros")
