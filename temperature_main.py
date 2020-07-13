# Import standart libraries
import datetime
import time
import pathlib

# Import custom libraries
import temperature_parser
import temperature_config_reader
import temperature_email

# Initializes variables from the config file

pol_time = temperature_config_reader.get_pol_time()
email_on = temperature_config_reader.get_email_on()


# Initializes variables based on time

current_day = datetime.date.today()


# Checks whether the 'Temperature_Logs' directory exists
# and, if it doesn't, creates it

current_path = pathlib.Path.cwd()
logs_path = current_path / 'Temperature_Logs'

if not logs_path.exists():
    logs_path.mkdir()

# Main body
while True:
    # Checks what day it is and, if it's a later date than the one
    # we're working with, changes the current day
    now = datetime.date.today()
    if now > current_day:
        current_day = now
        if email_on:
            temperature_email.send_email()

    # Gets the current temperature and time
    current_temp = temperature_parser.get_temp()
    current_time = datetime.datetime.now()

    # Writes the new temperature reading to today's log
    with open(((logs_path / current_day.isoformat()) + ".txt"), 'a') as todays_log:
        todays_log.write('{hour}:{minutes}:{seconds}-{temperature}\n'.format(
            hour=current_time.hour, minutes=current_time.minute,
            seconds=current_time.second, temperature=current_temp))

    time.sleep(pol_time)
