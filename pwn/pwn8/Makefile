all: pwn

pwn: simple_shell.c
	gcc -fno-stack-protector shell.c -m32 -z execstack -o pwn8
