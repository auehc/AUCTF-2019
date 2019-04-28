# FAT Analysis

What are the names of the user generated files on this image?

## Solution

Using a toolset like sleuth kit finding this information is fairly trivial.
Running `mmls` on the fat image we can see that there are three partitions starting at sectors 2048, 202049, and 402050.

Running `fls fat.dd -o 2048` for the first parititon we can see it has no files

Running `fls -o 12288 Gottem.dd` for the second partition we can see that there are 4 files.

Running `fls -o 12288 Gottem.dd` for the third partition we can see that there is a recycling bin

Running `fls -o 22528 FinalExam.dd 66-144-2` we can see that there are 2 directories

Running `fls -o 22528 FinalExam.dd 68-144-2` we can see inside the file folder and there are 2 files.

Running `fls -o 32768 FinalExam.dd` for the fourth partition we can see there are two more files.

## Flag
95 Theses.pdf, Gullivers Travels.pdf, NothingToSeeHere, Puss and Boots.jpg, Shriek.jpg, The Count of Monte Cristo.pdf, The Raven.pdf, Yoda
