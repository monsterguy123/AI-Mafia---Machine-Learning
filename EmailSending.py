import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

def send_html_email():
    # Load environment variables from .env file
    load_dotenv()

    sender = "deepakbisht9891@gmail.com"
    recipient = "deepak10621202021@msijanakpuri.com"
    subject = "🚀 AI Mafia - Machine Learning Batch Announcement"

    # Read Gmail app password from .env
    password = os.getenv("GMAIL_APP_PASSWORD")

    if not password:
        print("❌ Error: App password not found in .env file.")
        return

    # HTML body
    html = """
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #f5f5f5; padding: 30px;">
        <div style="max-width: 600px; margin: auto; background-color: white; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); padding: 20px;">
            <h2 style="color: #2b2b2b; text-align: center;">🤖 Welcome to AI Mafia!</h2>
            <p style="font-size: 16px; color: #333;">
                Hello <b>Everyone!</b><br><br>
                We are thrilled to announce that a new batch of
                <span style="color: #007bff;"><b>AI Mafia - Machine Learning</b></span> 
                is starting soon! 🚀<br><br>
                Join us to explore the world of Artificial Intelligence, Machine Learning, and Data Science. 
                Let’s learn, build, and grow together!
            </p>
            <div style="text-align: center; margin: 30px 0;">
                <a href="https://your-website-link.com"
                   style="background-color: #007bff; color: white; padding: 12px 20px; border-radius: 8px; text-decoration: none; font-weight: bold;">
                   Join Now
                </a>
            </div>
            <p style="font-size: 14px; color: #555;">Thank you!<br>— <b>Deepak Bisht</b></p>
        </div>
    </body>
    </html>
    """

    # Create MIME message
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    # Attach HTML content
    msg.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)
        print("✅ HTML email sent successfully!")
    except Exception as e:
        print("❌ Error:", e)

send_html_email()
