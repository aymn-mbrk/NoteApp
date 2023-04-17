FROM ubuntu

RUN apt update
RUN apt upgrade -y
RUN apt install -y apache2
RUN apt install -y apache2-utils
RUN apt install -y pip python
ADD ./NoteApp
RUN apt-get install libpq-dev 
RUN apt clean

EXPOSE 80

CMD ["apache2ctl", "-D", "FOREGROUND"]
