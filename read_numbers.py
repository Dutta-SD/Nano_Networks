from dectobin_function import dec_to_float32
import pandas as pd



def csv2float32(filename):
    # read DataFrame   
    df = pd.read_csv(filename, header = None, dtype='str', sep = "\t")
    
    # Concatenate numbers 
    for i in df.columns:
        df[0] += df[i]
    
    # Create the final DataFrame
    Final_df = pd.DataFrame()
    for i in df[0]:
        Final_df[i] = dec_to_float32(i)
      
    # Transpose so that numbers become index
    Final_df = Final_df.transpose()
    
    return Final_df

def xlsx2float32(filename):
     # read DataFrame    
    df = pd.read_excel(filename, header = None, dtype='str')
    
    # Concatenate numbers
    for i in df.columns:
        df[0] += df[i]
        
    # Create the final DataFrame
    Final_df = pd.DataFrame()
    for i in df[0]:
        Final_df[i] = dec_to_float32(i)
     
    # Transpose so that numbers become index
    Final_df = Final_df.transpose()
    
    return Final_df


#filename = ".\new_1.xlsx"
# xlsx2float32(filename)
