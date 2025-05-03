FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    openjdk-17-jdk \
    wget \
    curl \
    git \
    openssh-server \
    python3 \
    python3-pip \
    unzip \
    xvfb \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libnspr4 \
    libnss3 \
    libxss1 \
    libxtst6 \
    software-properties-common \
    sudo

# Установка Jenkins
RUN curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | tee \
    /usr/share/keyrings/jenkins-keyring.asc > /dev/null && \
    echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian binary/ | \
    tee /etc/apt/sources.list.d/jenkins.list > /dev/null && \
    apt-get update && apt-get install -y jenkins

# Установка Chrome
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb && \
    apt install -y ./chrome.deb && rm chrome.deb

# Настройка SSH
RUN useradd -m -s /bin/bash dev && echo "dev:devpass" | chpasswd && adduser dev sudo
RUN mkdir /var/run/sshd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Копирование скриптов и установка зависимостей
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 22 8080

CMD ["/start.sh"]