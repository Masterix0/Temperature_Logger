import json

print("Welcome to the Temperature Logger config initializer!")
print("Please input the following deatils, so they can be written to the config file!")
polling_interval = int(input(
    "Polling interval (delay between temperature reads, in seconds): "))
emails_on = input(
    "Email usage (whether you want the program to email you with relevant information)\nYES or NO: ").lower()

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

if temperature_alert_on == "yes":
    alert_email_on = True
    alert_email_subject = input("Your alerts emails' subject: ")
    alert_email_body = input(
        "Your alert email body (written in string format)\nPLEASE use '{temperature}' to signal where you\nwant your temperature to go, as it will be used to format the string: ")
    alert_email_receiver = input(
        "Email address which will receive the alerts: ")

else:
    alert_email_subject, alert_email_body, alert_email_receiver = ''
    alert_email_on = False

json_config = {
    "polling_interval": polling_interval,
    "email_on": email_on,
    "email_username": email_username,
    "email_password": email_password,
    "graph_email": {
        "graph_email_on": graph_email_on,
        "graph_email_subject": graph_email_subject,
        "graph_email_body": graph_email_body,
        "graph_email_receiver": graph_email_receiver
    },
    "temperature_alert_email": {
        "alert_email_on": alert_email_on,
        "alert_email_subject": alert_email_subject,
        "alert_email_body": alert_email_body,
        "alert_email_receiver": alert_email_receiver
    }
}

with open("config.json", 'w') as config:
    json.dump(json_config, config)
