## X-Ray App - Python
The X-Ray App is a two-part web application that scrapes repositories, stores the data in DynamoDB, and displays the data as HTML using Python Flask.

# Lambda Function - Scrape and Store Data
The provided Python script is an AWS Lambda function that performs the scraping and storage functionalities. Here's an overview of the script:

The script leverages the requests library to scrape a webpage from the provided URL. It decodes the response content using base64 and stores the scraped text in a DynamoDB table. The script is executed as an AWS Lambda function.

# X-Ray App - Dynamic Backend Visualization
The X-Ray App is a web application that allows visitors to explore your infrastructure code and gain a deeper understanding of your expertise. It provides a recursive look at your backend code while it runs.

Traditional portfolio websites often fall short in demonstrating the backend aspects of your work. This app aims to bridge that gap by dynamically pulling code directly from your repositories. By doing so, you ensure that viewers always have access to the most up-to-date information without the need for manual updates.

With this app, potential employers or clients can explore your code and stay updated on the latest developments in your projects. It showcases your DevOps skills in infrastructure deployment and serves as a reflection of similar projects you have done on the job.

# The X-Ray App consists of two main components:

Data Scraping: The app scrapes repositories, retrieving code from the provided URL.
Data Visualization: The app stores the retrieved data in DynamoDB and displays it as HTML using Python Flask.

This dynamic approach to showcasing your backend infrastructure sets your portfolio apart, allowing visitors to delve deeper into your code and gain insights into your expertise.
