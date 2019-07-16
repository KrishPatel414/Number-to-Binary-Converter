value=int(input("Please input a numerical value to be converted into binary"))
binary=""
if(value>=0 and value <=255):

#loop through each bit in the conversion
    for count in range(8):
        remainder=value%2
        value=value//2
        binary=str(remainder) + binary
    
    print(binary)

value=int(input("Please input a numerical value to be converted into binary"))
binary=""
if(value>=0 and value <=255):

#loop through each bit in the conversion
    for count in range(8):
        #put the remainder of the decimal divided by 2-- this is the next bit in the conversion
            binary=str(decimal%2)
        #The conversion algoristhm requires the input divided by 2
            decimal=decimal//2
 #to be divided by 2-- we must use// to divide so there are no decimals
            print(binary)
