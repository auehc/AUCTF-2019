#Secret

## Solution
You can go about this challenge a few ways. The way I solved it was with Sleuth Kit
Running fls on the image will give us the files of the partition located at offset 0. 

Here we can see a few files
Running
`icat -r secret.dd <inode> > <filename>`

Will recover our files for us. The png is a misdirection with the flag being hid in the zip file. However it is encrypted. Pulling out the hash with zip2john and running the hash through John wil give us the password!

## Flag
aubie{plaid_stole_this_from_me}
