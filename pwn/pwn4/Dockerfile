FROM ubuntu:latest

RUN apt update
RUN apt install -y socat 
RUN apt install -y python3
RUN groupadd ctf

RUN mkdir /pwn

COPY jail_v2.py /pwn/pwn4.py
COPY entry.sh /pwn/entry.sh

RUN useradd -G ctf --home=/pwn pwnuser
RUN useradd -G ctf --home=/pwn pwnflag

RUN chown pwnflag:pwnflag /pwn/pwn4.py
RUN chown pwnflag:pwnflag /pwn

RUN chmod 4755 /pwn/pwn4.py
RUN chmod 4755 /pwn/entry.sh

EXPOSE 8003
ENTRYPOINT ["/pwn/entry.sh"]
