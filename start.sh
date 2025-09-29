#!/bin/bash

# Instalar dependencias de Playwright
apt-get update && apt-get install -y \
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
    libpango-1.0-0

# Instalar navegadores de Playwright
playwright install

# Ejecutar tu aplicación
python app.py
