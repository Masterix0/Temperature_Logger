# Import standard libraries
import smtplib
import ssl
import datetime
from pathlib import Path

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Import custom libraries
import temperature_config_reader

# Read config
username, password, email_subject, email_body, \
    email_receiver = temperature_config_reader.get_email_credentials()


# Create a multipart message and set headers
def send_email():
    # Get the day of the readings as a string
    readings_date = (datetime.date.today() -
                     datetime.timedelta(days=1)).isoformat()

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = username
    message["To"] = email_receiver
    message["Subject"] = email_subject

    # Add body to email
    message.attach(MIMEText(email_body, "plain"))

    # Fetch filepath
    log_name = (readings_date + '.csv')
    log_path = Path.cwd() / 'Temperature_Logs' / log_name
    graph_name = (readings_date + '.png')
    graph_path = Path.cwd() / 'Temperature_Graphs' / graph_name

    # Open file in binary mode
    with open(log_path, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        "attachment; filename= {log_name}".format(log_name=log_name),
    )

    # Add attachment to message and convert message to string
    message.attach(part)

    # Open file in binary mode
    with open(graph_path, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        "attachment; filename= {graph_name}".format(graph_name=graph_name),
    )

    # Add attachment to message and convert message to string
    message.attach(part)

    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(username, password)
        server.sendmail(username, email_receiver, text)
