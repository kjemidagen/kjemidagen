# Kjemidagens API

Alt av endpoints og slik ligger på `localhost:8000/docs`

## Dokumentasjon

FastAPI og SQLModel har begge fantastisk dokumentasjon. Den finner du på [fastapi.tiangolo.com](fastapi.tiangolo.com) og [sqlmodel.tiangolo.com](sqlmodel.tiangolo.com).

## Testing

Testing fungerer ikke lengre etter vi byttet til mongodb. ~~Testing er støttet av pytest og kjøres enkelt ved å kjøre `pytest`.~~

### Admin-kontrollpanel

Få tilgang ved ~~`docker compose exec backend python -m kjemidagen.server_scripts.create_initial_user`. ~~
Ser ut til at dette ^ lager en separat mongo server...
Bruk heller cli fra docker desktop appen.  
![docker cli](./imgs/docker_cli.png =300x)  
Kjør kommandoen `python -m kjemidagen.server_scripts.create_initial_user` for å opprette en bruker.

Brukes til å f.eks. opprette den første admin-brukeren.

### Refresh-token-rullering

Auth-systemet er jeg redd kan være noe porøst fordi det rullerer refresh tokens. Det vil si at hver gang en refresh token brukes blir den invalidert og brukeren får en ny. Dette betyr muligens at hvis noen velger feil øyeblikk å spamklikke på så mister de den eneste valide tokenen og må logge inn på nytt. Jeg skal prøve å designe frontend for å unngå dette, men hvis brukere rapporterer å bli utelåst er nok dette grunnen.

## PGSQL Command line

Komme til cli: `docker-compose exec mongodb bash -it` eller docker desktop cli.
For å koble til: `mongo -u <brukernavn> -p <passord>`. Resten får du google.
