FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt install -y apache2 
RUN apt install -y apache2-utils
RUN apt install -y python
RUN apt install -y pip

RUN apt clean 

EXPOSE 80

CMD [“apache2ctl”, “-D”, “FOREGROUND”]
