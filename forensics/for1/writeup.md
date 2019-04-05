# Astrosaurs

## Solution

For this challenge we are given a jpg called secret and we are told that there are secrets inside. The name of the challenge is Astrosaurs which is a reference to a series of children's novels written about a stegosarus. A Common Digital Forensics information process is called steganography. If we now have the hint that this challenge is hiding secrets and is using steganography we may want to see if this file is secretly zipped

Running `unzip secret.jpg` will give us a folder called `Secrets` and inside secret is a file called `secrets.png` which contains the flag

## Flag
aubie{w3Lc0Me_t0_F0r3nS1cS}