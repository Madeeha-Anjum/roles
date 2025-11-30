# Dev Container Setup for Roles Project

## Setting up the Dev Container

1. Add .env file to .devcontainer folder with the following variables:
   ```bash
   ENVIRONMENT="local"
   PG_DB_NAME="rools_db"
   PG_USERNAME="appuser"
   PG_PASSWORD="apppassword"
   PG_HOSTNAME="localhost"
   PG_PORT="5432"
   ```

2. Connect to the dev container using vs code
   - Open the `Ctrl + Shift + P` command palette and type `"Remote-Containers: Open Folder in Container"`

3. View Project
   - Open `http://localhost:8000` for the project
   - Open `http://localhost:8080` for pgAdmin
   - Useful Docker commands:
     - `docker ps` to see running containers
     - `docker logs <container_id>` to see the logs of the containers
     - `docker exec -it <container_id> bash` to open a shell inside the container

4. Setting up the database
   1. To load a .sql file into the database inside the container:
         - step1: open a new terminal not inside the dev container
         - step2:`docker ps`  to get the container name
         - step3:`docker cp ./<LOCATION ON COMPUTER> <CONTAINER NAME>:/tmp/my_script.sql` copy the .sql file to the container
         - step4:Then go into the container in the docker desktop or do `docker exec -it <CONTAINER NAME> sh`
         - step5: `ls -l /tmp/` to see the files in the tmp dir
         - step6: `psql <DB_NAME> <DB_USERNAME>`
         - step7: `\i /tmp/my_script.sql` to load the file in the database
   - **How to create a ".sql file"**
      - `PGPASSWORD=$RDS_PASSWORD pg_dump -U $RDS_USERNAME -h $RDS_HOSTNAME $RDS_DB_NAME > stg.sql`
   - **How to copy db from container to host machine:**
     - `docker cp <container_id>:/var/lib/postgresql/data /path/to/your/local/directory` or use docker-desktop app to download the file

5. How to start the code:
   - `postCreateCommand` in .devcontainer.json will run this command
       - `uvicorn app.main:app --reload`
