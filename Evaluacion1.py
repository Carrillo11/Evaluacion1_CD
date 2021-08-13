import Conexion as net
import os

db=net.client["Evaluacion1"]
col=db["CE"]

while True:

     os.system("csl")

     
     print("1. Ver los registros.")
     print("2. Agregar registro.")
     print("3. Actualizar registro")
     print("4. Eliminar Registro")
    
     op=input("Accion a realizar: ")

     if op=="1":
         for i in col.find():
             print(i)
         print("Presione enter para continuar")
         input()

     elif op=="2":
         id=int(input("Ingrese el id del CE: "))
         nombre=input("Ingrese el nombre del CE: ")
         departamento=input("Ingrese el departamento al que pertece el CE: ")
         municipio=input("Ingrese el municipio del CE: ")
         dict={ "_id":id, "Nombre":nombre, "Departamento":departamento, "Municipio":municipio}
         ingreso=col.insert_one(dict)
         print("Registro realizado precione enter.")
         input()

     elif op=="3":
         ing_id=col.find_one(int(input("Ingrese el id: ")))

         print("1. Nombre de CE.")
         print("2. Departamento de CE.")
         print("3. Municipio de CE.")

         op1=input("Atrubuto a modificar: ")
         
         if op1=="1":
            mnombre=input("Ingrese el nombre: ")
            mod=col.update({"_id" : ing_id["_id"]},{"$set":{"Nombre":mnombre}})
            print("Registro actualizado")
            input()

         if op1=="2":
             mdepartamento=input("Ingrese el departamento: ")
             mod=col.update({"_id" : ing_id["_id"]},{"$set":{"Departamento":mdepartamento}})
             print("Registro actualizado")
             input()

         if op1=="3":
             mmunicipio=input("Ingrese el minicipio: ")
             mod=col.update({"_id" : ing_id["_id"]},{"$set":{"Municipio":mmunicipio}})
             print("Registro actualizado")
             input()

     elif op=="4":
         ing_id=int(input("Ingrese id del CE: "))
         eliminar=col.delete_one({"_id" : ing_id})
         print("Registro eliminado precione enter.")
         input()
     
     elif op=="5":
         print("Saliendo del sistema")
         input()
         break
        
     else:
         print("Opcion incorrecta")
         input()
         continue