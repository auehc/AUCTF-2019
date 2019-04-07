FROM ubuntu:latest

RUN apt update; apt install -y socat

RUN groupadd ctf

RUN mkdir /simple

COPY simple.sh /simple
COPY flag.txt /simple
COPY entry.sh /simple
RUN touch /simple/ex

RUN useradd -G ctf --home=/simple simpleuser
RUN useradd -G ctf --home=/simple simpleflag

RUN chown simpleflag:simpleflag /simple/flag.txt
RUN chown simpleflag:simpleflag /simple/simple.sh
RUN chown simpleflag:simpleflag /simple
RUN chown simpleuser:simpleuser /simple/ex

RUN chmod 4755 /simple/simple.sh
RUN chmod 444 /simple/flag.txt
RUN chmod 4755 /simple/entry.sh
RUN chmod 711 /simple/ex

EXPOSE 8001

ENTRYPOINT ["/simple/entry.sh"]
