import requests
from pprint import pprint

#Get

resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
pprint(resultado_get.json())

#Get com id - Obter recurso unico
resultado_get_com_id = requests.get('https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_get_com_id.json())

#Pos - Criar um novo recurso
nova_tarefa = {
    'completed': False,
    'title': 'Lavar o carro',
    'userId': 1
}
resultado_post = requests.post('http://jsonplaceholder.typicode.com/todos', nova_tarefa)
pprint(resultado_post.json())

#Post
nova_tarefa = {'completed': False,
               'title': 'Lavar o carro',
               'userId': 1
               }
resultado_put = requests.put(
    'https://jsonplaceholder.typicode.com/todo/2', nova_tarefa
)
pprint(resultado_post.json())

#Delete
resultado_delete = requests.delete(
    'https://jsonplaceholder.typicode.com/todos/2'
)
pprint(resultado_delete.json())

