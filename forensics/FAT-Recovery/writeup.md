# FAT Recovery

It would seem that we have accidently deleted a file containing valuable information. Could you please recover it for us?

# Solution

Using Sleuth kit this is a fairly easy process.

Start by figuring out how the partitions are setup for this image by running mmls
`mmls recover.dd`

Here we can see that there is only one partition 
