# fsleads

## Getting Started

### Running the app

- Ensure you have a postgresql running on your machine. 
    - If postgresql is installed via homebrew, you can run `brew services start postgresql` to fire it up.
    - If you do not have postgresql installed, the easiest way I know is to use homebrew. 
    Run `brew install postgresql` to install postgresql, then run the command above to start it.
- Clone the repository by running: `git clone git@github.com:dhaniboy09/fsleads.git`
- `cd` into the project directory by running: `cd fsleads`
- Copy the env vars below to your clipboard and run `pbpaste > .env` to automatically create a `.env` file and populate it. 
Alternatively, run `touch .env` and manually paste the env vars below in the newly created `.env` file
    ```bash
    PGHOST=localhost
    PGPORT=5432
    DOCKER_PGUSER=postgres
    DOCKER_PGDATABASE=postgres
    DOCKER_PGPASSWORD=admin123
    DOCKER_PGHOST=db
    LEADS_API_KEY=M6ol0RI47FDANo8wAnBxYw6ZVBbi61whq6wYOKpi
    ```
    (.env file contents are only posted here for convenience)
- Run `docker-compose up`
- When all containers are running 
    - Open up a new terminal window. 
    - `cd` into the project directory
    - Run `docker-compose exec fsweb python manage.py migrate --no-input` to run all migrations.
- The API should now be accessible on 0.0.0.0:8000

### Running Tests

- Ensure you're in the project directory
- Run `docker-compose run fsweb python manage.py test` to run all tests

