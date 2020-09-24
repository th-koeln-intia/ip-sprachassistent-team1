FROM python:3.8-slim

ARG USER=docker
ARG FOLDER=/home/$USER
ARG FOLDER_NAME=hermesLedControl

RUN set -ex && adduser --uid 1000 --disabled-password --gecos '' $USER && \
	addgroup --gid 997 --system gpio && \
	addgroup --gid 999 --system spi && \
	usermod -a -G gpio,spi $USER

WORKDIR /home/docker
RUN set -ex && \
	apt-get update && apt-get install -y --no-install-recommends \
	git \
	wget \
	tar \
	gcc \
	mosquitto \
	mosquitto-clients \
	portaudio19-dev \
	python3-numpy \
	python3-pip && \
	mkdir -p ${FOLDER_NAME} && \
	wget https://api.github.com/repos/project-alice-assistant/HermesLedControl/tarball/v2.0.9 -O tarball.tar.gz && \
	tar -xvf tarball.tar.gz -C ${FOLDER_NAME} --strip-components=1 && \
	rm tarball.tar.gz && \
	mkdir -p ${FOLDER}/${FOLDER_NAME}/logs && \
	chown -R ${USER} ${FOLDER}/${FOLDER_NAME} && \
	rm -rf /var/lib/apt/lists/* && \
	apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false

USER $USER

RUN	pip3 --no-cache-dir install RPi.GPIO && \
	pip3 --no-cache-dir install spidev && \
	pip3 --no-cache-dir install gpiozero && \
	pip3 --no-cache-dir install paho-mqtt && \
	pip3 --no-cache-dir install toml

WORKDIR ${FOLDER}/${FOLDER_NAME}

ENTRYPOINT python3 main.py ${HLC_ARGUMENTS}