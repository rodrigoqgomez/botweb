#!/bin/bash
# Instala dependencias
pip install -r requirements.txt

# Instala Chromium para Playwright
playwright install chromium

# Ejecuta tu aplicación
python app.py

