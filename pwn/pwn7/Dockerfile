FROM ubuntu:latest

RUN apt update
RUN apt install -y socat 
RUN groupadd ctf

RUN mkdir /pwn

COPY pwn7 /pwn/pwn7
COPY entry.sh /pwn/entry.sh

RUN useradd -G ctf --home=/pwn pwnuser
RUN useradd -G ctf --home=/pwn pwnflag

RUN chown pwnflag:pwnflag /pwn/pwn7
RUN chown pwnflag:pwnflag /pwn

RUN chmod 4755 /pwn/pwn7
RUN chmod 4755 /pwn/entry.sh

EXPOSE 8006
ENTRYPOINT ["/pwn/entry.sh"]
