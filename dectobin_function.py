# Function to give sign bit and change the string
def give_sign_bit_and_convert(hex_number):
    ''' Function give_sign_bit_and_convert() gives the sign bit value of input string.
        If first character of input is "-" then sign_bit = 1 else 0
        If the sign_bit is 1, it removes the "-" character from the input string.
        If we get + then we remove that symbol 
       
          @INPUT : hex_number(string) : hexadecimal form of number
          @RETURN : sign_bit(string): value of the signed bit
                    hex_number(string): the number with the sign_bit_removed
        
    '''
    # First character is - indicates negative number, sign bit is 1
    if hex_number[0] == "-" :
        # If negative sign bit is 1
        sign_bit = "1"
        
        # if number is negative, remove the '-' sign from the number
        hex_number = hex_number[ 1 : ]
        
    else:
        # If positive sign bit is 0
        sign_bit = "0"
        
        # If for the string we get numbers like +1, +3 etc...
        if hex_number[0] == '+':
            # remove the '+' sign 
            hex_number = hex_number[ 1 : ]
            
        
    return sign_bit, hex_number

# Function to get the exponent of the number
def get_exponent(hex_number):
    ''' Function get_exponent() returns the exponent of the hexadecimal input sring.
    Hexadecimal string is of the form '0x1.<mantissa>p<exponent>'.
    We can extract the exponent by selecting the last three characters.
    Then we add 127 to it in compliance with IEEE rules. And Convert to binary.
    
    @INPUT: hex_number(string) : hexadecimal form of string
    @RETURN: exponent of the number in binary'''
    
    # Get the sign of the exponent
    sign_of_expo, expo = give_sign_bit_and_convert(hex_number)
    
    # 0 for positive
    if sign_of_expo == '0':
        # Convert to integer and add 127       
        int_exp = int("0x" + expo, base = 16) + 127
    else:
        # Convert to integer and add 127
        int_exp = int("-0x" + expo, base = 16) + 127
    
    # Check for overflow, underflow conditions 
    if int_exp < 0:
        # If int_exp less than 0 then underflow, so give min limit
        return bin(0)[2:]
    elif int_exp > 255:
        # If int_exp greater than 255 overflow, so give max limit
        return bin(255)[2:]
    else:
        # Else return as need
        return bin(int_exp)[2:]
        

    
# Function to return the mantissa
def get_mantissa(hex_number):
    ''' Function get_mantissa() returns the mantissa of the hexadecimal input sring.
    Hexadecimal string is of the form '0x1.<mantissa>p<exponent>'.
    We can extract the mantissa by selecting characters from 4 to 8.
    Then we round the last bit and return the mantissa.(as the number is in hexadecimal so
    6 character would give 6 x 4 = 24 bits). Then we convert it to binary.
    
    @INPUT: hex_number(string) : hexadecimal form of string
    @RETURN: mantissa of the number in binary'''
    
    # get the required number of characters from the string
    # (here 6 hexadecimal characters)
    mantissa_hex = hex_number[:6]
    
    # get the mantissa
    mantissa = bin( int( "0x" + mantissa_hex, base=16) )[2:]
    
    # Round the mantissa
    if(mantissa[-1] == "1"):
        mantissa = mantissa[ : 22] + "1"
    else:
        mantissa = mantissa[ : 22] + "0"
      
    return "{:<023}".format(mantissa)



def dec_to_float32(str_number):
    ''' Function dec_to_float32() converts a number inputted as 
        string to a IEEE 754 32 bit floating point number.
        # =============================================================================
        #     @ INPUT : str_number (string) - The number to be converted to 754 format
        #     @ RETURN : string giving the sign, exponent, mantissa of the number
        #               separately
        # =============================================================================
        **Additional Info: 
        If string is 0, then send all values as 0.
        If invalid input is given, return '', '', '' ie Empty String.
        If number inputted is greater than max range or less than min range, set 
        it to infinities.    
    '''    
    # Convert the string to float using Python's builtin method float
    # Then convert the float to hexadecimal format using .hex() method
    
    
    #Check for 0, 0 is exception
    
    # try to parse, check if 0
    try:
        if( int(str_number) == 0):
            sign_bit = 1
            mantissa = "0"*23
            exponent = "0"*8
            return "sign: {} \nexponent: {} \nmantissa: {}".format(sign_bit, exponent, mantissa)
    except ValueError:
        pass
    #Try to parse float
    try:
        # Parse string to hexadecimal form
        hex_number = float(str_number).hex()
    
    except ValueError:
        return "sign: {} \nexponent: {} \nmantissa: {}".format('', '', '')
        
    
    # Get the sign_bit and the formatted number
    sign_bit, hex_number = give_sign_bit_and_convert(hex_number)
    
    # hexadecimal is of the form 0x1.<mantissa>p<exponent>
    # We remove the 0x1. from the left side and split the string with delimiter p
    hex_number = hex_number[4 : ]
    mantissa_prev, exponent_prev = hex_number.split('p')
    
    # Get Exponent
    exponent = get_exponent(exponent_prev)    
     
    # Get Mantissa
    mantissa = get_mantissa(mantissa_prev)
    
    # Handle Exceptions
    # If exponent is already 255(1111 1111) and mantissa nonzero
    # then we set it to infinities
    if exponent == bin(255)[2:] and mantissa.find("1") != -1:
        mantissa = "1" * 23   
        
    return (sign_bit, exponent, mantissa)
