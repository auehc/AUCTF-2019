FROM php:7.0-apache

RUN mkdir /var/www/html/.hidden
RUN mkdir /var/www/html/.hidden/uploads

COPY index.html /var/www/html
COPY restaurantcurrysecrets.php /var/www/html/.hidden
COPY tryme.php /var/www/html/.hidden/uploads

EXPOSE 80
RUN chmod 755 /var/www/html
RUN chmod 755 /var/www/html/*
