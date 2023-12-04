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

    fig = plt.figure(figsize=(10, 2))
    fig.gca().yaxis.set(ticks=[-0.5, 0, 0.5, 1, 1.5])

    plt.scatter(X,y, alpha=0.5)

    plt.plot(X, [0.75] * len(X), "--b")
    plt.plot(X, [0.25] * len(X), '--r')

    current_values = plt.gca().get_yticks()

    plt.ylim((-0.25, 1.25))
    plt.gca().set_yticklabels(["Too-Dry" if y == 0 else ("Optimal" if y == 0.5 else ("Too-Wet" if y == 1 else "")) for y in current_values])

    plt.gcf().autofmt_xdate()

    plt.savefig('moisture-trend.png')
    current_moisture = ("low", "optimal", 'high')[int(2 * y[-1])]
    return 'moisture-trend.png', current_moisture

def tag(tag, text="", options=""):
    return f"<{tag} {options}>"+text+f"</{tag}>"

def get_suggested_action(current_moisture): #TODO make this dynamic
    if (current_moisture == 'low'):
        moisture_notification()
        return " The Plant/Lawn Needs Watering"
    elif (current_moisture == 'optimal'):
        return " Water if the Temperature is 80-Degrees Farenheit or More (\Outside Plants or Lawn Only)\."
    elif (current_moisture == 'high'):
        return " Do not water Lawn/Plants"

def update_html():
    trend_png, current_moisture = get_moisture_data()
    action = get_suggested_action(current_moisture)

    with open('index.html', 'w') as site:
        site.write(tag("h", "Soil Moisture Monitor"))
        site.write(tag("br"))
        site.write(tag("h4", "48-Hour Moisture Trend:"))
        site.write(tag("img", options=f"src=\"{trend_png}\""))
        site.write(tag("br"))
        site.write(tag("p", f"Current Moisture Content: {current_moisture}"))
        site.write(tag("p", f"Suggested Action: {action}"))

update_html()
