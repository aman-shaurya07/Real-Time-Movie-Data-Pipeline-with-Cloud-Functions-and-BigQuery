#!/bin/bash

# Variables
PROJECT_ID="YOUR_PROJECT_ID"
BUCKET_NAME="your-bucket-name"
TOPIC_NAME="your-topic"

# Create a Pub/Sub topic
gcloud pubsub topics create $TOPIC_NAME --project=$PROJECT_ID

# Enable bucket notifications
gsutil notification create -t projects/$PROJECT_ID/topics/$TOPIC_NAME -f json gs://$BUCKET_NAME

echo "Bucket notification set up for bucket: $BUCKET_NAME with topic: $TOPIC_NAME"
