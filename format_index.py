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
    plt.gca().set_yticklabels(["too-dry" if y == 0 else ("optimal" if y == 0.5 else ("too-wet" if y == 1 else "")) for y in current_values])

    plt.gcf().autofmt_xdate()

    plt.savefig('moisture-trend.png')
    current_moisture = ("low", "optimal", 'high')[int(2 * y[-1])]
    return 'moisture-trend.png', current_moisture

def tag(tag, text="", options=""):
    return f"<{tag} {options}>"+text+f"</{tag}>"

def get_suggested_action(current_moisture): #TODO make this dynamic
    if (current_moisture == 'low'):
        return "water the lawn"
    elif (current_moisture == 'optimal'):
        return "water if sunny"
    elif (current_moisture == 'high'):
        return "don't water the lawn"

def update_html():
    trend_png, current_moisture = get_moisture_data()
    action = get_suggested_action(current_moisture)

    with open('index.html', 'w') as site:
        site.write(tag("h", "Lawn moisture monitor"))
        site.write(tag("br"))
        site.write(tag("h4", "last weeks trend:"))
        site.write(tag("img", options=f"src=\"{trend_png}\""))
        site.write(tag("br"))
        site.write(tag("p", f"Current moisture content: {current_moisture}"))
        site.write(tag("p", f"Suggested action: {action}"))

update_html()