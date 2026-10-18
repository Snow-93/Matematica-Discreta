@echo off
rem Usa "py" si existe; si no, "python".
set PY=py
py --version >nul 2>&1
if errorlevel 1 set PY=python
echo Usando: %PY%
%PY% --version
if errorlevel 1 goto sinpython
echo.
echo === Instalando lo necesario ===
%PY% -m pip install "ttkbootstrap<2" nodemon pyinstaller
if errorlevel 1 goto error
echo.
echo === Compilando (puede tardar 1 o 2 minutos) ===
%PY% -m PyInstaller --onefile --windowed --name ProyectoMatDiscreta --paths arbol --hidden-import interfaz --hidden-import arbol --hidden-import PIL._tkinter_finder --collect-all ttkbootstrap --collect-all nodemon menu.py
if errorlevel 1 goto error
echo.
echo LISTO. El programa esta en la carpeta dist: dist\ProyectoMatDiscreta.exe
pause
exit /b 0
:sinpython
echo.
echo No se encontro Python. Instale Python desde python.org y marque "Add python.exe to PATH".
pause
exit /b 1
:error
echo.
echo Algo fallo. Copie el mensaje de error de arriba.
pause
