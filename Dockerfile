# Use uma imagem base do Ubuntu com Python instalado
FROM ubuntu:22.04

WORKDIR /app

# Instale Python e outras dependências APT
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3.11-venv \
    python3-pip \
    libnss3 \
    libxss1 \
    libappindicator3-1 \
    libgbm-dev \
    libc6 \
    libasound2 \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Crie um link simbólico para o Python 3.11
RUN ln -s /usr/bin/python3.11 /usr/bin/python

# Copie o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

RUN mkdir -p /app/media && chmod -R 777 /app/media

# Crie e ative um ambiente virtual
RUN python -m venv /opt/venv --copies
ENV PATH="/opt/venv/bin:$PATH"

# Instale as dependências do Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copie o restante do código da aplicação para o diretório de trabalho
COPY . .

# Execute migrações e colete arquivos estáticos
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

# Exponha a porta que a aplicação usará
EXPOSE 8000 5555


# Comando para iniciar o servidor Gunicorn
CMD ["sh", "-c", "\
    gunicorn guanxi_app.wsgi:application --access-logfile - & \
    celery -A guanxi_app worker -l info & \
    celery -A guanxi_app flower --basic_auth='root@root.com:#guanxi2025' & \
    wait"]
