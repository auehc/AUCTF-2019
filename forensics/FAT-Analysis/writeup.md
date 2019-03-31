# FAT Analysis

1. What are the partitions listed on this image? (list them in alphabetical order)

2. What are the files listed on the third partition? (list them in alphabetical order)

3. How many deleted files in total are there?

4. How many active files in total are there?

# Solution

Using a toolset like sleuth kit finding this information is fairly trivial.
Running `mmls` on the fat image we can see that there are three partitions starting at sectors 2048, 202049, and 402050.

Running `fsstat fat.dd -o 2048` for the first parititon we can see that the partitions name is SEC PICS

Running `fls fat.dd -o 2048' we can see that there are 7 files, 4 active and 3 being deleted.

Running 'fstat fad.dd -o 202049' for the second partition we can see that the name is CLASSICS

Running `fls fat.dd -o 202049' we can see that there are 4 files, 1 active and 3 deleted

Running 'fstat fad.dd -o 402050' for the third partition we can see that the name is gifs

Running `fls fat.dd -o 402050' we can see that there are 2 deleted files, with their names being minion.gif and banana.gif

# Flag
classics, gifs, sec | banana.gif, minion.gif | 8 | 5
