# Security Analytics ETL Pipeline
This project is an end-to-end ETL pipeline that generates, processes, and stores simulated SIEM (Security Information and Event Management) data. It demonstrates key data engineering and data science skills, including:

- Data generation and simulation: Creates realistic security event logs using Python and Pandas.

- Data cleaning and transformation: Normalizes, filters, and aggregates data to extract actionable insights.

- Database integration: Loads processed data into PostgreSQL and queries it for analysis.

- Containerization and reproducibility: Uses Docker to isolate and run the pipeline consistently across environments.

This project showcases practical experience in Python-based ETL workflows, data pipeline automation, and working with structured data in both code and databases, all of which are core skills for data science and data engineering roles.

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

3. **Run data generation and data cleaning scripts to create .csv files in /data/**
```bash
cd etl_pipeline
python data_generation_script.py
python etl_pipeline.py
```

4. **Ensure Docker Desktop is installed and open on your machine**

5. **Build and start the containers:**
```bash
docker-compose up -d --build
```
> This will build the ETL container, start the PostgreSQL database, generate simulated SIEM data, clean it, and load it into the database. This shows some behind-the-scenes of each of the python scripts running and the PostgreSQL database being created/loaded into. Process takes a minute or two.

6. **Once build finishes, verify containers are running:**
```bash
docker ps
```

7. Access PostgreSQL database:
```bash
docker exec -it siem_postgres psql -U siemuser -d siemdb
```
> IMPORTANT: Docker image takes a while to fully build and create the database. If the docker exec command does not work, give it a minute and try again.

8. Query the loaded SIEM events:
```sql
SELECT * FROM siem_events LIMIT 10;
```
> You should see the first 10 rows of the simulated SIEM data.

9. Stop containers once finished:
```bash
docker-compose down
```

## Example Data Section:
### Running data_generation_script.py:
<img width="1074" height="395" alt="image" src="https://github.com/user-attachments/assets/18bae5b9-6d65-4229-b2b4-79c48751bf0c" />

### Running etl_pipeline.py:
<img width="1262" height="951" alt="image" src="https://github.com/user-attachments/assets/5e60c810-849e-451a-a179-e4c7dffba741" />

### Building Docker container:
<img width="894" height="146" alt="image" src="https://github.com/user-attachments/assets/1f925327-138d-4448-bca4-4be21bdb51e1" />
<img width="1657" height="728" alt="image" src="https://github.com/user-attachments/assets/9fa143ef-42d6-4d5d-b18e-0703aa69716d" />

### Running PostgreSQL in Docker container:
<img width="1336" height="383" alt="image" src="https://github.com/user-attachments/assets/d4de3a9a-eb22-4278-8565-0960b5926658" />
