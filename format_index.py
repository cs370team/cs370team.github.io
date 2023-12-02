# import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
# import numpy as np
import csv

def get_moisture_data():
    # data = pd.read_csv('sample_data/data.csv').values

    # X = data[max(-346,-len(data)):,0]
    # X = [datetime.datetime.fromtimestamp(x) for x in X]
    # y = 1-np.average(data[max(-168,-len(data)):,1:], axis=1)

    # fig = plt.figure(figsize=(10, 2))
    # fig.gca().yaxis.set(ticks=np.arange(-.5, 2, .5))

    # plt.scatter(X,y, alpha=.5)

    # plt.plot(X, np.array([.75]*len(X)), "--b")
    # plt.plot(X, np.array([.25]*len(X)), '--r')

    # current_values = plt.gca().get_yticks()

    # plt.ylim((-0.25,1.25))
    # plt.gca().set_yticklabels("too-dry" if x == 0 else ("optimal" if x == .5 else ("too-wet" if x == 1 else "")) for x in current_values)

    # plt.gcf().autofmt_xdate()
    
    # plt.savefig('moisture-trend.png')
    # current_moisture = ("low", "optimal", 'high')[int(2*y[-1])]
    # return 'moisture-trend.png', current_moisture

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    X = [datetime.datetime.fromtimestamp(float(row[0])) for row in data[-346:]]
    y = 1 - sum(float(row[1]) for row in data[-168:]) / 168

    fig = plt.figure(figsize=(10, 2))
    fig.gca().yaxis.set(ticks=[-0.5, 0, 0.5, 1, 1.5])

    plt.scatter(X, [y] * len(X), alpha=0.5)

    plt.plot(X, [0.75] * len(X), "--b")
    plt.plot(X, [0.25] * len(X), '--r')

    current_values = plt.gca().get_yticks()

    plt.ylim((-0.25, 1.25))
    plt.gca().set_yticklabels(["too-dry" if x == 0 else ("optimal" if x == 0.5 else ("too-wet" if x == 1 else "")) for x in current_values])

    plt.gcf().autofmt_xdate()

    plt.savefig('moisture-trend.png')
    current_moisture = ("low", "optimal", 'high')[int(2 * y)]
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