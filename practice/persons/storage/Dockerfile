FROM postgres:14-alpine
MAINTAINER jussiar

ARG USER_NAME
ARG USER_PASSWORD

ENV POSTGRES_PASSWORD=jussiar
ENV POSTGRES_USER=jussiar
ENV POSTGRES_DB=persons

RUN apk add --no-cache tzdata
EXPOSE 9000
ENV TZ=Europe/London
