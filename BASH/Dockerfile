FROM ubuntu:latest
 
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:auehc' | chpasswd

RUN useradd level1
RUN useradd level2
RUN useradd level3
RUN useradd level4
RUN useradd level5
RUN useradd level6
RUN useradd level7
RUN useradd level8
RUN useradd level9
RUN useradd level10

RUN echo "level1:aubie" | chpasswd
RUN echo "level2:aubie{M0m_g37_z_K@#rA}" | chpasswd 
RUN echo "level3:aubie{h1DdeN_f1Le$_R_n0_M@7cH_4_mi}" | chpasswd 
RUN echo "level4:aubie{that_w@Sn7_2_HaRD}" | chpasswd
RUN echo "level5:aubie{that_w0uLdv3_B3eN_2_Ez}" | chpasswd
RUN echo "level6:aubie{1_know_u_H8_m3_NOW}" | chpasswd
RUN echo "level7:aubie{1_swar_i'M_@_d3cEN7_person}" | chpasswd
RUN echo "level8:aubie{n0T1c3_D_difF3reNc3}" | chpasswd
RUN echo "level9:aubie{H4v1Ng_s37uId_1$_dAn6Er0us}" | chpasswd
RUN echo "level10:aubie{W0w_th@ts_@LOt_2_R3aD}" | chpasswd

COPY level1 /home/level1/README
RUN chown level1 /home/level1/README
RUN chmod 400 /home/level1/README

COPY level2 /home/level2/.hidden
RUN chown level2 /home/level2/.hidden
RUN chmod 400 /home/level2/.hidden

COPY level3 /bin/filename
RUN chown level3 /bin/filename
RUN chmod 400 /bin/filename

COPY level4 /usr/share/findme
RUN chown level4 /usr/share/findme
RUN chmod 400 /usr/share/findme

COPY level5 /home/level5/compressed
RUN chown level5 /home/level5/compressed
RUN chmod 400 /home/level5/compressed

COPY level6 /home/level6/level6
RUN chown level6 /home/level6
RUN chmod 400 /home/level6

COPY level7 /home/level7/level7
COPY level7.diff /home/level7/diff
RUN chown level7 /home/level7
RUN chown level7 /home/level7/diff

COPY level8 /home/level8/level8
COPY cat /home/level8/cat
RUN chown level9 /home/level8/level8
RUN chown level9 /home/level8/cat
RUN chmod u+s /home/level8/cat

COPY level9 /home/level9
RUN chown level9 /home/level9
RUN chmod 400 /home/level9

COPY level10 /home/level10/.findme
RUN chown level10 /home/level10/.findme
RUN chmod 400 /home/level10/.findme
RUN echo "exit" >> .bashrc

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
