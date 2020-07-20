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
graph_on = temperature_config_reader.get_graphs_email_on()
alert_on = temperature_config_reader.get_alerts_email_on()
min_temp, max_temp, alert_temp_scaling = temperature_config_reader.get_alert_temps()

# Initializes variables based on time

current_day = datetime.date.today()

# This is the base value of the last bad temp
last_bad_temp = None

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
        if graph_on:
            # Finds out yesterday's date
            yesterdays_date = (datetime.date.today() -
                               datetime.timedelta(days=1)).isoformat()
            # Creates yesterday's temps plot
            temperature_plot.create_plot_png(yesterdays_date)
            # Sends yesterday's data and corresponding plot through email
            temperature_email.send_graph_email()

    # Gets the current temperature and time
    current_temp = temperature_parser.get_temp()
    current_time = datetime.datetime.now()

    # Writes the new temperature reading to today's log
    with open((str(logs_path / current_day.isoformat()) + ".csv"), 'a') as todays_log:
        todays_log.write('{time},{temperature}\n'.format(
            time=current_time.strftime("%H:%M:%S"), temperature=current_temp))

    # Prints the current time and temp to the interpreter
    print("Time:{time} - Temp(deg C):{temperature}".format(
        time=current_time.strftime("%H:%M:%S"), temperature=current_temp))

    # If the program is set to look for alerts, checks
    # whether the temp is within the allowed range
    if alert_on:
        if ((current_temp < min_temp) or (current_temp > max_temp)):
            # If it isn't, checks to see if there was no last_bad_temp
            # If there wasn't, send a warning and set it
            # All further readings will both have to be outside the allowed range
            # AND have a discrepancy of alert_temp_scaling over the last temp
            if ((last_bad_temp == None) or (abs(current_temp - last_bad_temp) > alert_temp_scaling)):
                last_bad_temp = current_temp
                temperature_plot.create_plot_png(
                    datetime.date.today().isoformat())
                temperature_email.send_alert_email()

    # Waits for however long you defined
    time.sleep(pol_time)
