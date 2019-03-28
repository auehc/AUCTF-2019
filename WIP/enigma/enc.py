from enigma.machine import EnigmaMachine

machine = EnigmaMachine.from_key_sheet(
       rotors='V II I',
       reflector='B',
       ring_settings='17 18 26',
       plugboard_settings='UN HT WQ RS DF VI GP XZ MY AK')

c = 'YRS'
machine.set_display(c)
user_input = input("Please enter string to be encoded: ")
enc = machine.process_text(user_input)
machine.set_display(c)
dec = machine.process_text(enc)

print("Encoded text: %s" % enc)
print("Decoded text: %s" % dec.lower().replace('x', ' '))