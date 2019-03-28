U52 12 C 2300 = 63 = EHC XLW = 
LXZAL AGLAR RUZRQ GCLHV ATCAK XHBLI PFWMR CGHNC YCVUN CSJWA PSNUK BRODC FVBYH KAQ =

U52: station being transmitted from
C: station being transmitted to
12: day 12
2300: 11 PM
63: message is 63 characters

LXZAL: kenngruppen, or indicator
    padded with two random letters, users will have to look at the key sheet

    Indicator could be LXZ / XZA / ZAL 

Now we can get the values from the key sheet for the rotors, reflector, ring settings, and plugboard settings

``` machine = EnigmaMachine.from_key_sheet(
    rotors='II V I',
    reflector='B',
    ring_settings='07 19 02',
    plugboard_settings='HR NC IU DM TW GV FB ZL EQ OX')
```


Next the receiving operator must decrypt the message key
``` machine.set_display('EHC')
    msg_key = machine.process_text('XLW')
```

This reveals key used to encrypt the message, which is `CTF`
Now we can decrypte the original message
``` machine.set_display(msg_key) # CTF
    plaintext = machine.process_text('AGLARRUZRQGCLHVATCAKXHBLIPFWMRCGHNCYCVUNCSJWAPSNUKBRODCFVBYHKAQ')
    print(plaintext)
```


Resources:
https://py-enigma.readthedocs.io/en/latest/guide.html#example-communication-procedure
