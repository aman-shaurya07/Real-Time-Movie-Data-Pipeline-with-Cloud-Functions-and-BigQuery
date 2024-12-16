# BigQuery-based Data Pipeline Project

## Overview
This project demonstrates a real-time data pipeline using:
- **Google Cloud Pub/Sub**: For message streaming.
- **Cloud Functions**: For event-driven processing.
- **Google BigQuery**: For data storage and analytics.

## **Architecture**
The architecture consists of:
1. **Google Cloud Storage (GCS):** Stores raw input data files.
2. **Pub/Sub:** Sends notifications for new file uploads in GCS.
3. **Cloud Functions:** Executes a transformation query in BigQuery based on Pub/Sub notifications.
4. **BigQuery:** Processes and stores the transformed data.

**Data Flow**:
    - Files uploaded to **Google Cloud Storage (GCS)** trigger Pub/Sub notifications.
    - Pub/Sub messages trigger a **Cloud Function** to process the data.
    - Processed data is loaded into a **BigQuery** table for analytics.

### **Prerequisites**
Ensure you have:
1. A **Google Cloud Platform (GCP)** project with billing enabled.
2. **Google Cloud SDK** installed locally and project must me authorized(if not, use following to authorize):
    ```bash
    gcloud auth login
    ```
3. **Python 3.11** installed.
4. Required GCP APIs enabled:
   - **Cloud Functions API**
   - **Pub/Sub API**
   - **BigQuery API**
   - **Cloud Storage API**
5. Your GCP account's default service account must have following permissions:
   - **BigQuery Data Editor**
   - **Pub/Sub Data Editor**
   - **Storage Admin**

## Setup Instructions

### Step 1: Clone the Repository
1. **Create Topic**:
    ```bash
    git clone https://github.com/aman-shaurya07/Real-Time-Movie-Data-Pipeline-with-Cloud-Functions-and-BigQuery.git
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
