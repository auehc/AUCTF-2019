from enigma.machine import EnigmaMachine

machine = EnigmaMachine.from_key_sheet(
       rotors='II V I',
       reflector='B',
       ring_settings='07 19 02',
       plugboard_settings='HR NC IU DM TW GV FB ZL EQ OX')

init_rot_pos = 'EHC'
machine.set_display(init_rot_pos)
enc_key = machine.process_text('CTF')
print("Initial Rotor Positions: %s" % init_rot_pos)
print("Three letter message key: %s" % enc_key)

secret_key = 'CTF'
machine.set_display(secret_key)
print("Secret Key: %s" % secret_key)

#user_input = input("Please enter string to be encoded: ")
#user_input ='AGLARRUZRQGCLHVATCAKXHBLIPFWMRCGHNCYCVUNCSJWAPSNUKBRODCFVBYHKAQ'
user_input = 'Riddle me this what is always on its way here but never arrives'
enc = machine.process_text(user_input)

print("Original Message: %s" % user_input)
print("Encoded text: %s" % enc)
