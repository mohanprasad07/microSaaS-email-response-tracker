# Email Response Tracker

Email Response Tracker is a simple tool for tracking emails sent and receiving reminders if no response has been received within a set period. It is useful for people who regularly send emails to clients, prospects, or colleagues and want to stay on top of follow-up actions.

## Features

- Track sent emails and their response status.
- Set a reminder if no response is received within a certain time frame (e.g., 3 days).
- Basic front-end to visualize email status and follow-ups.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/email-response-tracker.git
    ```

2. Navigate to the project directory:
    ```bash
    cd email-response-tracker
    ```

3. Install dependencies:
    - If using Python:
      ```bash
      pip install flask
      ```

4. Set up email integration in `app.py`:
    - Use your Gmail or SMTP details in the script.

5. Run the app:
    ```bash
    python app.py
    ```

6. Open `index.html` in your browser to see the UI.

## Screenshots

![Email Response Tracker Screenshot](C:\Users\sunil\OneDrive\Desktop\microSaaS-email-response-tracker\screenshot of email response tracker.png) 

Tech Stack:
Backend: Python (Flask, smtplib)
Frontend: HTML, CSS
### Key Sections in the README:

1. **Project Description**: Brief overview of the tool's purpose.
2. **Features**: List of features.
3. **Setup Instructions**: Clear step-by-step guide on how to set up the project.
4. **Screenshots**: If you have a screenshot, you can link it here.
5. **Basic Implementation**: Contains code snippets for `app.py`, `index.html`, and `styles.css`.
6. **Tech Stack**: The technologies used for the project.
7. **License**: A placeholder for the project license (e.g., MIT License).


## Basic Implementation

### Backend (app.py)

```python
from flask import Flask, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Serving the index.html page

@app.route('/send_email')
def send_email():
    # Code to send email (basic example)
    sender_email = "your-email@example.com"
    receiver_email = "recipient@example.com"
    subject = "Follow-up: Your response needed"
    body = "Hi, this is a reminder for your pending response."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, "yourpassword")
        server.sendmail(sender_email, receiver_email, msg.as_string())

    return "Email sent!"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Response Tracker</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Email Response Tracker</h1>
        <p>Track your sent emails and get notified if no response is received within the set time.</p>
        <button onclick="sendEmail()">Send Test Email</button>
    </div>
    
    <script>
        function sendEmail() {
            fetch('/send_email')
                .then(response => response.text())
                .then(data => alert(data));
        }
    </script>
</body>
</html>

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f9;
    margin: 0;
    padding: 0;
}

.container {
    width: 50%;
    margin: 50px auto;
    text-align: center;
    background-color: #fff;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

button {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}


