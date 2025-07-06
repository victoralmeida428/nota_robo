# Use uma imagem base oficial do Python
FROM python:3.10-slim

# Instala o Tesseract OCR e outras dependências do sistema
# O Tesseract é necessário para a funcionalidade de OCR da aplicação
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-por \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho dentro do contêiner
WORKDIR /opt/nota

# Copia o arquivo de dependências para o diretório de trabalho
COPY ./requirements.txt /app/requirements.txt

# Instala as dependências do Python definidas no requirements.txt
# --no-cache-dir: Não armazena o cache do pip para manter a imagem menor
# --upgrade: Garante que o pip está atualizado
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copia o código-fonte da sua aplicação para o diretório de trabalho
COPY ./src /app/src

# Expõe a porta 8000 para permitir a comunicação com a API fora do contêiner
EXPOSE 8000
