# Import standard libraries
from pathlib import Path
import datetime
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, HourLocator, DateFormatter

readings_date = (datetime.date.today() -
                 datetime.timedelta(days=1)).isoformat()


readings_path = Path.cwd() / 'Temperature_Logs' / (readings_date + ".csv")


def create_plot_png():
    """
    Creates a png graph based on a day's readings
    """

    def dateconv(s): return datetime.datetime.strptime(
        s.decode("utf-8"), "%H:%M:%S")

    data = np.genfromtxt(readings_path, delimiter=',', names=('time', 'temp'),
                         converters={'time': dateconv},
                         dtype=[('time', datetime.datetime), ('temp', float)], skip_footer=1)

    print(data)

    fig, ax = plt.subplots()
    ax.plot_date(data['time'], data['temp'])

    # this is superfluous, since the autoscaler should get it right, but
    # use date2num and num2date to convert between dates and floats if
    # you want; both date2num and num2date convert an instance or sequence
    ax.set_xlim(dates[0], dates[-1])

    # The hour locator takes the hour or sequence of hours you want to
    # tick, not the base multiple

    ax.xaxis.set_major_locator(HourLocator(range(0, 25, 6)))
    ax.xaxis.set_minor_locator(HourLocator(range(0, 25, 1)))
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))

    ax.fmt_xdata = DateFormatter('%H:%M:%S')
    fig.autofmt_xdate()
    plt.savefig("{date}.png".format(date=readings_date))


"""
    plt.title("Temperature Graph for {date}".format(date=readings_date))
    plt.xlabel('Time')
    plt.ylabel('Temp(deg C)')
    plt.xticks(rotation=45, ha='right')
    plt.plot(data['time'], data['temp'])
    plt.savefig("{date}.png".format(date=readings_date))
"""
