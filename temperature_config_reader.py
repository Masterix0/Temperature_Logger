# Opens the config file and proceeds to browse it,
def find_line(config_str):
    """
    Reads the config file and proceeds to find a line started 
    by whichever string you specified as an input 
    """

    # If the function works, this should be replaced by the line
    res = 'meh'

    line = 'placeholder'
    config = open('config.txt')
    while (line != ''):
        line = config.readline()
        # Ignores any comments, providing (I hope) a boost in speed
        if (line[0] != '#'):
            pass

        # If the line starts with the given texts, stops the cycle
        # sets the result as that line
        if line.startswith(config_str):
            res = line
            break

    config.close()

    # If the original res value is ever outputted, that means the config doesn't
    # have the line we were looking for. Therefore, we should raise an error.
    if res == 'meh':
        print('Well, something went terribly wrong.')
    else:
        return res


def get_pol_time():
    """
    Returns an integer corresponding to the ammount of 
    seconds specified for the pol_time in config.txt
    """
    pol_line = find_line('pol_interval')

    # Formats the line so we find the number we want
    pol_time = pol_line[(pol_line.index('=') + 1):]
    pol_time = pol_time.lstrip(' \n')
    pol_time = int(pol_time)

    return pol_time


def get_email_on():
    email_on_line = find_line('email_on')

    email_on = eval(
        email_on_line[(email_on_line.index('=') + 1):].lstrip(' \n'))

    return email_on


def get_email_credentials():
    """
    Returns an array containing the email details
    """

    username_line = find_line('email_username')
    password_line = find_line('email_password')
    subject_line = find_line('email_subject')
    body_line = find_line('email_body')
    receiver_line = find_line('email_receiver')

    username = username_line[(username_line.index('=') + 1):].lstrip(' \n')

    password = password_line[(password_line.index('=') + 1):].lstrip(' \n')

    subject = subject_line[(
        subject_line.index('=') + 1):].lstrip(' \n')

    body = eval(
        body_line[(body_line.index('=') + 1):].lstrip(' \n'))

    receiver = receiver_line[(
        receiver_line.index('=') + 1):].lstrip(' \n')

    return (username, password, subject, body, receiver)
