from requisicao import Requisicao
# Lista de pedidos a serem processados
pedido = [515481, 742145, 485136, 354648]

# Itera sobre a lista de pedidos e envia requisições POST para cada um
for i in pedido:
    req = Requisicao(f'http://localhost:8080/{i}', 'POST')
    response = req.enviar_requisicao()
    print(response.status_code)