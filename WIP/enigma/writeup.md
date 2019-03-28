We are giving a sound file that contains a morse code message. Converting it to ASCII we get

`U52????12????C????2300????=????63????=????EHC????XLW????=????LXZAL????AGLAR????RUZRQ????GCLHV????ATCAK????XHBLI????PFWMR????CGHNC????YCVUN????CSJWA????PSNUK????BRODC????FVBYH????KAQ????=`

After removing the padding we we get:

```
U52 12 C 2300 = 63 = EHC XLW = 
LXZAL AGLAR RUZRQ GCLHV ATCAK XHBLI PFWMR CGHNC YCVUN CSJWA PSNUK BRODC FVBYH KAQ = 
```
![Flyer](https://github.com/nadroj-isk/AUCTF-2019/blob/master/WIP/enigma/flyer.jpg)

Looking at the picture give to use with the challenge, pasted above we can perform a reverse image search and figure out that this is a code sheet for enigma.

The normal syntax for a code being translated is that it starts with the station the message is being transmitted from, then the day of the month, then the station it is being sent to, and then the time it is being sent and the padded indicator. So for this challenege we can get these variables:

```
station being transmitted from: U52
station being transmitted to: C
day of the month: 12 PM
time: 2300 hours or 11 PM
message size: 63 characters
padded indicator: LXZAL
```

The indicator is padded with two random letters therefore the actual indicator could be LXZ / XZA / ZAL 

The user would have to look at the code sheet to find the actual indicator. Since this is the 12th day you can look at the 12th record to see that `XZA` is the actual indicator. 

Now we can get the values from the key sheet for the rotors, reflector, ring settings, and plugboard settings based on the record in the key sheet. Below is code to setup an enigma machine using Pythons Py-Enigma Library

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
