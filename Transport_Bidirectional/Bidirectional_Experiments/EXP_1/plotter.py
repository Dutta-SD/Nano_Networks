import os
import matplotlib.pyplot as plt
import pandas as pd

df_A = pd.read_csv('bidirectional_motorA_hop_1_rate_3.csv')
df_B = pd.read_csv('bidirectional_motorB_hop_2_rate_5.csv')

hop_A, hop_B, rate_A, rate_B = 1, 2, 3, 5 ### Change for each file

motorA = f'motorA  [hop {hop_A} rate {rate_A}] '
motorB = f'motorB  [hop {hop_B} rate {rate_B}] '

str1 = '[left → right]'
str2 = '[right → left]'

# Ontrack

# plt.title(
# '''
# Number of Motors on Track, 
# Track Dimensions : 3 x 50
# Initial : 100 motor A left, 100 motor B left, 100 motor A right, 100 motor B right
# '''
# )

# plt.plot(df_A['OnTrack'])
# plt.plot(df_B['OnTrack'])

# plt.legend([motorA ,motorB])

# plt.xlabel('number of Epochs')
# plt.grid(True)
# plt.ylabel('Num motors on the track')
# plt.show()


# plt.title(
# '''
# Number of Motors of Left Input, 
# Track Dimensions : 3 x 50
# Initial : 100 motor A left, 100 motor B left, 100 motor A right, 100 motor B right
# '''
# )

# plt.plot(df_A['Input_Left'])
# plt.plot(df_B['Input_Left'])

# plt.legend([motorA ,motorB])

# plt.xlabel('number of Epochs')
# plt.grid(True)
# plt.ylabel('Num motors left input')
# plt.show()

# plt.title(
# '''
# Number of Motors of Right Input, 
# Track Dimensions : 3 x 50
# Initial : 100 motor A left, 100 motor B left, 100 motor A right, 100 motor B right
# '''
# )

# plt.plot(df_A['Input_Right'], 'r')
# plt.plot(df_B['Input_Right'])

# plt.legend([motorA ,motorB])

# plt.xlabel('number of Epochs')
# plt.grid(True)
# plt.ylabel('Num motors')
# plt.show()

# plt.title(
# '''
# Number of Motors of Reservoir, 
# Track Dimensions : 3 x 50
# Initial : 100 motor A left, 100 motor B left, 100 motor A right, 100 motor B right
# '''
# )

# plt.plot(df_A['Reservoir'], 'r.-')
# plt.plot(df_B['Reservoir'], alpha = 0.8)

# plt.legend([motorA ,motorB])

# plt.xlabel('number of Epochs')
# plt.grid(True)
# plt.ylabel('Num motors')
# plt.show()

# plt.title(
# '''
# Number of Motors of Output Right, 
# Track Dimensions : 3 x 50
# Initial : 100 motor A left, 100 motor B left, 100 motor A right, 100 motor B right
# '''
# )

# plt.plot(df_A['Output_Right'], 'r.-')
# plt.plot(df_B['Output_Right'], alpha = 0.8)

# plt.legend([motorA ,motorB])

# plt.xlabel('number of Epochs')
# plt.grid(True)
# plt.ylabel('Num motors')
# plt.show()

plt.title(
'''
Number of Motors of Output Left, 
Track Dimensions : 3 x 50
Initial : 100 motor A left, 100 motor B left, 100 motor A right, 100 motor B right
'''
)

plt.plot(df_A['Output_Left'], 'r.-')
plt.plot(df_B['Output_Left'], alpha = 0.8)

plt.legend([motorA ,motorB])

plt.xlabel('number of Epochs')
plt.grid(True)
plt.ylabel('Num motors')
plt.show()
