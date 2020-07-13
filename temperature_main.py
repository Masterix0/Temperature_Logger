# Import standart libraries
import datetime
import time
import pathlib

# Import custom libraries
import temperature_parser
import temperature_config_reader

# Initializes variables from the config file

pol_time = temperature_config_reader.get_pol_time()


# Initializes variables based on time

today = datetime.date.today()


# Checks whether the 'Temperature_Logs' directory exists
# and, if it doesn't, creates it

current_path = pathlib.Path.cwd()
logs_path = current_path / 'Temperature_Logs'

if not logs_path.exists():
    logs_path.mkdir()
