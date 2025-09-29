#!/bin/bash

# Actualizar repositorios e instalar dependencias de Linux para Playwright
apt-get update && apt-get install -y \
    libgtk-3-0 \
    libgtk-4-1 \
    libgdk-pixbuf2.0-0 \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libatk1.0-0 \
    libcups2 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpangocairo-1.0-0 \
    libx11-xcb1 \
    libxcb1 \
    libxfixes3 \
    libxrender1 \
    libxext6 \
    libxi6 \
    libxtst6 \
    wget \
    ca-certificates \
    fonts-liberation \
    libappindicator1 \
    libatk-bridge2.0-0 \
    libatspi2.0-0 \
    libdbus-1-3 \
    libexpat1 \
    libxkbcommon0 \
    libpango-1.0-0 \
    libgstreamer-1.0-0 \
    libgstreamer-plugins-base1.0-0 \
    libvpx7 \
    libwoff2-1 \
    libxslt1.1 \
    libatomic1 \
    libopus0 \
    libflite1 \
    libwebpdemux2 \
    libavif15 \
    libharfbuzz-icu0 \
    libwebpmux3 \
    libenchant-2-2 \
    libsecret-1-0 \
    libhyphen0 \
    libnghttp2-14 \
    libgles2 \
    libx264-163

# Instalar navegadores de Playwright
playwright install

# Ejecutar la aplicación
python app.py
