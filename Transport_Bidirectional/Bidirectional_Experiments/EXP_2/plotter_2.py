import os
import matplotlib.pyplot as plt
import pandas as pd

def return_params(motor_name, extension = '.csv'):
    # motor_name should be motorA or motorB
    csv_file = [        
        f for f in os.listdir() if (f.endswith(extension) and f.find(motor_name) != -1)
        ][0]

    splits = csv_file.split(sep = '_')
    hop_motor, rate_motor = splits[3], splits[5].split(sep='.')[0]

    return csv_file, hop_motor, rate_motor



motorA_csv, hop_A, rate_A = return_params('motorA')
motorB_csv, hop_B, rate_B = return_params('motorB')


df_A = pd.read_csv(motorA_csv, index_col=0)
df_B = pd.read_csv(motorB_csv, index_col=0)


motorA = f'motorA  [hop {hop_A} rate {rate_A}] '
motorB = f'motorB  [hop {hop_B} rate {rate_B}] '

str1 = '[left → right]'
str2 = '[right → left]'

for column_name in df_A.columns:
    plt.figure()
    plt.title(
    f'''
    Number of Motors of {column_name}, 
    Track Dimensions : 3 x 50
    Initial : 100 motor A left, 100 motor B left, 100 motor A right, 100 motor B right
    '''
    )

    plt.plot(df_A[column_name], 'r')
    plt.plot(df_B[column_name], 'k', alpha = 0.7)

    plt.legend([motorA ,motorB])

    plt.xlabel('number of Epochs')
    plt.grid(True)
    plt.ylabel('Num motors')
    plt.savefig(f'{column_name}.png', bbox_inches='tight', dpi=200)
