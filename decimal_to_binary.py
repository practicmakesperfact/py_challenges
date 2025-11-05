
def D_to_B(number):
   
   remainderList =[]
  
   while number > 0:
       quotient = number // 2
       remainder = number % 2
       remainderList.append(str(remainder))
       number = quotient

   result = ''.join(reversed(remainderList)) 
   print(result)

# best way 
# def D_to_Simple(number):
    
#     binary_str = ''
#     if number == 0:
#         return '0'
#     while number > 0:
#         remainder = number % 2
#         binary_str = str(remainder) + binary_str

#         number = number//2
#     return binary_str

       
       

def main():

    D_to_B(int(input('Plase enter number: ')))
    # D_to_Simple(int(input('Plase enter number: ')))

if __name__=='__main__':
    main()
