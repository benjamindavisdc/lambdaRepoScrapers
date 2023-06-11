import requests
import base64
import boto3

def lambda_handler(event, context):
    # Scrape the webpage
    url = "https://api.github.com/repos/benjamindavisdc/may23pipeline01jenkinsfile/contents/Jenkinsfile"
    response = requests.get(url)
    
    if response.status_code == 200:
        page_text = response.json()["content"]
        decoded_bytes = base64.b64decode(page_text)
        scraped_text = decoded_bytes.decode(errors='replace')

        print("Scraped webpage text:")
        print(scraped_text)
        
        # Put the scraped text into DynamoDB
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table = dynamodb.Table('x-ray_table')

        response = table.put_item(
            Item={
                'file_path': url,
                'file_content': scraped_text
            }
        )

        return {
            'statusCode': 200,
            'body': 'Item added successfully to DynamoDB table.'
        }
    else:
        return {
            'statusCode': response.status_code,
            'body': 'Failed to scrape webpage.'
        }
