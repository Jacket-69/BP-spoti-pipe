# Moodify: Your Personal Spotify Data Analyzer

![Project Banner](https://placehold.co/1200x300/1DB954/FFFFFF?text=Moodify&font=raleway)

A data-driven web application that analyzes your Spotify listening habits to reveal your musical moods and patterns. This project is built with a complete data engineering pipeline, from data ingestion to a user-facing API.

---

## ✨ Key Features

-   **Authentication:** Secure login using the Spotify OAuth 2.0 flow.
-   **Data Ingestion:** Automated pipeline to fetch recently played tracks periodically.
-   **ETL Processing:** Transformation and enrichment of raw data, including audio features (`valence`, `energy`, `danceability`).
-   **Data Warehousing:** Clean, structured data stored in a PostgreSQL database, ready for analysis.
-   **API Layer:** A fast and robust API built with FastAPI to serve the processed data.
-   **Dynamic Frontend:** An interactive dashboard (built with Next.js) to visualize your listening statistics.

---

## 🛠️ Tech Stack & Architecture

This project utilizes a modern, scalable architecture designed to handle data efficiently.

-   **Frontend:** Next.js (React)
-   **Backend (API):** FastAPI (Python)
-   **Data Ingestion:** AWS Lambda
-   **Data Lake:** AWS S3
-   **ETL Orchestration:** Apache Airflow
-   **Data Warehouse:** PostgreSQL
-   **Infrastructure:** Docker

*You can see the detailed architecture diagram [here](./architecture-diagram.png).*

---

## 🚀 Getting Started

To get the backend running locally, follow these steps.

### Prerequisites

-   Python 3.9+
-   Docker
-   A Spotify Developer account and credentials (`CLIENT_ID`, `CLIENT_SECRET`).

### Backend Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Jacket-69/BP-spoti-pipe.git
    cd BP-spoti-pipe
    ```

2.  **Set up the backend environment:**
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Create the environment file:**
    Create a `.env` file inside the `/backend` folder and add your Spotify credentials:
    ```env
    SPOTIFY_CLIENT_ID="YOUR_CLIENT_ID"
    SPOTIFY_CLIENT_SECRET="YOUR_CLIENT_SECRET"
    ```

4.  **Run the server:**
    ```bash
    uvicorn main:app --reload --host 127.0.0.1
    ```
    The API will be available at `http://127.0.0.1:8000`.

---


## 🗺️ Roadmap

The complete project roadmap is detailed in our `ROADMAP.md` file. We are currently on **Phase 2: Data Pipeline v1 - Ingestion to Data Lake**.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

