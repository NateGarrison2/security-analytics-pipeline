# Security Analytics ETL Pipeline
An end-to end ETL pipeline that generates simulated SIEM (Security Information and Event Management) data, cleans it, and loads it into a PostgreSQL database for analysis. This project demonstrates practical data engineering concepts, containerization with Docker, and database integration with Python.

## Instructions to Run:

1. **Clone the repository**
```bash
git clone https://github.com/nategarrison2/security-analytics-pipeline.git
cd security-analytics-pipeline
```

2. **Create a local environment file**
```bash
cd etl_pipeline
copy .env.example .env
cd ..
```
> Locate .env.example in /etl_pipeline folder and copy to .env, then navigate back to root directory of project.
> .env is in .gitignore to simulate realistic security practices to avoid leaking information, .env.example is here to allow scripts to run correctly. 

3. **Start Docker Desktop**
> Ensure Docker Desktop is running on your machine.

4. **Build and start the containers:**
```bash
docker-compose up --build
```
> This will build the ETL container, start the PostgreSQL database, generate simulated SIEM data, clean it, and load it into the database.

5. Verify containers are running:
```bash
docker ps
```

6. Access PostgreSQL database:
```bash
docker exec -it siem_postgres psql -U siemuser -d siemd
```

7. Query the loaded SIEM events:
```sql
SELECT * FROM siem_events LIMIT 10;
```
> You should see the first 10 rows of the simulated SIEM data.

8. Stop containers once finished:
```bash
docker-compose down
```
