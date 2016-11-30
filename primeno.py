#Function that find numbers between 0-n
def prime_num(number):
    #The list of prime numbers
    if not isinstance(number,int):
        return "only intergers are allowed"
    if not isinstance(number,int):
        return "Dictionary not allowed"
    if not isinstance(number,int):
        return "List not allowed"
    if not isinstance(number,int):
        return "Tuples not allowed"
    if not isinstance(number,int):
        return "Set not allowed"
    if number==1:
        return "One is not a prime number"



    primenumbers=[]
    isdivisible=True
    if number<0:
        return "There are no negative prime numbers"
    else:
        for i in range(2,number+1):
            isdivisible=True
            for j in range(2,i):
                if i%j==0:# if i is divisible by j
                    isdivisible=False
            if isdivisible:
                primenumbers.append(i)
    return primenumbers





