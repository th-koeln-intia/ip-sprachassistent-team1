FROM python:3.8-slim-buster

ARG USER=docker
ARG FOLDER=/home/$USER
ARG VENV=venv
ARG FOLDER_NAME=hermesLedControl

RUN set -ex && adduser --uid 1000 --disabled-password --gecos '' $USER && \
	addgroup --gid 997 --system gpio && \
	addgroup --gid 999 --system spi && \
	usermod -a -G gpio,spi $USER

WORKDIR /home/docker
RUN set -ex && \
	apt-get update && apt-get install -y \
	git \
	wget \
	tar \
	mosquitto \
	mosquitto-clients \
	portaudio19-dev \
	python3-numpy \
	python3-pip && \
	rm -rf /var/lib/apt/lists/* && \
	pip3 --no-cache-dir install virtualenv
RUN set -ex && \
	mkdir -p ${FOLDER_NAME} && \
	wget https://api.github.com/repos/project-alice-assistant/HermesLedControl/tarball/v2.0.9 -O tarball.tar.gz && \
	tar -xvf tarball.tar.gz -C ${FOLDER_NAME} --strip-components=1 && \
	rm tarball.tar.gz && \
	mkdir -p ${FOLDER}/${FOLDER_NAME}/logs && \
	chown -R ${USER} ${FOLDER}/${FOLDER_NAME}

USER $USER

RUN set -ex && \
	virtualenv -p python3 ${FOLDER}'/'${FOLDER_NAME}'/'${VENV}

ENV PATH="${FOLDER}'/'${FOLDER_NAME}'/'${VENV}/bin:$PATH"

RUN	pip3 --no-cache-dir install RPi.GPIO && \
	pip3 --no-cache-dir install spidev && \
	pip3 --no-cache-dir install gpiozero && \
	pip3 --no-cache-dir install paho-mqtt && \
	pip3 --no-cache-dir install toml

WORKDIR ${FOLDER}/${FOLDER_NAME}

ENTRYPOINT python3 main.py ${HLC_ARGUMENTS}