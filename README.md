## X-Ray App - Python
The X-Ray App is a two-part web application that scrapes repositories, stores the data in DynamoDB, and displays the data as HTML using Python Flask.

# Lambda-scraper.py
The provided Python script is an AWS Lambda function that performs the scraping and storage functionalities.
The script leverages the requests library to scrape a webpage from the provided URL. It decodes the response content using base64 and stores the scraped text in a DynamoDB table. The script is executed as an AWS Lambda function.

# Apache-flask.conf
The server configuration file that allows Apache to serve our Flask site. It specifies how Apache handles incoming requests on ports 80 and 443, enabling HTTPS and SSL certificate support for a secure website. Additionally, it sets up rules for handling domain names, web traffic, and specifies the location of CSS and JS content.

# app.py
The Flask application code that acts as the front-end wrapper for our website. This code replaces the traditional "index.html" page and executes Python code to route users to specific pages. By leveraging Python, this code enables real-time retrieval of data from the DynamoDB database and dynamically populates text boxes with the scraped code. Each page functions as a miniature Python app, delivering HTML content along with any required Python functions.

# X-Ray App - Dynamic Backend Visualization
The X-Ray App is a web application that allows visitors to explore your infrastructure code and gain a deeper understanding of your expertise. It provides a recursive look at your backend code while it runs.

Traditional portfolio websites often fall short in demonstrating the backend aspects of your work. This app aims to bridge that gap by dynamically pulling code directly from your repositories. By doing so, you ensure that viewers always have access to the most up-to-date information without the need for manual updates.

I use this app to show off my backend work that would traditionally never get to shine with a portfolio site. The website itself is just the tip of the iceberg, but the backend is completely automated and can be duplicated instantly thanks to AWS, Docker, Jenkins, and Github.
