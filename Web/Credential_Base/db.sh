service mysql start && mysql -uroot -e "CREATE DATABASE SqliDB; CREATE USER 'sqli-user'@'localhost' IDENTIFIED BY 'AndThatDudeBryceBrown'; GRANT ALL PRIVILEGES ON SqliDB.* TO 'sqli-user'@'localhost'; USE SqliDB; CREATE TABLE login(User varchar(20), Password varchar(100)); INSERT INTO login (User, Password) VALUES ('admin', 'dGhpc2lzYWElY2VudGx5bG9uZ3Bhc3N3b3Jk'); INSERT INTO login (User, Password) VALUES ('aubie',{is_this_the_flag}'); SET PASSWORD FOR root@'localhost' = PASSWORD('1234567890qwertyuiopasdfghjklzxcvbnm')";

apache2 -D FOREGROUND
