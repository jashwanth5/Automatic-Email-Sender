import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    # Email account credentials
    from_email = "your_email@gmail.com"
    from_password = "your_password"
    
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(from_email, from_password)  # Login to your email account
        
        # Convert the MIMEMultipart object to a string
        text = msg.as_string()
        
        # Send the email
        server.sendmail(from_email, to_email, text)
        
        # Disconnect from the server
        server.quit()
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
subject = "Test Email"
body = "This is a test email sent from a Python script."
to_email = "recipient_email@example.com"

send_email(subject, body, to_email
