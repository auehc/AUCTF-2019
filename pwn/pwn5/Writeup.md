##

# Solution
The point behind this game is to show what happens if a programmer does not properly check user input. If one goes to the bank and asks to deposit money there is a check to see if the money the user is requesting to deposit is less than the users wallet. So if the user has 10 dollars in his wallet and deposits 6 it passes, if he passes 11 it fails. However the programmer failed to check what would happen if the user passed a negative number.

When the user passes a normal number like 6 this is what happens.
```
user_input = 6
user_wallet = 10
if user_input <= user_wallet: # Passes
    user_bank_account += user_input
    user_wallet -= user_input
```
Therefore his bank account is now 6 dollars more and his wallet is 6 less.

However if we pass a negative number this happens
```
user_input = -15
user_wallet = 10
if user_input <= user_wallet: # Passes
    user_bank_account += user_input # A positive plus a negative results in subtraction, so in this case his bank account lowers
    user_wallet -= user_input   # A postitive minus a negative results in addition, so in this case his wallet increase
```
Now user_bank_account will be 15 dollars less, and his wallet will be 15 dollar more.

# Flag
aubie{logical_error}