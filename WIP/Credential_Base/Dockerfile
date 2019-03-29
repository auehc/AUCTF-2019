FROM php:7.0-apache

COPY index.html /var/www/html
COPY AU.png /var/www/html
COPY source.php /var/www/html

EXPOSE 80

RUN service apache2 start
RUN chmod 755 /var/www/html
RUN chmod 755 /var/www/html/*
