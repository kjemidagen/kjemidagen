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

## Server

Server hostes på DigitalOcean. Vi bruker [caddy](https://caddyserver.com/) for å holde styr på ssl-sertifikater.

TODO: Fiks slik at ssr har tilgang til backend

### Hjelp, det brenner på dass

Innloggingsinfo bør du ha. Logg inn på digitalocean for å se ip-adressen eller ssh til
Alle filene ligger under `/github-actions-runner/_work/kjemidagen/kjemidagen`. Der kan du endre .env-filer og manuelt skru av og på docker services.

# Kjemidagen frontend i Sveltekit

## Development

For at man ikke skal få feilmeldinger i IDE-en, bør man installere dependencies lokalt.

Kjør følgende kommando i `frontend`-mappen:

```bash
npm install
```

## Building

Building gjøres med docker, se Readme i foreldre-mappe.

## Sikkerhet

Les om sikkerhet på Auth0 sine sider. Vi bruker ikke Auth0, men vi bruker prinsippene. [Auth0 docs](https://auth0.com/docs/secure/tokens/refresh-tokens/refresh-token-rotation)
