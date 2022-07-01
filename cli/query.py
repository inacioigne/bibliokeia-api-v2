import httpx

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {"query": "Pesquisa"}

response = httpx.post('http://localhost:8983/solr/acervo/query', json=data)