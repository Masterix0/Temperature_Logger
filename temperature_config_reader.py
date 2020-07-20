import json

with open("config.json", "r") as json_config:
    config = json.load(json_config)


def get_pol_time():
    """
    Returns an integer corresponding to the ammount of 
    seconds specified for the pol_time in config.txt
    """

    return config["polling_interval"]


def get_graphs_email_on():
    """
    Returns a boolean indicating whether daily graphs are on or off
    """
    return config["graph_email"]["graph_email_on"]


def get_alerts_email_on():
    """
    Returns a boolean indicating whether temperature alerts are on or off
    """
    return config["temperature_alert_email"]["alert_email_on"]


def get_email_general_credentials():
    """
    Returns an array containing the email sender address and corresponding password
    """

    return (config["email_username"], config["email_password"])


def get_email_graph_details():
    """
    Returns an array with a graph email details
    """

    graph_details = config["graph_email"]

    return (graph_details["graph_email_subject"],
            graph_details["graph_email_body"],
            graph_details["graph_email_receiver"])


def get_email_alert_details():
    """
    Returns an array with a temperature alert email details
    """

    alert_details = config["temperature_alert_email"]

    return (alert_details["alert_email_subject"],
            alert_details["alert_email_body"],
            alert_details["alert_email_receiver"])


def get_alert_temps():
    """
    Returns an array with the min and max 
    temps required for an alert to go off,
    as well as the value of the sensitivity
    used to calculate whether a new alert is
    sent after a bad temp
    """

    alert_details = config["temperature_alert_email"]

    return (alert_details["alert_min_temp"], alert_details["alert_max_temp"], alert_details["alert_temp_scaling"])
