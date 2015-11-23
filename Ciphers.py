import re

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return "Doesn't exist"
    else:
        return x % m


def nicerText(line):
    line = line.replace(" ", "")
    line = line.replace(".", "")
    line = line.replace(",", "")
    line = line.replace("-", "")
    line = line.replace("!", "")
    line = line.replace("\\", "")
    line = line.replace("/", "")
    line = line.upper()
    output = []
    while line:
        output.append(line[:5])
        line = line[5:]
    return output

def add(p, b):
    l = list(p)
    string = ""
    for x in l:
        if x in letters:
            string += letters[((letters.index(x) + b)%26)].upper()
    return string

def mul(p, a):
    l = list(p)
    string = ""
    for x in l:
        if x in letters:
            string += letters[((letters.index(x)*a)%26)].upper()
    return string

def affineEncryption(p, a, b):
    l = list(p)
    string = ""
    for x in l:
        if x in letters:
            string += letters[((letters.index(x)*a + b)%26)].upper()
    return string

def letterFreq(p):
    for x in range(65,91):
        print chr(x),": ", p.count(chr(x))




keepGoing = True

while keepGoing:
    print "1. Make my text nicer"
    print "2. Get a mod inverse"
    print "3. Do additive cipher"
    print "4. Do multiplicative cipher"
    print "5. Do affine provided a and b"
    print "6. Letter frequency counter"
    print "7. Exit program"
    
    choice = int(raw_input())

    while choice not in range(1,8):
        print "\n"
        print "No gamessss, seriousness please!!"
        print "\n\n"
        print "1. Make my text nicerrrrr"
        print "2. Get a mod inverse"
        print "3. Do affine provided a and b"
        print "4. Exit program"
        choice = int(raw_input())

    if choice == 1:
        o = nicerText(raw_input("Enter the text: "))
        for x in o:
            print x,
        print "\n\n"
    elif choice == 2:
        final = modinv(int(raw_input("What is the number? ")), 26)
        print "Your mod inverse is:", final
        print "\n\n"
    elif choice == 3:
        final = nicerText(add(raw_input("Enter your secret text: ").lower(), int(raw_input("Enter b: "))))
        for x in final:
            print x,
        print "\n\n"
    elif choice == 4:
        final = nicerText(mul(raw_input("Enter your secret text: ").lower(), int(raw_input("Enter a: "))))
        for x in final:
            print x,
        print "\n\n"
    elif choice == 5:
        final = nicerText(affineEncryption(raw_input("Enter your secret text: ").lower(), int(raw_input("Enter a: ")), int(raw_input("Enter b: "))))
        for x in final:
            print x,
        print "\n\n"
    elif choice == 6:
        letterFreq(raw_input("Enter the text to count: ").upper())
        print "\n\n"
    elif choice == 7:
        print "Bye bye princess!"
        keepGoing = False
