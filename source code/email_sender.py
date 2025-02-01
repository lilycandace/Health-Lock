
 import smtplib
 from email.mime.multipart import MIMEMultipart
 from email.mime.text import MIMEText
 def send_email(subject, content):
 # Gmail account credentials
 sender_email = "12342403@gmail.com" # Your Gmail address
 recipient_email = "5678@gmail.com" # Recipient's email address
 password = "sjf hsh sdf" # Gmail app-specific password or your regular
 password if less secure apps is enabled
 # Create email message
 msg = MIMEMultipart()
 msg['From'] = sender_email
 msg['To'] = recipient_email
 msg['Subject'] = subject
 01 - BRANDING
IMPLEMENTATION 
email_sender.py
 # Email content
    body = MIMEText(content, 'plain') # Plain text email body
    msg.attach(body)
    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the Gmail SMTP server
    server.starttls() # Secure the connection using TLS (Transport Layer Security)
    try:
        # Log in to your Gmail account
        server.login(sender_email, password)
        # Send email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
    finally:
        server.quit() # Close the SMTP connection
 # Example usage
 send_email('Anomaly Alert', 'An anomaly has been detected in the log data')
