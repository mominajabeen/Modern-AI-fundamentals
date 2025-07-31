import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('industry.csv')
data.hist()

plt.show()