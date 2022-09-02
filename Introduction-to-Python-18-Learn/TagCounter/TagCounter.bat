:: Can be used with Python embedded (portable) version

@echo off

SET mypath=%~dp0
echo %mypath%
pause
cd .\TagCounter\
..\python.exe tagcounter.py
pause