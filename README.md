# fsleads

## Getting Started

### Running the app

- Ensure you have a postgresql running on your machine. If postgresql is installed via homebrew, you can run `brew services start postgresql` to fire it up.
- `cd` into the project directory, 
- Run `touch .env`
- Copy and paste the following into the newly created `.env` file
    ```bash
    PGHOST=localhost
    PGPORT=5432
    DOCKER_PGUSER=postgres
    DOCKER_PGDATABASE=postgres
    DOCKER_PGPASSWORD=admin123
    DOCKER_PGHOST=db
    LEADS_API_KEY=M6ol0RI47FDANo8wAnBxYw6ZVBbi61whq6wYOKpi
    ```
    (.env file contents are only posted here for convenience. For real projects an env variable management package e.g. `helm` will be used)
- Run `docker-compose up`
- When all containers are running, open up a new terminal window, `cd` into the project directory and run `docker-compose exec fsweb python manage.py migrate --no-input`, which will run all migrations
- The API should now be accessible on 0.0.0.0:8000

### Running Tests

- Ensure you're in the project directory
- Run `docker-compose run fsweb python manage.py test` to run all tests

