# Import standard libraries
import smtplib
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Import custom libraries
import temperature_config_reader

# Read config
username, password, email_subject_start, email_body, \
    email_receiver = temperature_config_reader.get_email_credentials()
