@echo off
chcp 65001 >nul

echo.
echo [ADIM 1] PyInstaller kuruluyor...
echo.
python -m pip install pyinstaller

echo.
echo [ADIM 2] Eski dosyalar temizleniyor...
echo.
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

echo.
echo [ADIM 3] EXE dosyası oluşturuluyor...
echo.
if exist icon.ico (
    python -m PyInstaller --onefile --windowed --icon=icon.ico --name "HashTool" hashTool.py
) else (
    python -m PyInstaller --onefile --windowed --name "HashTool" hashTool.py
)

echo.
echo [ADIM 4] Wordlist kopyalanıyor...
echo.
if not exist dist mkdir dist
if exist wordlist.txt copy wordlist.txt dist\

echo.
echo ============================================
echo TAMAMLANDI!
echo ============================================
echo.
echo EXE dosyası buradadır: dist\HashTool.exe
echo.
pause