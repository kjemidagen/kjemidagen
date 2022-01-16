# Kjemidagens API

Alt av endpoints og slik ligger på `localhost:8000/docs`

## Dokumentasjon

FastAPI og SQLModel har begge fantastisk dokumentasjon. Den finner du på [fastapi.tiangolo.com](fastapi.tiangolo.com) og [sqlmodel.tiangolo.com](sqlmodel.tiangolo.com).

## Alembic

Generere migration: `docker-compose -f <docker-compose[.filen som du bruker].yml> exec backend alembic revision --autogenerate -m <informativ tekst>`
NBNB! Husk å lese over at de stemmer. Spesielt må `kjemidagen.sql_uuid.UUID` må skrives om til `sqlalchemy.dialects.postgresql.UUID`.
Migrere: `docker-compose -f <docker-compose[.filen som du bruker].yml> exec backend alembic upgrade head`

## Testing

Testing er støttet av pytest og kjøres enkelt ved å kjøre `pytest`.

## Porøse systemer

### Refresh-token-rullering

Auth-systemet er jeg redd kan være noe porøst fordi det rullerer refresh tokens. Det vil si at hver gang en refresh token brukes blir den invalidert og brukeren får en ny. Dette betyr muligens at hvis noen velger feil øyeblikk å spamklikke på så mister de den eneste valide tokenen og må logge inn på nytt. Jeg skal prøve å designe frontend for å unngå dette, men hvis brukere rapporterer å bli utelåst er nok dette grunnen.

## PGSQL Command line

Komme til cli: `docker-compose -f docker-compose.backend.yml exec postgres bash -it` eller docker desktop cli.
For å koble til: `psql --username <brukernavn> --dbname kjemidagen`. Resten får du google.
