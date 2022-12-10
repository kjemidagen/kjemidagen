# Kjemidagen

Se respektive readmes for frontend og backend

## Caddy (reverse proxy)

Caddy er ikke i docker fordi det ikke fungerte like bra. Det er åpent for å endre.
Må lastes ned.
Kjøres `caddy run` i dev
Kjøres `caddy start` på prod

## Docker

For å kjøre: `docker compose up -d`.
For å "skru av og på igjen" `docker compose restart`
For å "skru av og på igjen" grundig `docker compose build`, så `docker compose up --force-recreate -d`.

## Server

Server hostes på DigitalOcean. Vi bruker [caddy](https://caddyserver.com/) for å holde styr på ssl-sertifikater.

Filene ligger under `/app/kjemidagen/` og må pulles manuelt fra git (fordi det er lettere å feilsøke).

**NB! Husk å bruke `xxx -f docker-compose.prod.yml yyy`**
