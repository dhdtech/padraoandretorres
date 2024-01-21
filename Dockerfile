FROM python:3.12

ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends build-essential 
RUN apt-get install -y curl gdal-bin libpq-dev postgresql-client  gettext
RUN rm -rf /var/lib/apt/lists/* 

# COPY ./requirements/ /requirements
COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

RUN pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

RUN mkdir -p padraoandretorres

COPY ./padraoandretorres padraoandretorres

COPY entrypoint.sh /padraoandretorres

RUN chmod +x /padraoandretorres/entrypoint.sh

WORKDIR /padraoandretorres

EXPOSE 10000

CMD [ "/padraoandretorres/entrypoint.sh" ]
