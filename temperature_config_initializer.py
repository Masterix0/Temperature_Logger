import json

# Welcome phrases
print("Welcome to the Temperature Logger config initializer!")
print("Please input the following deatils, so they can be written to the config file!")

# General Info
polling_interval = int(input(
    "Polling interval (delay between temperature reads, in seconds): "))
emails_on = input(
    "Email usage (whether you want the program to email you with relevant information)\nYES or NO: ").lower()

# General email info
if emails_on == "yes":
    email_on = True
    email_username = input(
        "The email address with which you want to send emails: ")
    email_password = input("That email's password: ")
    graph_on = input(
        "Do you want the program to send you daily temperature graphs?\nYES or NO: ").lower()
    temperature_alert_on = input(
        "Do you want the program to email you when the temperature goes over a certain threshold?\nYES or NO: ").lower()

else:
    email_on = False
    email_username, email_password = ""
    graph_on, temperature_alert_on = "False"

# Graph email info
if graph_on == "yes":
    graph_email_on = True
    graph_email_subject = input("Your graphs emails' subject: ")
    graph_email_body = input(
        "Your graph email body (written in string format): ")
    graph_email_receiver = input(
        "Email address which will receive the graphs: ")

else:
    graph_email_subject, graph_email_body, graph_email_receiver = ''
    graph_email_on = False

# Alert email info
if temperature_alert_on == "yes":
    alert_email_on = True
    alert_min_temp = float(input(
        "The LOWEST temp acceptable before getting an alert (float): "))
    alert_max_temp = float(input(
        "The HIGHEST temp acceptable before getting an alert (float): "))
    alert_temp_scaling = float(input(
        "The variation in temperature required to send a new\nemail after the last alert (float): "))
    alert_email_subject = input("Your alerts emails' subject: ")
    alert_email_body = input(
        "Your alert email body (written in string format)\nPLEASE use '{temperature}' to signal where you\nwant your temperature to go, as it will be used to format the string: ")
    alert_email_receiver = input(
        "Email address which will receive the alerts: ")

else:
    alert_email_subject, alert_email_body, alert_email_receiver, alert_min_temp, alert_max_temp = ''
    alert_email_on = False

# Create a dictionary using all the inputs
# This is a standart config format, seeing that the actual
# JSON file will be very similar
# Standard values are below
json_config = {
    "polling_interval": polling_interval,  # 300 (5 minutes)
    "email_on": email_on,  # True
    "email_username": email_username,  # blabla@gmail.com
    "email_password": email_password,  # xxxxxxxxxxxxxxxxxxx
    "graph_email": {
        "graph_email_on": graph_email_on,  # True
        "graph_email_subject": graph_email_subject,  # Yesterday's temperature data
        # "A random message\n\nBest regards,\nBlabla Bot"
        "graph_email_body": graph_email_body,
        "graph_email_receiver": graph_email_receiver  # bleble@gmail.com
    },
    "temperature_alert_email": {
        "alert_email_on": alert_email_on,  # True
        "alert_min_temp": alert_min_temp,  # 16.0
        "alert_max_temp": alert_max_temp,  # 26.0
        "alert_temp_scaling": alert_temp_scaling,  # 0.5
        "alert_email_subject": alert_email_subject,  # OOPS, Temperature Exceeded Limit
        "alert_email_body": alert_email_body,
        # "\"This email serves as a notification that your beer is currently
        # at {temperature} degrees.\\nToday's temperature graph is sent as
        # an attachment.\\n\\nBest regards,\\nBot Cervejeiro.\""
        "alert_email_receiver": alert_email_receiver  # bleble@gmail.com
    }
}

# Save values to config file
with open("config.json", 'w') as config:
    json.dump(json_config, config)
