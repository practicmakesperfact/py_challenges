
def D_to_Simple(number):
    
    binary_str = ''
    if number == 0:
        return '0'
    while number > 0:
        remainder = number % 2
        binary_str = str(remainder) + binary_str

        number = number//2
    return binary_str

       
       

def main():

   
    print(D_to_Simple(int(input('Plase enter number: '))))

if __name__=='__main__':
    main()
