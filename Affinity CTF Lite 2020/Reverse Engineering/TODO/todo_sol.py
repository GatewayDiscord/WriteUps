import string

#SOLUTION BY NERDY (Twitter: Greeg007), A part of Gateway CTF Team

def encode(msg):
    output = ''

    for i in range(len(msg)):
        temp = ord(msg[i]) * 0x40
        temp = temp >> 4
        if 0xc0 <= temp < 0xe8:
            output = str(int(msg[i]) * 0x1234) + output
        else:
            output = chr(ord(msg[i]) * 0x10) + output

    return output


# TODO implement the decode function
def decode(output):
    m = {}

    for i in string.printable:
        m[encode(i)] = i
    print(m)

    msg = ''

    x = ''

    for i in range(len(output)):
        x += output[i]
        try:
            msg += m[x]
            x = ''
        except:
            continue
        
    return msg


def shift(msg):
    j = len(msg) - 1
    output = ''

    for i in range(len(msg)//2):
        output += msg[i] + msg[j]
        j -= 1

    return output


# TODO implement the unshift function
def unshift(msg):
    fwd = ''
    rev = ''

    for i in range(len(msg)):
        if i % 2 == 0: 
            fwd += msg[i]
        else:
            rev += msg[i]
    return rev[::-1] + fwd

if __name__ == '__main__':
    # shifted = shift('<REDACTED>')
    # hashed = encode(shifted)
    hashed = '4660۠ܰ4660ڀ٠װװސ23300۰ސݐ18640ܠݰװۀڠ18640۰ްؠѠȐՀȐа4660ѠȐѠߐА'
    # CODE HERE
    d = decode(hashed)
    print(unshift(d))

