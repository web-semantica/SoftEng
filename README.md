# FGA-Ontology

Ontologia de disciplinas do curso de Engenharia de Software da FGA

#### Para acessar a aplicação:

```
python3 fga_ontology/manage.py runserver 0.0.0.0:8000
Navegador: http://0.0.0.0:8000/
```

#### Para acessar o banco de triplas:

```
sudo docker-compose up -d
Navegador: http://localhost:8001/openrdf-workbench/
```

#### Tutorial de uso

1. Primeiro suba a aplicação e o banco de triplas como mencionado acima

2. Crie um novo repositorio chamado **softeng** e aperte next duas vezes no banco de triplas

![img1](https://user-images.githubusercontent.com/14116020/41176876-6dcba296-6b38-11e8-988f-e9e5a2bd3329.png)

3. Execute o comando para popular o banco de triplas

```
make populate
```

4. Execute o comando ```make query``` para testar se o banco foi populado

5. Execute suas queries e armazene suas queries dentro do banco de queries da aplicação.

```
Executar query: http://0.0.0.0:8000/
Criar e listar queries: http://0.0.0.0:8000/queries/
Editar e deletar queries: http://0.0.0.0:8000/queires/<query_id>/details/
```
