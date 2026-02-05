FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---------------- SYSTEM DEPENDENCIES ----------------
RUN apt-get update && apt-get install -y \
    build-essential \
    ffmpeg \
    curl \
    git \
    python3-dev \
    libffi-dev \
    libssl-dev \
    pkg-config \
    ca-certificates \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# ---------------- NODEJS 18 ----------------
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs

WORKDIR /app

# ---------------- PYTHON TOOLS ----------------
RUN pip install --upgrade pip setuptools wheel

# ---------------- COPY REQUIREMENTS ----------------
COPY requirements.txt .

# ---------------- DEBUG INSTALL (PACKAGE BY PACKAGE) ----------------
RUN set -ex; \
    pip install --no-cache-dir --prefer-binary aiofiles; \
    pip install --no-cache-dir --prefer-binary aiohttp; \
    pip install --no-cache-dir --prefer-binary beautifulsoup4; \
    pip install --no-cache-dir --prefer-binary dnspython; \
    pip install --no-cache-dir --prefer-binary ffmpeg-python; \
    pip install --no-cache-dir --prefer-binary gitpython; \
    pip install --no-cache-dir --prefer-binary hachoir; \
    pip install --no-cache-dir --prefer-binary heroku3; \
    pip install --no-cache-dir --prefer-binary "httpx[http2]==0.25.2"; \
    pip install --no-cache-dir --prefer-binary motor; \
    pip install --no-cache-dir --prefer-binary numpy; \
    pip install --no-cache-dir --prefer-binary pillow==9.5.0; \
    pip install --no-cache-dir --prefer-binary psutil; \
    pip install --no-cache-dir --prefer-binary py-tgcalls==0.9.7; \
    pip install --no-cache-dir --prefer-binary pyrogram==2.0.106; \
    pip install --no-cache-dir --prefer-binary pytgcrypto; \
    pip install --no-cache-dir --prefer-binary python-dotenv; \
    pip install --no-cache-dir --prefer-binary pyyaml; \
    pip install --no-cache-dir --prefer-binary requests; \
    pip install --no-cache-dir --prefer-binary speedtest-cli; \
    pip install --no-cache-dir --prefer-binary spotipy; \
    pip install --no-cache-dir --prefer-binary unidecode; \
    pip install --no-cache-dir --prefer-binary humanize; \
    pip install --no-cache-dir --prefer-binary pykeyboard; \
    pip install --no-cache-dir --prefer-binary yt-dlp; \
    pip install --no-cache-dir --prefer-binary youtube-search; \
    pip install --no-cache-dir --prefer-binary youtube-search-python; \
    pip install --no-cache-dir --prefer-binary python-telegram-bot==13.15; \
    pip install --no-cache-dir --prefer-binary py-yt-search

# ---------------- COPY PROJECT ----------------
COPY . .

CMD ["python3", "-m", "AviaxMusic"]
