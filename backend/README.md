# Kjemidagens API

Alt av endpoints og slik ligger på `kjemidagen.localhost/docs`

## Dokumentasjon

FastAPI og SQLModel har begge fantastisk dokumentasjon. Den finner du på [fastapi.tiangolo.com](fastapi.tiangolo.com) og [sqlmodel.tiangolo.com](sqlmodel.tiangolo.com).

## Testing

Testing er ikke implementert. ~~Testing er støttet av pytest og kjøres enkelt ved å kjøre `pytest`.~~

### Admin-kontrollpanel

Bruk heller cli fra docker desktop appen.  
![docker cli](./imgs/docker_cli.png =300x)  
Kjør kommandoen `python admin.py create-initial-user` for å opprette en bruker.

Brukes til å opprette den første admin-brukeren.

### Refresh-token-rullering

Auth-systemet er jeg redd kan være noe porøst fordi det rullerer refresh tokens. Det vil si at hver gang en refresh token brukes blir den invalidert og brukeren får en ny. Dette betyr muligens at hvis noen velger feil øyeblikk å spamklikke på så mister de den eneste valide tokenen og må logge inn på nytt. Jeg skal prøve å designe frontend for å unngå dette, men hvis brukere rapporterer å bli utelåst er nok dette grunnen.

## Mariadb Command line

Komme til cli: `docker-compose exec db bash -it` eller docker desktop cli -> terminal -> `bash`.
For å koble til: `mariadb -u <brukernavn> -p`. Resten får du google.
