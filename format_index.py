from notification import moisture_notification
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import csv

def get_moisture_data():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    X = [datetime.datetime.fromtimestamp(float(row[0])) for row in data[-346:]]
    y = [1 - (int(row[1]) + int(row[2])) / 2.0 for row in data]

    fig = plt.figure(figsize=(10, 4))
    fig.gca().yaxis.set(ticks=[-0.5, 0, 0.5, 1, 1.5])

    plt.scatter(X,y, alpha=0.5)

    plt.plot(X, [0.75] * len(X), "--b")
    plt.plot(X, [0.25] * len(X), '--r')

    current_values = plt.gca().get_yticks()

    plt.ylim((-0.25, 1.25))
    plt.gca().set_yticklabels(["Too-Dry" if y == 0 else ("Optimal" if y == 0.5 else ("Too-Wet" if y == 1 else "")) for y in current_values])
    plt.gcf().autofmt_xdate()
    plt.subplots_adjust(bottom=.5)

    plt.savefig('moisture-trend.png')
    current_moisture = ("low", "optimal", 'high')[int(2 * y[-1])]
    return 'moisture-trend.png', current_moisture

def tag(tag, text="", options=""):
    return f"<{tag} {options}>"+text+f"</{tag}>"

def get_suggested_action(current_moisture): #TODO make this dynamic
    
    moisture_notification() #For the demo
    
    if (current_moisture == 'low'):
        moisture_notification()
        return " The Plant/Lawn Needs Watering"
    elif (current_moisture == 'optimal'):
        return " Lightly water if the temperature is 80-Degrees Farenheit or More (Outside Plants or Lawn Only)."
    elif (current_moisture == 'high'):
        return " Soil is above optimal levels, do not water."

def update_html():
    trend_png, current_moisture = get_moisture_data()
    action = get_suggested_action(current_moisture)

    with open('index.html', 'w') as site:
        site.write(tag("h1", "Soil Moisture Monitor"))
        site.write(tag("br"))
        site.write(tag("h4", "7-Day Moisture Trend:"))
        site.write(tag("p", f"If less than 7 days of data, the graph will reflect back to the first day of data."))
        site.write(tag("img", options=f"src=\"{trend_png}\""))
        site.write(tag("br"))
        site.write(tag("p", f"Current Moisture Content: {current_moisture}"))
        site.write(tag("p", f"Suggested Action: {action}"))

