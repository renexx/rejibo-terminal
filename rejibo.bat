@echo off

REM Získanie aktuálnej cesty k skriptu rejibo.bat
set "REJIBO_PATH=%~dp0"

REM Vytvorenie virtuálneho prostredia
REM python -m venv venv
REM Aktivácia virtuálneho prostredia
REM call "%REJIBO_PATH%venv\Scripts\activate.bat"

REM Inštalácia závislostí
REM pip install -r "%REJIBO_PATH%requirements.txt"

REM Spustenie Python skriptu
python "%REJIBO_PATH%main.py"