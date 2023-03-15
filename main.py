import json
#importo els dos arxius Python de la carpeta A
from Integrant_A.car import car
from Integrant_A.university2 import university
#faig les llistes de les dues clases i poso les dades de cada car i cada universitat
cars = [
    car("Peugeot", "406", "Vermell", "1998"),
    car("Ferrari", "812", "Negre", "2016"),
    car("Lamborghini", "Murcielago", "Groc", "2012"),
    car("Seat", "Ibiza", "Blanc", "2000"),
    car("Citroen", "C3", "Blau", "2022"),
]

universities = [
    university("Harvard","Espanya",500000,"Medicina",300,"No"),
    university("Cambridge","Italia",10,"Ingenieria",1000,"Si"),
    university("Universitat de Madrid", "Francia", 12932, "Matematiques", 30000, "Si"),
    university("UAB", "Alemanya", 10932, "Fisica", 10000, "Si"),
    university("Universitat Europea", "Libano", 100002, "Criminologia", 2500, "No"),
]
#convirteixo les dues llistes en diccionaris
cars_list = [c.to_dict() for c in cars]
universities_list = [u.to_dict() for u in universities]
#guardo les llistes en un objecte contenidor
data = {"cars":cars_list, "universities": universities_list}
#Guardo el contenidor en un arxiu .json
with open ("json_API/A.json", "w") as file:
    json.dump(data, file)