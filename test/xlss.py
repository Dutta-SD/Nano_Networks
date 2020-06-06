''' To use this function change the name of the filepath
variable to the path of the .xlsx file. '''

'''NOTE: This program makes the .txt files in the same directory
as the program.'''


import pandas as pd
import struct

# the variable to change[Change this]
filepath = "./data_1.xlsx"

''' Converts to ieee binary format'''
def float_to_bin32(f):
    fl_repr = struct.unpack( 'I', struct.pack('f', f) )[0]
    '''fills left with 0 else only the portion without sign bit is returned'''
    return bin(fl_repr)[2:].zfill(32)

# Prints in same folder as program
df = pd.read_excel(filepath, header=None)
df_2 = df.applymap(float_to_bin32)

for row in range(df_2.shape[0]):
    file_name = "rom_row_" + str(row) + ".txt"
    with open(file_name, "w") as f:
        for i in df_2.iloc[row, : ]:
            f.write(str(i) + "\n")
