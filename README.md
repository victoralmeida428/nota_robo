API de Processamento de Notas

Este projeto é uma API construída com FastAPI, projetada para receber imagens de comprovantes (notas), extrair o texto dessas imagens usando Tesseract OCR e, em seguida, processar esse texto com um serviço de IA (DeepSeek).
Funcionalidades

    Upload de Arquivo: Endpoint para carregar um arquivo de imagem.

    Validação de Imagem: Verifica se os arquivos carregados possuem extensões de imagem permitidas.

    Autenticação: Protege o endpoint com uma senha.

    Extração de Texto (OCR): Utiliza a ferramenta Tesseract para extrair texto da imagem do comprovante.

    Processamento com IA: Envia o texto extraído para o serviço DeepSeekServer para processamento.

    Armazenamento Temporário: Salva os arquivos carregados em um diretório temporário para processamento.


Como Começar
Pré-requisitos

    Python 3.10 ou superior

    Tesseract OCR instalado no sistema

    Dependências do Python (FastAPI, Werkzeug, etc.)

Instalação

    Clone o repositório:

    git clone <url-do-repositorio>
    cd <nome-do-repositorio>

    Crie e ative um ambiente virtual (recomendado):

    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

    Instale as dependências:

    pip install fastapi "uvicorn[standard]" python-multipart

Execução

    Inicie o dev FastAPI:

    make run host=localhost port=8000

    Inicie o prod FastAPI:
    docker-compose up --build -d

    A API estará disponível em http://localhost:8000.

Uso da API
Endpoint POST /

Este endpoint é utilizado para carregar a imagem de um comprovante.

    URL: /

    Método: POST

    Corpo da Requisição: multipart/form-data

        file: O arquivo de imagem do comprovante a ser enviado.

        password: A senha para autenticação.

Exemplo de uso com curl:

curl -X POST -F "file=@/caminho/para/seu/comprovante.jpeg" -F "password=sua_senha" http://127.0.0.1:8000/

Resposta

A API retornará um dicionário (dict) com a resposta do serviço DeepSeek após processar o texto extraído do comprovante.