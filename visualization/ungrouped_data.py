import pandas as pd 

import matplotlib.pyplot as plt 

plt.style.use("dark_background")

ungrouped_data = pd.read_csv("./data/ungrouped_data.csv")
ungrouped_data.index += 1

def line_graph_ungrouped():
    ungrouped_data.plot() 
    plt.show()

def bar_graph_ungrouped():
    ungrouped_data.plot.bar()
    plt.show()