def countVowels(string):
    
    vowels =['a','e','i','o','u']
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1   
    return count
        

def main():
    string = input('Enter String: ')
    print(countVowels(string))

if __name__=='__main__':
    main()