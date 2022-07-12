# Kjemidagen

Se respektive readmes for frontend og backend

## Docker

For å kjøre: `docker-compose up`.
For å "skru av og på igjen" grundig `docker-compose down -v`, så `up`.

## Filewatcher

Fordi file watching og docker ikke spiller så godt på lag på windows har jeg laget et hjelpeskript i python.  
Kjør det med `python run_docker.py` og ikke vær redd for å endre det. Det eneste det gjør er å kjørr `docker compose restart <service>` når filer endres i den tilhørende mappen.

## Server

Server hostes på DigitalOcean. Vi bruker [caddy](https://caddyserver.com/) for å holde styr på ssl-sertifikater.
