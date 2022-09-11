# Kjemidagen

Se respektive readmes for frontend og backend

<!-- ## Reverse proxy

For at applikasjonen skal fungere på localhost må du installere caddy lokalt.  -->

## Caddy (reverse proxy)

Caddy er ikke i docker fordi det ikke fungerte like bra. Det er åpent for å endre.
Må lastes ned.
Kjøres `caddy run` i dev
Kjøres `caddy start` på prod

## Docker

For å kjøre: `docker compose up -d`.
For å "skru av og på igjen" `docker compose restart`
For å "skru av og på igjen" grundig `docker compose build`, så `docker compose up --force-recreate -d`.

## Filewatcher

Fordi file watching og docker ikke spiller så godt på lag på windows har jeg laget et hjelpeskript i python.  
Kjør det med `python run_docker.py` og ikke vær redd for å endre det. Det eneste det gjør er å kjøre `docker compose restart <service>` når filer endres i den tilhørende mappen.

Min foretrukne workflow er å bruke run_docker bare på backend også kjøre frontend med `npm run dev -- --port 3001`. Da får jeg en raskere feedback-loop, fordi frontend container tar for en eller annen grunn ~ 10 sek å stoppe.

## Server

Server hostes på DigitalOcean. Vi bruker [caddy](https://caddyserver.com/) for å holde styr på ssl-sertifikater.

TODO: Fiks slik at ssr har tilgang til backend
