FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt install -y apache2 apache2-utils python pip

RUN apt clean 

EXPOSE 80

CMD [“apache2ctl”, “-D”, “FOREGROUND”]
