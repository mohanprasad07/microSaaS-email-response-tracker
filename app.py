from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A list to track sent emails
tracked_emails = []

@app.route("/")
def index():
    return render_template("index.html", emails=tracked_emails)

@app.route("/send-email", methods=["POST"])
def send_email():
    # Get form data
    recipient = request.form.get("recipient")
    subject = request.form.get("subject")
    message = request.form.get("message")

    # Simulate sending an email (actual email functionality can be added later)
    if recipient and subject and message:
        tracked_emails.append({
            "recipient": recipient,
            "subject": subject,
            "message": message
        })
        return redirect(url_for("index"))

    # If form data is missing, return to the index with an error
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
