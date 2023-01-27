FROM postgres

ENV POSTGRES_DB movies
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD Ensai-2023-GL

COPY init.sql /docker-entrypoint-initdb.d/