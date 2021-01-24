# fsleads

## Getting Started

### Running the app

First, create a .env file and paste in the following env vars:

```bash
PGUSER=fsleadsuser
PGPASSWORD=admin123
PGDATABASE=fsleadsdb
PGHOST=localhost
PGPORT=5432
DOCKER_PGUSER=postgres
DOCKER_PGDATABASE=postgres
DOCKER_PGPASSWORD=admin123
DOCKER_PGHOST=db
USE_DOCKER_CONFIG=False
LEADS_API_KEY=M6ol0RI47FDANo8wAnBxYw6ZVBbi61whq6wYOKpi
```

Next, run migrations
```bash
python manage.py migrate
```

Finally run the server
```bash
python manage.py runserver
```
