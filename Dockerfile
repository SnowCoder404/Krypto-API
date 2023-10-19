#
#   Copyright © 2023, SnowCoder404
#
FROM debian
LABEL authors='SnowCoder404'
LABEL WEBSITE='https://github.com/SnowCoder404'
ENV LANG C.UTF-8
RUN mkdir /opt/krypto-api
RUN mkdir /opt/krypto-api/templates
COPY main.py /opt/krypto-api/
COPY requirement.txt /opt/krypto-api/
COPY templates /opt/krypto-api/templates/
COPY install.sh /opt/krypto-api/
RUN bash /opt/krypto-api/install.sh