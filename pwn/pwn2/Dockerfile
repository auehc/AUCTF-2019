FROM ubuntu:latest

RUN apt update; apt install -y socat

RUN groupadd ctf

RUN mkdir /pwn

COPY simple.sh /pwn/pwn2
COPY flag.txt /pwn
COPY entry.sh /pwn
RUN touch /pwn/ex

RUN useradd -G ctf --home=/pwn pwnuser
RUN useradd -G ctf --home=/pwn pwnflag

RUN chown pwnflag:pwnflag /pwn/flag.txt
RUN chown pwnflag:pwnflag /pwn/pwn2
RUN chown pwnflag:pwnflag /pwn
RUN chown pwnuser:pwnuser /pwn/ex

RUN chmod 4755 /pwn/pwn2
RUN chmod 444 /pwn/flag.txt
RUN chmod 4755 /pwn/entry.sh
RUN chmod 711 /pwn/ex

EXPOSE 8001

ENTRYPOINT ["/pwn/entry.sh"]
