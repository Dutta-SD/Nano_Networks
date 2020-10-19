import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('./motorB_run_1.csv')
#sns.barplot(data = df, x = 'Epoch', y = 'Input', color = 'black')
sns.barplot(data = df, x = 'Epoch', y = 'Input', color = 'blue', saturation=.5)
sns.barplot(data = df, x = 'Epoch', y = 'Output', color = 'black', saturation = .5)
plt.xticks([])
plt.title('MotorB { initial : 200, Hop :1}')
plt.show()