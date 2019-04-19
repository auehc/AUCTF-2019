FROM debian:latest

RUN apt update
RUN apt install -y socat 
RUN groupadd ctf

RUN mkdir /pwn

COPY pwn6 /pwn/
COPY entry.sh /pwn/entry.sh
COPY flag.txt /pwn
COPY key.txt /pwn
COPY secret.txt /pwn

RUN useradd -G ctf --home=/pwn pwnuser
RUN useradd -G ctf --home=/pwn pwnflag

RUN chown pwnflag:pwnflag /pwn/pwn6
RUN chown pwnflag:pwnflag /pwn
RUN chown pwnflag:pwnflag /pwn/flag.txt
RUN chown pwnflag:pwnflag /pwn/secret.txt
RUN chown pwnflag:pwnflag /pwn/key.txt

RUN chmod 4755 /pwn/pwn6
RUN chmod 444 /pwn/flag.txt
RUN chmod 444 /pwn/secret.txt
RUN chmod 444 /pwn/key.txt
RUN chmod 4755 /pwn/entry.sh

EXPOSE 8005
ENTRYPOINT ["/pwn/entry.sh"]
