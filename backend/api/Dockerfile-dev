FROM python:3.10-slim
ENV TZ=Asia/Seoul

RUN apt-get update && apt-get install -y --no-install-recommends curl bash procps ca-certificates git openssh-client && rm -rf /var/lib/apt/lists/*

RUN update-ca-certificates

RUN curl -fsSL https://pixi.sh/install.sh | PIXI_BIN_DIR=/usr/local/bin PIXI_NO_PATH_UPDATE=1 bash

CMD ["sleep", "infinity"]
