FROM ubuntu
RUN apt clean
RUN apt-get update && apt install apache2 python3 pip libpq-dev apache2-dev -y \
        && pip3 install --upgrade pip


COPY --chmod=775 ./app /var/www/app
RUN pip install -r /var/www/app/requirements.txt
RUN mv /var/www/app/flask-noteapp.conf /etc/apache2/sites-available/


RUN pip install mod_wsgi
RUN mod_wsgi-express module-config > /etc/apache2/mods-available/wsgi.load
RUN a2enmod wsgi
RUN a2dissite 000-default.conf
RUN a2ensite flask-noteapp.conf

RUN apt clean

EXPOSE 80

CMD ["apache2ctl", "-D", "FOREGROUND"]
