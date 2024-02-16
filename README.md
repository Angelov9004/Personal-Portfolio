# Personal Portfolio Website

This is my personal portfolio website built using Flask, a Python web framework.

![portfolio](https://github.com/Angelov9004/Personal-Portfolio-Flask-/assets/136641015/536ae872-0951-402d-8f4e-b64554f4d7c4)


## Description

This website serves as a platform to showcase my projects, skills, and experience. It includes a homepage, portfolio section, about me section, and a contact form.

## Features

- Responsive design for various devices
- Portfolio section to showcase projects
- About Me page to provide information about myself
- Contact form for users to reach out to me

## Technologies Used

- Flask
- HTML
- CSS
- JavaScript

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Angelov9004/Personal-Portfolio.git
   
## Navigate to the project directory:

cd portfolio

## Install the required dependencies:

pip install -r requirements.txt

## Run the Flask application:

python app.py


Open your web browser and visit http://localhost:5000 to view the website.

## Date_time.py

Your time() function is designed to return the current local date and time in the format "Month Day, 
Year Hour:Minute:Second". However, it can be further improved for clarity and consistency.

## smtp.py

Your send_email function is designed to send an email using SMTP. However, there are a few potential improvements and considerations:

Environment Variables: Using os.getenv to fetch sensitive data like email credentials from environment variables is a good practice for security. Make sure you have these environment variables set in your deployment environment or in a .env file if you're using tools like python-dotenv.

Email Body: The email body construction seems straightforward, incorporating the user's name, email, subject, and message. Ensure that you're properly formatting the email body for readability.

SMTP Server: Ensure that you're using the correct SMTP server and port. The server address 'smtp.yourserver.com' and port 25 are placeholders. Make sure to replace them with the actual SMTP server details provided by your email service provider.

Error Handling: It's essential to handle potential errors gracefully, especially during email sending. Consider implementing error handling to catch and log any exceptions that may occur during the email sending process.

## Make sure to replace 'smtp.yourserver.com', 25, and the environment variables (SENDER_EMAIL, RECEIVER_EMAIL, PASSWORD) with your actual SMTP server details and email credentials. Additionally, consider logging errors or handling them according to your application's requirements.


