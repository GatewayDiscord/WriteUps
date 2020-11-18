# Shifter Salad 
Cryptography 10 pts -> Solve by Sarastro.

This CTF is one of the easier CTFs that AFFINITY CTF has presented in its crypto session CTF panel. The name itself suggest that its a shifter and by the challenge we see that we need to find a cipher and decipher it. 
Shifter + Salad + Cipher is only meant to be a Caeasers Cipher. 

A shifter is really what the name suggests. It shifts the letters. You have a certain pattern or a shift of numbers starting from a specific point and working towards that number in an upper or lesser context. Affecting the cipher will 
get you to the plaintext. 

*AGHFXK{5ai5b1cee10z}* - cipher text. 

Since AGHFXK is not the default flag format ( AFFCTF ) we can decipher that right away.


A = A = 0 shiftes ( no changes )

F = G --> F in the alphabet is 7th and G is sixth while F is 6th. Following the previous shift and pattern we see that this one is subtracted with -1. So this would be G-1 or 7-1 = 6 or F ( In the A1Z26 alphabet cipher )

F = H --> H is 8th in the alphabet. Following the pattern from previous : 0, -1, this would be -2 and that would be -- > H-2 or 8-2 = 6 or F. 

So far so good.

C = F --> F-3 or 6-3 = 3 or C

X = T --> X-4 or 24-4 = 20  or T

You can do K for yourself.


We clearly saw the pattern. Each letter gets subtracted by -1,-2,.. as it goes when converted to the alphabetic value of itself. 

Now a problem, what to do with the numbers that are found in there, since we do not have to turn them into letters or subtitute them you can leave them be and focus on the letters.

AFFCTF{aibceez} . Now you have 2 ways to go about this,either go manually and extract each one or write a script. I will show you both ways.

![image](https://user-images.githubusercontent.com/74470185/99503638-bdb05480-297e-11eb-93fc-525488931aef.png)

### MANUALLY

A = A-6 = 1(first in the alphabet) - 6 = -5, hmm what do we do here? What would be the -1th letter. The letter -1 from A or the last letter in the alphabet Z. = Z-5 = 26-5 = 21 or U

I = I-7 = 9-7 = 2 or B

B = B-8 = 2-8 = -6 = Z-6 = 20 or T

C = C-9 = 3-9 = -6 = Z-6 = 20 or T

E = E-10 = 5-10 = -5 = Z-5 = 21 = U

E = E-11 = 5-11 = -6 = Z-6 = T

Z = Z-12 = 26-12 = 14 = N


We got UBTTUN. Some may already see it but if you do not circle back to when I said leave the numbers outside since we cannot do anything with them. Let's plock them in here

AFFCTF{5UB5T1TUT10N}

### SCRIPT

Using a script you will save some time but it's an equally good option.

```python
def cipher(symbol, shift): // shift for the given alphabet. Can be substituted
    LETTERS = 'abcdefghijklmnopqrstuvwxyz'

    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        num = num + shift
        if num >= len(LETTERS):
            num = num - len(LETTERS)
            return LETTERS[num]
        elif num < 0:
            num = num + len(LETTERS)
            return LETTERS[num]
        else:
            return LETTERS[num]
    return symbol


enc = 'aibceez' // cipher 

dec = [] // store in

cnt = 0 // starting 
for c in enc:
    dec.append(cipher(c, cnt)) / append function for the count
    cnt -= 1

print("".join(dec))
```

#### Conclusion

This CTF is very beginner friendly and a good learning experience!
