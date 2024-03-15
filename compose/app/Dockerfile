FROM python:3.11.8-bullseye
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update &&\
    apt-get upgrade -y &&\
    apt-get install -y \
		liblzma-dev \
    build-essential \
    cmake \
    curl \
    freetds-bin \
    gcc \
    git \
    krb5-user \
    ldap-utils \
    libbz2-dev \
    libffi-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsasl2-2 \
    libsasl2-modules \
    libsqlite3-dev \
    libssl-dev \
    libssl1.1 \
    llvm \
    locales  \
    lsb-release \
    sasl2-bin \
    sqlite3 \
    unixodbc \
    vim \
    wget \
    xz-utils \
    zlib1g-dev \
    tk-dev

ENV RYE_NO_AUTO_INSTALL=1
RUN curl -sSf https://rye-up.com/get | RYE_INSTALL_OPTION="--yes" bash
RUN /root/.rye/shims/rye pin 3.11.8
ENV PYPI=https://mirrors.cloud.tencent.com/pypi/simple
RUN pip install -U pip -i $PYPI
WORKDIR /opt/tifa
COPY . .
RUN --mount=type=cache,target=/root/.cache /root/.rye/shims/rye sync
CMD ["start"]
