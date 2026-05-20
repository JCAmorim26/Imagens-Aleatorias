import requests
import random
from PIL import Image # Importa a biblioteca Pillow para manipular imagens
import io # Usado para tratar os dados da imagem em memória

# 1. Defina a URL base do seu "servidor" no GitHub Pages
#    Substitua '<seu-usuario>' e '<nome-repositorio>' pelos seus dados
base_url = "https://jcamorim26.github.io/Imagens-Aleatorias/imagens/"

# 2. Crie uma lista com os nomes de todos os arquivos de imagem
#    Se os nomes seguem um padrão, você pode gerá-los facilmente
nomes_das_imagens = [f"Imagem{i}.jpg" for i in range(1, 61)] # Gera de Imagem1.jpg a Imagem60.jpg

# 3. Escolha um nome de arquivo aleatoriamente da lista
imagem_aleatoria = random.choice(nomes_das_imagens)

# 4. Monte a URL completa da imagem escolhida
url_completa = base_url + imagem_aleatoria

print(f"Buscando a imagem: {url_completa}")

try:
    # 5. Faz a solicitação GET para a URL da imagem
    response = requests.get(url_completa)

    # 6. Verifica se a requisição foi bem-sucedida (código 200)
    if response.status_code == 200:
        print("Imagem encontrada com sucesso!")
        
        # 7. A resposta de uma imagem não é JSON, são dados binários brutos.
        #    Usamos 'response.content' para pegar esses dados.
        dados_da_imagem = response.content
        
        # 8. Usa o Pillow para abrir a imagem a partir dos dados em memória
        imagem = Image.open(io.BytesIO(dados_da_imagem))
        
        # 9. Exibe a imagem! O Pillow abrirá o visualizador de imagens padrão do seu SO.
        imagem.show()
            
    else:
        print(f"Falha ao buscar a imagem. Código de status: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro de conexão: {e}")