FROM ubuntu:latest

RUN apt update
RUN apt install -y socat 
RUN groupadd ctf

RUN mkdir /pwn

COPY game.py /pwn/pwn5.py
COPY entry.sh /pwn/entry.sh

RUN useradd -G ctf --home=/pwn pwnuser
RUN useradd -G ctf --home=/pwn pwnflag

RUN chown pwnflag:pwnflag /pwn/pwn5.py
RUN chown pwnflag:pwnflag /pwn

RUN chmod 4755 /pwn/pwn5.py
RUN chmod 4755 /pwn/entry.sh

EXPOSE 8004
ENTRYPOINT ["/pwn/entry.sh"]
