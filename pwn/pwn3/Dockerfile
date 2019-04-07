FROM 32bit/ubuntu:16.04

RUN apt update
RUN apt install -y socat 
RUN groupadd ctf

RUN mkdir /pwn

COPY jailbreak.py /pwn/pwn3.py
COPY entry.sh /pwn/entry.sh
COPY flag.txt /pwn

RUN useradd -G ctf --home=/pwn pwnuser
RUN useradd -G ctf --home=/pwn pwnflag

RUN chown pwnflag:pwnflag /pwn/pwn3.py
RUN chown pwnflag:pwnflag /pwn
RUN chown pwnflag:pwnflag /pwn/flag.txt

RUN chmod 4755 /pwn/pwn3.py
RUN chmod 444 /pwn/flag.txt
RUN chmod 4755 /pwn/entry.sh

EXPOSE 8002
ENTRYPOINT ["/pwn/entry.sh"]
