from enigma.machine import EnigmaMachine
import random

def randomlist(length, list):
    out_list = ''
    for i in range(length):
        rand = random.randint(0, len(list) - 1)
        out_list += list[rand]
        if i < length - 1:
            out_list += " " 
    return out_list

def position_guess(list):
    out_list = ''
    for i in range(3):
        rand = random.randint(0, len(list) - 1)
        out_list += list[rand]
    return out_list

def plugboard_gen(list):
    out_list = ''
    i = 0
    used_list = []
    while len(out_list) <= 28:
        if i == 2:
            out_list += " "
            i = 0
        character = list[random.randint(0, len(list) - 1)]
        if character not in used_list:
            used_list += character
            out_list += character
            i += 1
            
    return out_list


rotors = ['I', 'II', 'III', 'IV', 'V', 'V']
rotors_len = 3

reflectors = ['B', 'C']
reflectors_len = 1

rings = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '23', '24', '25', '26']
rings_len = 3

positions = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
positions_len = 3

plugins = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
plugins_len = 10

encrypted = True

encrypted_text = 'PHMBY'
expected_output = 'riddl'

while encrypted:
    rotor_in = randomlist(rotors_len, rotors)
    reflectors_in = randomlist(reflectors_len, reflectors)
    rings_in = randomlist(rings_len, rings)
    positions_in = position_guess(positions)
    plugins_in = plugboard_gen(plugins)
    
    '''
    rotor_in ='IV V I'
    reflectors_in ='B'
    rings_in='21 15 16'
    plugins_in ='AC LS BQ WN MY UV FJ PZ TR OK'
    positions_in = 'ABC'
    '''

    machine = EnigmaMachine.from_key_sheet(
       rotors= rotor_in,
       reflector= reflectors_in,
       ring_settings= rings_in,
       plugboard_settings= plugins_in)

    machine.set_display(positions_in)
    decrypt = machine.process_text(encrypted_text)
    print(decrypt)
    if decrypt.upper() == expected_output.upper():
        print("Rotors: %s" % rotor_in)
        print("Reflector: %s" % reflectors_in)
        print("Position: %s" % positions_in)
        print("Rings: %s" % rings_in)
        print("Plugboard: %s" % plugins_in)
        encrypted = False


