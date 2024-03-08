import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact')
def get_list():
    return { 'name' : 'Platzi'}

@app.get('/pagina', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Página en servidor</h1>
        <p>Esta es mi primera página HTML con Python en un servidor </p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()