from flask import Flask

app = Flask(__name__)

@app.route('/')

def eventos():
    events = [
    {
        'id': 1,
        'title': 'Conferencia de Python',
        'slug': 'conferencia-python',
        'description': 'Descripción del evento...',
        'date': '2025-09-15',
        'time': '14:00',
        'location': 'Auditorio Principal',
        'category': 'Tecnología',
        'max_attendees': 50,
        'attendees': [
            {'name': 'Juan Pérez', 'email': 'juan@example.com'}
        ],
        'featured': True
    }
]

categorias = ['Tecnologia','Academico','Cultural','Deportivo', 'Social']

def mostrar_todo():
    pass 

#Ruta para mostrar un evento especifico
@app.route('/event/<slug>/')

def mostrar_evento(slug):
    pass

#Agregar asistente a un evento ya programado
@app.route('/event/<slug>/register/')
def b():
    pass

#Ruta para el formulario de un nuevo evento 
@app.route('/admin/event/')
def a ():
    pass

#Eventos por categoria 
@app.route('/events/category/<category>/')
def c ():
    pass