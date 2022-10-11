import requests

sample = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
]

def generate_matrix(sample, coluna, linha, estado):
    sample[coluna][linha] = estado
    return sample

endpoint = "http://127.0.0.1:5000/matrix-status"
r = requests.get(endpoint)
content = r.json()

for enum, entry in enumerate(content):
    coluna = int(entry.get("coluna")) - 1
    linha = int(entry.get('linha')) - 1
    estado = int(entry.get('estado'))
    sample = generate_matrix(sample, linha, coluna, estado)

print(sample)