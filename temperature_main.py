# Import standart libraries
import datetime
import time
import pathlib

# Import custom libraries
import temperature_parser
import temperature_config_reader
import temperature_email
import temperature_plot

# Initializes variables from the config file

pol_time = temperature_config_reader.get_pol_time()
email_on = temperature_config_reader.get_email_on()


# Initializes variables based on time

current_day = datetime.date.today()


# Checks whether the 'Temperature_Logs' directory exists
# and, if it doesn't, creates it

current_path = pathlib.Path.cwd()
logs_path = current_path / 'Temperature_Logs'
graphs_path = current_path / 'Temperature_Graphs'

if not logs_path.exists():
    logs_path.mkdir()

if not graphs_path.exists():
    graphs_path.mkdir()

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
    with open((str(logs_path / current_day.isoformat()) + ".csv"), 'a') as todays_log:
        todays_log.write('{time},{temperature}\n'.format(
            time=current_time.strftime("%H:%M:%S"), temperature=current_temp))

    time.sleep(pol_time)
