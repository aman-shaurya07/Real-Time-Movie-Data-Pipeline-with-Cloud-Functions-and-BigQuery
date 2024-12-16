from google.cloud import bigquery
import base64
import json

def gcs_to_bigquery(event, context):
    """
    Cloud Function to trigger BigQuery transformation query
    when a new file is uploaded to GCS.
    """
    try:
        # Decode the Pub/Sub message
        if 'data' in event:
            pubsub_message = base64.b64decode(event['data']).decode('utf-8')
            gcs_event = json.loads(pubsub_message)

            # Extract bucket and file details
            bucket_name = gcs_event.get('bucket')
            file_name = gcs_event.get('name')

            if not bucket_name or not file_name:
                print("Bucket or file name not found in event payload.")
                return

            print(f"Processing file: {file_name} in bucket: {bucket_name}")

            # Initialize BigQuery client
            client = bigquery.Client()

            # BigQuery Transformation Query
            query = """
            CREATE OR REPLACE TABLE movie_data.transformed_movie_data AS
            SELECT 
                Series_Title,
                Released_Year,
                Genre,
                Certificate,
                Runtime,
                IMDB_Rating,
                No_of_Votes,
                Gross,
                Meta_score,
                Director,
                Star1,
                Star2,
                Star3,
                Star4,
                CASE 
                    WHEN Gross >= 100000000 THEN 'Blockbuster'
                    WHEN Gross >= 50000000 THEN 'Hit'
                    ELSE 'Average'
                END AS Revenue_Category,
                CASE 
                    WHEN IMDB_Rating >= 8 THEN 'High'
                    WHEN IMDB_Rating >= 6 THEN 'Medium'
                    ELSE 'Low'
                END AS Rating_Category
            FROM 
                movie_data.raw_movie_data
            WHERE 
                Gross IS NOT NULL AND IMDB_Rating IS NOT NULL AND No_of_Votes IS NOT NULL;
            """

            # Execute the query
            query_job = client.query(query)  # API request
            query_job.result()  # Wait for the job to finish

            print("Transformation query executed successfully.")
        else:
            print("No event data found in the Pub/Sub message.")
    except Exception as e:
        print(f"Error during Cloud Function execution: {e}")
