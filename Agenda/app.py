import web

urls = (
    '/', 'Index',
    '/insertar', 'InsertarContacto',
    '/lista', 'ListaContactos',
    '/detalles', 'DetallesContacto',
    '/editar', 'EditarContacto',
    '/borrar', 'BorrarContacto'
)

app = web.application(urls, globals())
render = web.template.render('views')

# --- BASE DE DATOS SIMULADA EN MEMORIA ---
contactos_db = []
siguiente_id = 1

# Función auxiliar para buscar un contacto usando su ID
def obtener_contacto(id_buscado):
    for contacto in contactos_db:
        if str(contacto.id) == str(id_buscado):
            return contacto
    return None

# --- CLASES CONTROLADORAS ---

class Index:
    def GET(self):
        return render.index()

class InsertarContacto:
    def GET(self):
        return render.insertar_contacto()

    def POST(self):
        global siguiente_id
        
        formulario = web.input()
        
        nuevo_contacto = web.storage(
            id=siguiente_id,
            nombre=formulario.nombre,
            primer_apellido=formulario.primer_apellido,
            segundo_apellido=formulario.segundo_apellido,
            telefono=formulario.telefono,
            email=formulario.email
        )
        
        contactos_db.append(nuevo_contacto) 
        
        siguiente_id += 1                   
        
        raise web.seeother('/lista')

class ListaContactos:
    def GET(self):
        # Le enviamos la lista completa al HTML
        return render.lista_contactos(contactos_db)

class DetallesContacto:
    def GET(self):
        # Obtenemos el ID de la URL (ej. /detalles?id=1)
        parametros = web.input(id=None)
        contacto_encontrado = obtener_contacto(parametros.id)
        return render.detalles_contacto(contacto_encontrado)

class EditarContacto:
    def GET(self):
        parametros = web.input(id=None)
        contacto_encontrado = obtener_contacto(parametros.id)
        return render.editar_contacto(contacto_encontrado)

    def POST(self):
        formulario = web.input()
        contacto_a_editar = obtener_contacto(formulario.id_contacto)
        
        # Si existe, actualizamos sus valores con lo que viene del formulario
        if contacto_a_editar:
            contacto_a_editar.nombre = formulario.nombre
            contacto_a_editar.primer_apellido = formulario.primer_apellido
            contacto_a_editar.segundo_apellido = formulario.segundo_apellido
            contacto_a_editar.telefono = formulario.telefono
            contacto_a_editar.email = formulario.email
            
        raise web.seeother('/lista')

class BorrarContacto:
    def GET(self):
        parametros = web.input(id=None)
        contacto_encontrado = obtener_contacto(parametros.id)
        return render.borrar_contacto(contacto_encontrado)

    def POST(self):
        formulario = web.input()
        contacto_a_borrar = obtener_contacto(formulario.id_confirm)
        
        # Si existe en la lista, lo eliminamos
        if contacto_a_borrar in contactos_db:
            contactos_db.remove(contacto_a_borrar)
            
        raise web.seeother('/lista')

if __name__ == "__main__":
    app.run()