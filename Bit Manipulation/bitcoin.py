"""
This is an exercise from:
    http://www.righto.com/2014/09/mining-bitcoin-with-pencil-and-paper.html
that demonstrates how bitcoin mining works.  It performs only a single
pass of the SHA-256 algorithm to encrypt the first 32 bits of data.

Author: Sean Strout @ RIT CS
Author: <<< Aditya Pulekar, Mandar Badave>>
"""

# constants
BITS = 32    # working with 32 bits of data

# the initial constants for SHA-256
A0 = 0x6a09e667
B0 = 0xbb67ae85
C0 = 0x3c6ef372
D0 = 0xa54ff53a
E0 = 0x510e527f
F0 = 0x9b05688c
G0 = 0x1f83d9ab
H0 = 0x5be0cd19
K = 0x428a2f98

def padIntTo32Bits(data):
    """
    Takes an integer that can be represented in 32 bits (or less), and returns
    it as a 32 bit binary string of 0's and 1's.], e.g.:

        padIntTo32Bits(11) = '0b00000000000000000000000000001011'
        padIntTo32Bits(0x6a09e667) = '0b01101010000010011110011001100111'

    :param data (int): An integer represented in 32 bits or less
    :pre: data is 32 bits or less
    :return: A 32 bit binary string
    """
    binaryString=bin(data)
    zeroPadding=34-len(binaryString)
    zeroString=""
    for _ in range(zeroPadding):
        zeroString=zeroString+"0"
    for index in range(2,len(binaryString)):
        zeroString+=binaryString[index]
    return ("0b"+zeroString)

def Ma(A, B, C):
    """
    The Ma majority box looks at the bits of A, B, and C. For each position,
    if the majority of the bits are 0, it outputs 0. Otherwise it outputs 1.
    :param A (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :param B (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :param C (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :return: A 32 bit binary string that stores the result
    """
    MajorityString="0b"
    for index in range(2,34):
        sum=0
        sum=int(A[index])+int(B[index])+int(C[index])
        if(sum>=2):
            MajorityString=MajorityString+"1"
        else:
            MajorityString=MajorityString+"0"
    return MajorityString

def rightShift(data, amount):
    """
    Right shift (rotating) a binary string by an amount, e.g.:

        rightShift('0b01101010000010011110011001100111', 2) ==
                   '0b11011010100000100111100110011001'

    This routine is used internally by Sum0() and Sum1() to
    perform the proper shifts.

    :param data (str): The 32 bit binary string to shift/rotate
    :param amount (int): The amount to shift/rotate
    :return: The resulting 32 bit binary string
    """
    BitsToBeAdjusted=""
    for index in range(34-amount,34):
        BitsToBeAdjusted+=data[index]
    for index in range(2,34-amount):
        BitsToBeAdjusted+=data[index]


    return "0b"+BitsToBeAdjusted

def Sum0(A):
    """
    Rotates the bits of A to form three rotated versions, and then sums them
    together modulo 2. In other words, if the number of 1 bits is odd, the sum
    is 1; otherwise, it is 0.  The three values in the sum are A rotated right
    by 2 bits, 13 bits, and 22 bits.

    :param A (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :return: A 32 bit binary string with the result
    """
    counter=0
    threeVersion=[2,13,22]
    StringData=[]
    X=rightShift(A,2)
    Y=rightShift(A,13)
    Z=rightShift(A,22)
    OddString=""
    for index in range(2,34):
        sum=int(X[index])+int(Y[index])+int(Z[index])
        if(sum%2!=0):
            OddString+="1"
        else:
            OddString+="0"
    return"0b"+OddString

def Ch(E, F, G):
    """
    The Ch "choose" box chooses output bits based on the value of input E. If
    a bit of E is 1, the output bit is the corresponding bit of F. If a bit
    of E is 0, the output bit is the corresponding bit of G. In this way, the
    bits of F and G are shuffled together based on the value of E.
    :param E (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :param F (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :param G (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :return: A 32 bit binary string with the result
    """
    OutputString=""
    for index in range(2,34):
        if(E[index]=="1"):
            OutputString=OutputString+F[index]
        elif(E[index]=="0"):
            OutputString=OutputString+G[index]
    return "0b"+OutputString

def Sum1(E):
    """
    This sum box rotates and sums the bits of E, similar to Sum0 except the
    shifts are 6, 11, and 25 bits.
    :param E (str): A 32 bit binary string of 0's and 1's (e.g. '0b010...')
    :return: A 32 bit binary string with the result
    """
    X=rightShift(E,6)
    Y=rightShift(E,11)
    Z=rightShift(E,25)
    OddString=""
    for index in range(2,34):
        sum=int(X[index])+int(Y[index])+int(Z[index])
        if(sum%2!=0):
            OddString+="1"
        else:
            OddString+="0"
    return"0b"+OddString

def trimTo32Bits(val):
    """
    Takes a binary string that may be larger than 32 bits and cut it down to 32
    bits by removing the extra most significant bits, e.g.:

        trim('0b111111110000010001000100001001101') ==
            '0b11111110000010001000100001001101'

    :param val (str): A binary string of 32 or greater bits
    :pre: val is >= 32 bits
    :return: A trimmed 32 bit binary string
    """
    trimmedString=""
    if(len(val)-34>0):
        BitsTrimmed=len(val)-34
        for index in range(BitsTrimmed+2,len(val)):
            trimmedString+=val[index]
        return "0b"+trimmedString
    else:
        NonTrimmedString=padIntTo32Bits(int(val,2))
        return NonTrimmedString

def main():
    """
    The main performs a single pass of SHA-256 on a 32 bit user supplied input
    :return: None
    """

    # 1. Convert the initial values for A,B,C into padded binary strings
    A, B, C= padIntTo32Bits(A0), padIntTo32Bits(B0), padIntTo32Bits(C0)
    print("A: ",A)
    print("B: ",B)
    print("C: ",C)

    #2. Compute the majority and sum0 boxes
    majority = Ma(A, B, C)
    print('Ma: bin=' + majority, ', hex=' + hex(int(majority, 2)))

    sum0 = Sum0(A)
    print('Sum0: bin=' + sum0 + ', hex=' + hex(int(sum0, 2)))

    # 3. Convert the initial values for E,F,G into padded binary strings
    E, F, G = padIntTo32Bits(E0), padIntTo32Bits(F0), padIntTo32Bits(G0)
    print("E: ",E)
    print("F: ",F)
    print("G: ",G)
    # 4. Compute the choose and sum1 boxes
    choose = Ch(E, F, G)
    print('Ch: bin=' + choose, ', hex=' + hex(int(choose, 2)))
    trim=trimTo32Bits("0b111111000010101010101010000000001010")
    print('Trimmed String: ',trim)

    sum1 = Sum1(E)
    print('Sum1: bin=' + sum1, ', hex=' + hex(int(sum1, 2)))

    # 5. Prompt the user for a 32 bit integer, w, to encrypt
    w = int(input('Enter 32 bit input, e.g. 0x02000000:'), 16)

    # 6. Compute the overall sum
    sum = trimTo32Bits(bin(w + K + H0 + int(choose, 2) + int(sum1, 2)))
    print('sum: bin=' + sum, ', hex=' + hex(int(sum, 2)))

    #7. Update to the new values for A-H

    newA = int(trimTo32Bits(bin(int(sum0, 2) + int(majority, 2) + int(sum,2))), 2)
    newB = int(A, 2)
    newC = int(B, 2)
    newD = int(C, 2)
    newE = int(trimTo32Bits(bin(D0 + int(sum,2))), 2)
    newF = int(E, 2)
    newG = int(F, 2)
    newH = int(G, 2)

    # display results
    print("newA:", hex(newA))
    print("newB:", hex(newB))
    print("newC:", hex(newC))
    print("newD:", hex(newD))
    print("newE:", hex(newE))
    print("newF:", hex(newF))
    print("newG:", hex(newG))
    print("newH:", hex(newH))

    print(int(hex(A0),16))
if __name__ == '__main__':
    main()