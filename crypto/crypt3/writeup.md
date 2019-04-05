# Ronald's Wacky Encryption Scheme

I hope you guys like prime numbers! Do you think you can find my secrets?

`(2608201, 7)`

`(1693753, 1481467, 2425603, 2505721, 1481467, 1373315)`

## Solution

q and p both must be prime numbers. Therefore the given n (2608201) must be able to be factorized into two prime numbers
    q = 523
    p = 4987
    
    n = 2608201

r = (p-1)*(q-1) = 2602692

To get K we need a number that is equal to 1 % r and can also be factored
    Note that there are a variety of choices, but only one will work
    k = 33834997

From K we can derive e and d, which are numbers relatively prime to N
    e = 7
    d = 4833571

From here we can encode/decode the numbers

Encode:
    cipher = (msg)^e % n

Decode
    msg = (cipher)^d % N

encoded values = 1693753 1481467 2425603 2505721 1481467 1373315
decoded values = 77 64 76 64 66

## Flag
matlab