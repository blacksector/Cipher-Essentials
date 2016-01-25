import string

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
    line = line.translate(string.maketrans("",""), string.punctuation)
    line = line.upper()
    output = []
    while line:
        output.append(line[:5])
        line = line[5:]
    return output

def isValid(a):
    if (a%2 == 0) or a == 13:
        return False
    else:
        return True

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

def affineDecryption(p, a, b):
    l = list(p)
    string = ""
    a = modinv(a,26)
    for x in l:
        if x in letters:
            string += letters[((a*(letters.index(x) - b))%26)].upper()

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
    print "6. Do affine decryption provided a and b"
    print "7. Letter frequency counter"
    print "8. Make z = 0 reverse to original"
    print "9. Exit program"
    
    choice = int(raw_input())

    while choice not in range(1,10):
        print "\n"
        print "No gamessss, seriousness please!!"
        print "\n\n"
        print "1. Make my text nicer"
        print "2. Get a mod inverse"
        print "3. Do additive cipher"
        print "4. Do multiplicative cipher"
        print "5. Do affine provided a and b"
        print "6. Do affine decryption provided a and b"
        print "7. Letter frequency counter"
        print "8. Make z = 0 reverse to original"
        print "9. Exit program"
        choice = int(raw_input())

    if choice == 1:
        o = nicerText(raw_input("Enter the text: "))
        for x in o:
            print x,
        print "\n\n"
    elif choice == 2:
        final = modinv(int(raw_input("What is the number? ")), int(raw_input("Mod by what? ")))
        print "Your mod inverse is:", final
        print "\n\n"
    elif choice == 3:
        final = nicerText(add(raw_input("Enter your secret text: ").lower(), int(raw_input("Enter b: "))))
        for x in final:
            print x,
        print "\n\n"
    elif choice == 4:
        text = raw_input("Enter your secret text: ").lower()
        a = int(raw_input("Enter a: "))
        if isValid(a):
            final = nicerText(mul(text, a))
            for x in final:
                print x,
            print "\n\n"
        else:
            print "Invalid a!\n\n"    
    elif choice == 5:

        text = raw_input("Enter your secret text: ").lower()
        a = int(raw_input("Enter a: "))
        if isValid(a):
            final = nicerText(affineEncryption(text, a, int(raw_input("Enter b: "))))
            for x in final:
                print x,
            print "\n\n"
        else:
            print "Invalid a!\n\n"       
    elif choice == 6:
        text = raw_input("Enter your secret text: ").lower()
        a = int(raw_input("Enter a: "))
        if isValid(a):
            final = nicerText(affineDecryption(text, a, int(raw_input("Enter b: "))))
            for x in final:
                print x,
            print "\n\n"
        else:
            print "Invalid a!\n\n" 
    elif choice == 7:
        letterFreq(raw_input("Enter the text to count: ").upper())
        print "\n\n"
    elif choice == 8:
        if letters[-1] == "z":
            del letters[-1]
            letters.insert(0, "z")
            print "z is now 0\n\n"
        else:
            del letters[0]
            letters.append("z")
            print "z is now the last letter\n\n"
            
    elif choice == 9:
        print "Bye bye"
        keepGoing = False




    
