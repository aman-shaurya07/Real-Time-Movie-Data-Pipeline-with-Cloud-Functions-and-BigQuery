# BigQuery-based Data Pipeline Project

## Overview
This project demonstrates a real-time data pipeline using:
- **Google Cloud Pub/Sub**: For message streaming.
- **Cloud Functions**: For event-driven processing.
- **Google BigQuery**: For data storage and analytics.

## Architecture
![Architecture](diagrams/architecture.png)

1. **Data Flow**:
    - Files uploaded to **Google Cloud Storage (GCS)** trigger Pub/Sub notifications.
    - Pub/Sub messages trigger a **Cloud Function** to process the data.
    - Processed data is loaded into a **BigQuery** table for analytics.

## Prerequisites
- Google Cloud account.
- gcloud CLI installed.

## Setup Instructions

### Step 1: Clone the Repository
    ```bash
    git clone https://github.com/aman-shaurya07/Real-Time-Movie-Data-Pipeline-with-Cloud-Functions-and-BigQuery.git
    ```
    ```bash
    cd Real-Time-Movie-Data-Pipeline-with-Cloud-Functions-and-BigQuery
    ```


### Step 2: Create Pub/Sub Topic and Subscription
1. **Create Topic**:
    ```bash
    gcloud pubsub topics create <TOPIC_NAME>
    ```
2. **Create Subscription**:
    ```bash
    gcloud pubsub subscriptions create <SUBSCRIPTION_NAME> --topic=<TOPIC_NAME>
    ```

### Step 3: Set Up GCS Bucket and Notifications
1. **Create a GCS Bucket**:
    ```bash
    gcloud storage buckets create gs://<BUCKET_NAME> --location=us-central1
    ```
2. **Set Up Pub/Sub Notifications**:
    ```bash
    gcloud storage buckets notifications create \
        --topic=<TOPIC_NAME> \
        --event-types=OBJECT_FINALIZE \
        gs://<BUCKET_NAME>
    ```

### Step 4: Deploy Cloud Function
1. **Write Cloud Function Code**:
    The Cloud Function code is in `main.py`.

2. **Deploy Function**:
    ```bash
    gcloud functions deploy <FUNCTION_NAME> \
        --runtime=python310 \
        --trigger-topic=<TOPIC_NAME> \
        --entry-point=entry_function \
        --region=us-central1
    ```

### Step 5: Create BigQuery Table
1. **Create Dataset**:
    ```bash
    bq --location=us-central1 mk -d <DATASET_NAME>
    ```
2. **Create Table**:
    ```bash
    bq mk \
        --table \
        <DATASET_NAME>.<TABLE_NAME> \
        src/bigquery/schema.json
    ```

## Running the Project
1. Upload a file to the **GCS bucket**.
2. Monitor **BigQuery** for new data.

## Key Components
- **Google Cloud Storage (GCS)**: Raw data storage.
- **Pub/Sub**: Event-driven messaging.
- **Cloud Functions**: Data transformation.
- **BigQuery**: Data analytics and storage.

## Diagram
Refer to the `diagrams/architecture.png` file for an architectural overview.
