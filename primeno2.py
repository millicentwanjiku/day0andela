#Function that find numbers between 0-n
def prime_num(number):
    #The list of prime numbers
    if not isinstance(number,int):
        return "only intergers are allowed"

    primenumbers=[]
    isdivisible=True
    if number<0:
        print "There are no negative prime numbers"
    else:
        for i in range(2,number+1):
            isdivisible=True
            for j in range(2,i):
                if i%j==0:
                    isdivisible=False
            if isdivisible==True:
                primenumbers.append(i)
    return primenumbers
print prime_num(50)
print prime_num(-5)
print prime_num("kiki")

