import os
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('bidirectional_motorA_hop_1_rate_3.csv')
df_2 = pd.read_csv('')

motor = 'motorA [left → right] '

# Ontrack
plt.title(f'{motor} on track with epochs')
plt.plot(df['OnTrack'])
plt.xlabel('number of Epochs')
plt.grid(True)
plt.ylabel('Num motors on the track')
plt.legend([motor])
plt.show()


