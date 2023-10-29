import pandas as pd 

import matplotlib.pyplot as plt 

plt.style.use("dark_background")

grouped_data = pd.read_csv("./data/grouped_data.csv", index_col = "Range")

def line_graph_grouped():
    grouped_data.plot()
    plt.show()

def bar_graph_grouped():
    grouped_data.plot.bar()
    plt.show()