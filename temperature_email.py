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
import temperature_parser

# Read config for your email address and password
username, password = temperature_config_reader.get_email_general_credentials()


# Create a multipart message and set headers
def send_email(email_subject, email_body, email_receiver, readings_date):
    """
    Sends an email with yesterday's info plotted into a graph
    """

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


def send_graph_email():
    """
    Send yesterday's readings and their corresponding graph
    """

    subject, body, receiver = temperature_config_reader.get_email_graph_details()

    # Get yesterday as a string
    readings_date = (datetime.date.today() -
                     datetime.timedelta(days=1)).isoformat()

    send_email(subject, body, receiver, readings_date)


def send_alert_email():
    """
    Send today's readings and their corresponding graph,
    as well as the current temperature
    """

    subject, body, receiver = temperature_config_reader.get_email_alert_details()

    formated_body = body.format(temperature=temperature_parser.get_temp())

    # Get today as a string
    readings_date = (datetime.date.today()).isoformat()

    send_email(subject, formated_body, receiver, readings_date)
