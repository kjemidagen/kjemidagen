# Kjemidagen

Se respektive readmes for frontend og backend

## Docker

For å kjøre: `docker-compose -f <filnavn> up`.
For å "skru av og på igjen" `docker-compose -f <filnavn> down -v`.
default filnavn er `docker-compose.yml` og i det tilfellet kan `-f <filnavn>` droppes.

### Filene

https://docs.docker.com/storage/bind-mounts/#use-a-bind-mount-with-compose

`docker-compose.db.yml` postgres-database og pgadmin. Intended for rask utvikling av backend.
`docker-compose.backend.yml` backendserver og postgres-database. Intended for rask utvikling av frontend.
`docker-compose.dev.yml` frontend, backendserver og postgres-database. Intended for utvikling av hele stacken.
`docker-compose.yml` production-containeren.
