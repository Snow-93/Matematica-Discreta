@echo off
rem Abre el programa del Proyecto No. 2 con doble clic.
cd /d "%~dp0"
set PY=py
py --version >nul 2>&1
if errorlevel 1 set PY=python
%PY% --version >nul 2>&1
if errorlevel 1 goto sinpython
%PY% menu.py
if errorlevel 1 pause
exit /b 0
:sinpython
echo No se encontro Python. Instale Python desde python.org
echo y marque "Add python.exe to PATH".
pause
