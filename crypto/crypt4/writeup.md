# jack and Jill
====================

Hill cipher

## Hint
Think matrixes. NOTE: Flag is not in standard format.

## Key Text
auburnuniversity

## Ciphertext
nystkltiwlvazrwdmscs

## Plaintext
morethanmeetstheeyes

### Solution
Convert keytext into 4x4 matrix read from left-right top-bottom.
Convert cipher text into 5 column vectors. Multiply the inverse
of the keytext matrix with the column vectors to get the plaintext.
