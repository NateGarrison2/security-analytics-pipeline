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
copy .env.example .env
```
> .env is in .gitignore to simulate realistic security practices to avoid leaking information, .env.example is here for user to copy to allow scripts that use .env to run correctly. 

3. **Start Docker Desktop**
> Ensure Docker Desktop is running on your machine.

4. **Build and start the containers:**
```bash
docker-compose up -d --build
```
> This will build the ETL container, start the PostgreSQL database, generate simulated SIEM data, clean it, and load it into the database. This shows some behind-the-scenes of each of the python scripts running and the PostgreSQL database being created/loaded into. Process takes a minute or two.

5. Once build finishes, verify containers are running:
```bash
docker ps
```

6. Access PostgreSQL database:
```bash
docker exec -it siem_postgres psql -U siemuser -d siemdb
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

## Example Data Section:
**Running data_generation_script.py:**
<img width="1074" height="395" alt="image" src="https://github.com/user-attachments/assets/18bae5b9-6d65-4229-b2b4-79c48751bf0c" />

**Running etl_pipeline.py:**
<img width="1262" height="951" alt="image" src="https://github.com/user-attachments/assets/5e60c810-849e-451a-a179-e4c7dffba741" />

**Building Docker container:**
<img width="894" height="146" alt="image" src="https://github.com/user-attachments/assets/1f925327-138d-4448-bca4-4be21bdb51e1" />
<img width="1657" height="728" alt="image" src="https://github.com/user-attachments/assets/9fa143ef-42d6-4d5d-b18e-0703aa69716d" />

**Running PostgreSQL in Docker container:**
<img width="1336" height="383" alt="image" src="https://github.com/user-attachments/assets/d4de3a9a-eb22-4278-8565-0960b5926658" />
