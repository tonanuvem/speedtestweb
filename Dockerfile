FROM python:3.14-alpine

# Instala dependências do sistema necessárias para o speedtest-cli funcionar 
RUN apk add --no-cache gcc musl-dev libffi-dev python3-dev

# Cria diretórios
RUN mkdir -p /app/templates

# Copia os arquivos
COPY app.py /app/
COPY templates/index.html /app/templates/

# Define o diretório de trabalho
WORKDIR /app

# Instala as dependências do Python
RUN pip install --no-cache-dir speedtest-cli flask

# Expõe a porta 5000
EXPOSE 5000

# Define o comando de inicialização do container
ENTRYPOINT ["python", "app.py"]
