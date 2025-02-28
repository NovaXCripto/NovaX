from aiohttp import web
from requests import Request

#Faça o que tem que fazer com a solicitação GET na raiz
async def handle(request):
    try:
        return web.json_response({"message": "Hello World"})
    except IndexError:
        return web.Response(text=None, status=400)

async def login(request: Request):
    try:
        data = await request.json()
        return web.json_response({"message": f"Usuairo logado {data['username']}"})
    except Exception as e:
        return web.Response(text=str(e), status=400)

async def cadastro(request):
    try:
        data = await request.json()
        return web.json_response({"message": f"Usuário criado {data['username']}"})
    except Exception as e:
        return web.Response(text=str(e), status=400)
    


#Salva o servidor na variavel app
app = web.Application()

#Adiciona as rotas monitoradas
app.add_routes([
    web.get('/', handle),
    web.post('/login', login),
    web.post('/cadastro', cadastro),
])

#Inicia o Server
if __name__ == '__main__':
    web.run_app(app, host="0.0.0.0", port=5000)
