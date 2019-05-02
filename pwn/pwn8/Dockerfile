FROM 32bit/ubuntu:16.04

RUN apt update
RUN apt install -y socat
RUN groupadd ctf

RUN mkdir /pwn

COPY entry.sh /pwn/entry.sh
COPY pwn8 /pwn/
COPY flag.txt /pwn/flag.txt

RUN useradd -G ctf --home=/pwn pwnuser
RUN useradd -G ctf --home=/pwn pwnflag

RUN chown pwnflag:pwnflag /pwn/flag.txt
RUN chown pwnflag:pwnflag /pwn/pwn8
RUN chown pwnflag:pwnflag /pwn

RUN chmod 4755 /pwn/pwn8
RUN chmod 444 /pwn/flag.txt
RUN chmod 4755 /pwn/entry.sh

EXPOSE 8007
CMD ["/pwn/entry.sh"]
