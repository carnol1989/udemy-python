ruta_nombre_archivo_agenda_digital = "C:\\Cursos\\python\\agenda_digital_fichero.txt"

agenda_digital = {
    "Carlos Nole": {
        "nombre": "Carlos",
        "apellido": "Nole",
        "direccion": "Piura",
        "email": "carlos.nole@jupyter.com",
        "telefono": "978834576"

    },
    "Wilson Neira": {
        "nombre": "Wilson",
        "apellido": "Neira",
        "direccion": "26 de Octubre",
        "email": "wilson.neira@nttdata.com",
        "telefono": "975434576"

    },
    "Cristhian Davila": {
        "nombre": "Cristhian",
        "apellido": "Davila",
        "direccion": "Castilla",
        "email": "cristhian.davila@everis.com",
        "telefono": "975434512"

    }
}

def guardar_agenda_digital(ruta_nombre_archivo, agenda_digital_guardar):
    print("Guardar agenda digital en disco...")
    archivo_agenda_digital = open(ruta_nombre_archivo, "w")
    archivo_agenda_digital.write(str(agenda_digital_guardar))
    archivo_agenda_digital.close()

def leer_agenda_digital(ruta_nombre_archivo):
    print("Leer agenda digital desde el disco...")
    archivo_agenda_digital = open(ruta_nombre_archivo, "r")
    contenido_agenda_digital = archivo_agenda_digital.read()
    print(contenido_agenda_digital)
    archivo_agenda_digital.close()
    return contenido_agenda_digital

def solicitar_contacto_agenda():
    print("Solicitar datos de nuevo contacto...")
    nombre = input("Ingresar nombre: ")
    apellido = input("Ingresar apellido: ")
    direccion = input("Ingresar direccion: ")
    email = input("Ingresar email: ")
    telefono = input("Ingresar telefono: ")

    nombre_completo = nombre + " " + apellido

    nuevo_contacto = {
        "nombre": nombre,
        "apellido": apellido,
        "direccion": direccion,
        "email": email,
        "telefono": telefono
    }

    return nombre_completo, nuevo_contacto

def crear_contacto(agenda_digital, nuevo_contacto_agregar, nombre_completo_clave, ruta_nombre_archivo):
    print("Crear nuevo contacto...")
    agenda_digital[nombre_completo_clave] = nuevo_contacto_agregar
    guardar_agenda_digital(ruta_nombre_archivo, agenda_digital)

def obtener_datos_contacto(ruta_nombre_archivo):
    print("Obtener datos de contacto...")
    nombre_completo_buscar = input("Ingresar nombre completo del contacto a consultar: ")
    informacion_agenda_digital = leer_agenda_digital(ruta_nombre_archivo)
    agenda_digital_return = eval(informacion_agenda_digital)
    datos_contacto = agenda_digital_return.get(nombre_completo_buscar)
    print(datos_contacto)
    print("Direccion:", datos_contacto["direccion"])
    print("Email:", datos_contacto["email"])
    print("Telefono:", datos_contacto["telefono"])

guardar_agenda_digital(ruta_nombre_archivo_agenda_digital, agenda_digital)
informacion_agenda_digital = leer_agenda_digital(ruta_nombre_archivo_agenda_digital)
agenda_digital_return = eval(informacion_agenda_digital)
nombre_completo_clave, nuevo_contacto_agregar = solicitar_contacto_agenda()
crear_contacto(agenda_digital_return, nuevo_contacto_agregar, nombre_completo_clave, ruta_nombre_archivo_agenda_digital)

informacion_agenda_digital = leer_agenda_digital(ruta_nombre_archivo_agenda_digital)
agenda_digital_return = eval(informacion_agenda_digital)
obtener_datos_contacto(ruta_nombre_archivo_agenda_digital)