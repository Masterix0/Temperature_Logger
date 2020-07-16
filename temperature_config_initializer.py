config_text = """
#Polling interval, expressed in seconds (sets the interval in which your
#program will log a new temperature reading, default is 5 minutes)
pol_interval = {pol_interval}

#Email usage (whether you want the program to email you with relevant information)
#Either write "True" or "False", be careful with lower and upper case characters,
#as these will break the program
email_on = {email_on}

#Email username
email_username = {email_username}

#Email password
email_password = {email_password}

#Your email's subject
email_subject = {email_subject} 

#Your email body
email_body = "{email_body}"

#Receiver email
email_receiver = {email_receiver}
"""


print("Welcome to the Temperature Logger config initializer!")
print("Please input the following deatils, so they can be written to the config file!")
polling_interval = input(
    "Polling interval (delay between temperature reads, in seconds): ")
email_on = input(
    "Email usage (whether you want the program to email you with relevant information)\nYES or NO: ")

if email_on.lower() == "yes":
    email_username = input(
        "The email address with which you want to send emails: ")
    email_password = input("That email's password: ")
    email_subject = input("Your email's subject: ")
    email_body = input(
        "Your email body (written in string format. i.e: using \\ns): ")
    email_receiver = input("Receiver email: ")
    email_on = "True"

else:
    email_username, email_password, email_subject, email_body, email_receiver = ''
    email_on = "False"

with open("config.txt", 'w') as config:
    config.write(config_text.format(pol_interval=polling_interval,
                                    email_on=email_on,
                                    email_username=email_username,
                                    email_password=email_password,
                                    email_subject=email_subject,
                                    email_body=email_body,
                                    email_receiver=email_receiver))
