from Modules.Http.requisicao import Requisicao

req = Requisicao(f'http://localhost:8080/', 'GET')
response = req.enviar_requisicao()
print(response)