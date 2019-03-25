FROM php:7.0-apache

COPY index.html /var/www/html
COPY .htaccess /var/www/html
COPY robots.php /var/www/html

EXPOSE 80

RUN service apache2 start
RUN echo "<Directory /var/www/html>" >> /etc/apache2/sites-available/000-default.conf
RUN echo "Options Indexes FollowSymLinks" >> /etc/apache2/sites-available/000-default.conf
RUN echo "AllowOverride All" >> /etc/apache2/sites-available/000-default.conf
RUN echo "Require all granted" >> /etc/apache2/sites-available/000-default.conf
RUN echo "</Directory>" >> /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite
RUN service apache2 restart

RUN chmod 755 /var/www/html
RUN chmod 755 /var/www/html/*
