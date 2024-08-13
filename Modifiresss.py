'''
txt = f"The price of this book is 49 dollars"
print(txt)                                            '''

'''
Book_Price = 59
txt= f"The price of this book is {Book_Price} dollars"
print(txt)                                           '''

'''
Book_Price = 59
txt = f"The price of this book  is {Book_Price:.2f} dollars"
print(txt)                                            '''

'''
#Display the value 95 with 2 decimals:
txt = f"The price of this book is {95:.2f} dollars"
print(txt)                                           '''

'''
#Performed a math operation in the placeholder, and return the result:
txt = f"The price of this book is {20 * 59} dollars"
print(txt)                                           '''

'''
#Add taxes before displaying the price:
book_price = 59
tax = 0.25
txt = f"The price of this book is {book_price + (book_price * tax)} dollars"
print(txt)                                         '''

'''
book_price = 49
txt = f"It is very {'Expensive' if book_price>50 else 'Cheap'}"
print(txt)                              '''

'''
#Use the string method upper()to convert a value into upper case letters:
fruit = "mango"
txt = f"I love {fruit.upper()}"
print(txt)                                 '''

'''
def myconverter(x):  #a function that converts feet into meters:
  return x * 0.2024

txt = f"The plane is flying at a {myconverter(70000)} meter altitude"
print(txt)                                '''

'''
#Used a comma as a thousand separator:
book_price = 59000
txt = f"The price of this book is {book_price:,} dollars"
print(txt)                                   '''

'''
#Use ">" to right-align the value:
txt = f"We have {49:>8} chickens."
print(txt)                          '''

'''
#Use ">" to right-align the value:
txt = f"We have {49:>8} chickens."
print(txt)                            '''

''' 
#Use "^" to center-align the value:
txt = f"We have {49:^8} chickens."
print(txt)                                 '''

'''   
#Use "=" to place the plus/minus sign at the left most position:
txt = f"The temperature is {-5:=8} degrees celsius."
print(txt)                                    '''

'''
#Use "+" to always indicate if the number is positive or negative:
txt = f"The temperature is between {-3:+} and {7:+} degrees celsius."
print(txt)                      '''

'''
#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):
txt = f"The temperature is between {-3:-} and {7:-} degrees celsius."
print(txt)                                             '''

'''
#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:
txt = f"The temperature is between {-3: } and {7: } degrees celsius."
print(txt)                                               '''

'''
#Use "," to add a comma as a thousand separator:
txt = f"The universe is {16400000000:,} years old."
print(txt)                                                 '''

'''
#Use "_" to add a underscore character as a thousand separator:
txt = f"The universe is {13800000000:_} years old."
print(txt)                                           '''

'''
#Use "b" to convert the number into binary format:
txt = f"The binary version of 5 is {5:b}"
print(txt)                                    '''

'''
#Use "d" to convert a number, in this case a binary number, into decimal number format:
txt = f"We have {0b101:d} chickens."
dd = f"We have {0b100:d} chickens."
bb = f"We have {0b10011:d} chickens."
aa = f"We have {0b101011:d} chickens."
print(txt)
print(dd)
print(bb)
print(aa)                       '''


'''
#Use "e" to convert a number into scientific number format (with a lower-case e):
txt = f"We have {5:e} chickens."
print(txt)                               '''

'''
#Use "E" to convert a number into scientific number format (with an upper-case E):
txt = f"We have {5:E} chickens."
print(txt)                        '''

'''
#Use "o" to convert the number into octal format:
txt = f"The octal version of 10 is {10:o}"
print(txt)                                     '''

''' 
#Use "x" to convert the number into Hex format:
txt = f"The Hexadecimal version of 255 is {255:x}"
print(txt)                                               '''

'''
#Use "X" to convert the number into Hex format:
txt = f"The Hexadecimal version of 255 is {255:X}"
print(txt)                                                '''


#Use "%" to convert the number into a percentage format:
txt = f"You scored {0.25:%}"
print(txt)
#Or, without any decimals:
txt = f"You scored {0.25:.0%}"
print(txt)














