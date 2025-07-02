# **Roadmap: Moodify Project**

This document tracks the development plan for the Moodify data analysis project.

## **Phase 0: Architecture and Preparation (The Foundation)**

**Objective:** Establish the project's foundation, design the architecture, and configure all necessary tools and accounts.

* \[x\] **Architecture Design:** Create a data flow diagram showing all components.  
* \[x\] **Account Setup:**  
  * \[x\] Create GitHub repository.  
  * \[x\] Create Spotify for Developers app and get credentials.  
  * \[x\] Create AWS account (Free Tier).  
* \[x\] **Local Environment Setup:**  
  * \[x\] Install Docker and Docker Compose.  
  * \[x\] Create the initial project folder structure.  
* \[x\] **Initial Cloud Services Setup:**  
  * \[x\] Create an AWS S3 bucket for the Data Lake.  
  * \[x\] Create an AWS IAM user with programmatic access.

## **Phase 1: Authentication (The Gateway)**

**Objective:** Implement the Spotify authentication flow to interact with the API on behalf of the user.

* \[x\] **API Backend:** Initialize the FastAPI project.  
* \[x\] **OAuth 2.0:** Implement the logic for the Spotify authorization flow.  
* \[x\] **Testing:** Create and test the /login and /callback endpoints to successfully retrieve an access token.

## **Phase 2: Data Pipeline v1 \- Ingestion to Data Lake**

**Objective:** Create an automated process to extract data from Spotify and store it in its raw format in our Data Lake (S3).

* \[ \] **Ingestion Script:** Write a Python script to fetch data from the /me/player/recently-played endpoint.  
* \[ \] **S3 Integration:** Modify the script to save the JSON response as a file in the S3 bucket.  
* \[ \] **Serverless Automation:** Deploy the script as an AWS Lambda Function.  
* \[ \] **Scheduling:** Configure Amazon EventBridge to trigger the Lambda function hourly.

## **Phase 3: Data Pipeline v2 \- ETL Process with Airflow**

**Objective:** Transform the raw data from the Data Lake into a clean, structured format within a Data Warehouse (PostgreSQL).

* \[ \] **Data Warehouse Design:** Define the table schema in PostgreSQL (e.g., dim\_tracks, dim\_artists, fact\_plays).  
* \[ \] **Airflow Setup:** Set up a local Airflow environment using Docker Compose.  
* \[ \] **ETL Script:** Write the Python script that extracts from S3, transforms (cleans, enriches with audio features), and loads into PostgreSQL.  
* \[ \] **DAG Creation:** Create an Airflow DAG to orchestrate the ETL script.  
* \[ \] **Pipeline Test:** Run the DAG manually and verify that data appears correctly in PostgreSQL.

## **Phase 4: Service API and Frontend MVP**

**Objective:** Serve the processed data via an API and display it in a basic user interface.

* \[ \] **API Development (FastAPI):**  
  * \[ \] Connect FastAPI to the PostgreSQL database.  
  * \[ \] Create endpoints to query the data (e.g., /api/v1/top\_tracks).  
* \[ \] **Frontend Initialization (Next.js):**  
  * \[ \] Set up a new project with Next.js.  
* \[ \] **Frontend-Backend Integration:**  
  * \[ \] Create pages and components in Next.js that call the FastAPI.  
  * \[ \] Display the first visualizations (lists of top tracks/artists).

## **Phase 5 & Beyond: Advanced Analytics and Deployment**

* \[ \] **New Analytical Endpoints:** Create API endpoints for more complex queries (e.g., mood calendar, valence trends).  
* \[ \] **Advanced Visualizations:** Implement interactive charts using a library like Chart.js, Recharts, or D3.js.  
* \[ \] **Deployment:** Containerize and deploy the full application to the cloud (e.g., AWS ECS/Fargate, Vercel).  
* \[ \] **CI/CD:** Set up a continuous integration/continuous deployment pipeline with GitHub Actions.