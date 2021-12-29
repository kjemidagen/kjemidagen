# Kjemidagens API

Alt av endpoints og slik ligger på `localhost:8000/docs`

## Dokumentasjon

FastAPI og SQLModel har begge fantastisk dokumentasjon. Den finner du på [fastapi.tiangolo.com](fastapi.tiangolo.com) og [sqlmodel.tiangolo.com](sqlmodel.tiangolo.com).

## Alembic

todo

## Testing

Testing er støttet av pytest og kjøres enkelt ved å kjøre `pytest`.

## Porøse systemer

### Refresh-token-rullering

Auth-systemet er jeg redd kan være noe porøst fordi det rullerer refresh tokens. Det vil si at hver gang en refresh token brukes blir den invalidert og brukeren får en ny. Dette betyr muligens at hvis noen velger feil øyeblikk å spamklikke på så mister de den eneste valide tokenen og må logge inn på nytt. Jeg skal prøve å designe frontend for å unngå dette, men hvis brukere rapporterer å bli utelåst er nok dette grunnen.
