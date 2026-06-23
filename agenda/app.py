import web

# Definimos las rutas basadas en tus bocetos
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

class Index:
    def GET(self):
        return render.index()

class InsertarContacto:
    def GET(self):
        return render.insertar_contacto()

class ListaContactos:
    def GET(self):
        return render.lista_contactos()

class DetallesContacto:
    def GET(self):
        return render.detalles_contacto()

class EditarContacto:
    def GET(self):
        return render.editar_contacto()

class BorrarContacto:
    def GET(self):
        return render.borrar_contacto()

if __name__ == "__main__":
    app.run()