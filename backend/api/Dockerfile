FROM python:3.10-slim

ENV TZ=Asia/Seoul \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl bash ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# pixi 설치
RUN curl -fsSL https://pixi.sh/install.sh | PIXI_BIN_DIR=/usr/local/bin PIXI_NO_PATH_UPDATE=1 bash

# backend 폴더를 작업 디렉토리로
WORKDIR /app/backend

# 의존성 정의 먼저 복사(레이어 캐시 유리)
COPY pixi.toml pixi.lock ./

# api 환경 설치
RUN pixi install -e api --frozen

# 앱 코드 복사
COPY api ./api

EXPOSE 8000

# src/main.py가 uvicorn.run() 실행
CMD ["/app/backend/.pixi/envs/api/bin/python", "/app/backend/api/src/main.py"]