import aiohttp
import asyncio
from dataclasses import dataclass, field

@dataclass
class Requisicao:
    url: str
    metodo: str
    isAsync: bool = False
    dados: dict = field(default_factory=dict)
    headers: dict = field(default_factory=dict)

    # Método para enviar requisições de forma assíncrona
    async def __enviar_requisicao_async(self):
        async with aiohttp.ClientSession() as session:
            if self.metodo == 'GET':
                async with session.get(self.url, params=self.dados, headers=self.headers) as resposta:
                    return await resposta.json()
            elif self.metodo == 'POST':
                async with session.post(self.url, data=self.dados, headers=self.headers) as resposta:
                    return await resposta.json()
            elif self.metodo == 'PUT':
                async with session.put(self.url, data=self.dados, headers=self.headers) as resposta:
                    return await resposta.json()
            elif self.metodo == 'DELETE':
                async with session.delete(self.url, headers=self.headers) as resposta:
                    return await resposta.json()

    # Método para enviar requisições de forma síncrona
    def __enviar_requisicao_sync(self):
        import requests
        if self.metodo == 'GET':
            return requests.get(self.url, params=self.dados, headers=self.headers)
        elif self.metodo == 'POST':
            return requests.post(self.url, data=self.dados, headers=self.headers)
        elif self.metodo == 'PUT':
            return requests.put(self.url, data=self.dados, headers=self.headers)
        elif self.metodo == 'DELETE':
            return requests.delete(self.url, headers=self.headers)

    # Método para enviar requisições de acordo com o tipo de requisição
    def enviar_requisicao(self):
        if self.isAsync:
            return asyncio.run(self.__enviar_requisicao_async())
        else:
            return self.__enviar_requisicao_sync()