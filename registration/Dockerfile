FROM ipunktbs/nginx:1.9.7-7-1.0.4

EXPOSE 80

COPY phpinfo.php /var/www/app/public/
RUN ln -s /var/www/app/public/phpinfo.php /var/www/app/public/index.php