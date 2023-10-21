import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

def make_trend_png():
    data = pd.read_csv('sample_data/data.csv').values

    X = data[max(-346,-len(data)):,0]
    X = [datetime.datetime.fromtimestamp(x) for x in X]
    y = 1-np.average(data[max(-168,-len(data)):,1:], axis=1)

    fig = plt.figure(figsize=(15, 2))

    plt.scatter(X,y, alpha=.5)

    plt.plot(X, np.array([.75]*len(X)), "--b", label="over-saturation")
    plt.plot(X, np.array([.25]*len(X)), '--r', label="")

    current_values = plt.gca().get_yticks()
    print(current_values)
    plt.gca().set_yticklabels(["", "too-dry", "ideal", "too-wet", ""])

    plt.gcf().autofmt_xdate()
    
    plt.savefig('moisture-trend.png')
    return 'moisture-trend.png'

def tag(tag, text="", options=""):
    return f"<{tag} {options}>"+text+f"</{tag}>"

def get_suggested_action(): #TODO make this dynamic
    return "watter your lawn"

def make_html():
    trend_png = make_trend_png()
    action = get_suggested_action()

    with open('index.html', 'w') as site:
        site.write(tag("h", "Lawn moisture monitor"))
        site.write(tag("br"))
        site.write(tag("h4", "last weeks trend:"))
        site.write(tag("img", options=f"src=\"{trend_png}\""))
        site.write(tag("br"))
        site.write(tag("p", f"Suggested action: {action}"))


make_html()