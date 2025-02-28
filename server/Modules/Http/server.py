from aiohttp import web

pedidos = [123456, 7891011]
pedidoSerie = [{}]

#Faça o que tem que fazer com a solicitação GET na raiz
async def handle(request):
    try:
        pedidoAtual = pedidos[0]
        return web.Response(text=pedidoAtual)
    except IndexError:
        return web.Response(text=None, status=400)

#Faça o que tem que fazer numa solicitação POST
async def add(request):
    #Recupera na URL as variaveis enviadas, se não houver, recupera None (funciona igualmente para GET)
    pedido = request.match_info.get('pedido', None)
    if pedido:
        pedidos.append(pedido)
        return web.Response(status=200)
    else:
        return web.Response(status=400)
    
#Faça o que tem que fazer numa solicitação POST com mais de um parametro
async def addSerie(request):
    pdd = request.match_info.get('pedido', None)
    serie = request.match_info.get('serie', None)
    if pdd and serie:
        pedidoSerie[0][pdd] = serie
        print(pedidoSerie)
        return web.Response(status=200)
    else:
        return web.Response(status=400)

#Salva o servidor na variavel app
app = web.Application()

#Adiciona as rotas monitoradas
app.add_routes([
    web.get('/', handle),
    web.post('/{pedido}', add),
    web.post('/automate/{pedido}/{serie}', addSerie)
])

#Inicia o Server
if __name__ == '__main__':
    web.run_app(app)
