@echo off
pyinstaller main.py --onefile --icon="./icon.ico" --upx-dir=%cd%
move %cd%\dist\main.exe %cd%
ren main.exe anonuploader-sb.exe
pause
