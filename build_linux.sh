#!/bin/bash
set -e

echo ""
echo "[ADIM 1] PyInstaller kuruluyor/güncelleniyor..."
echo ""
python3 -m pip install --upgrade pyinstaller

echo ""
echo "[ADIM 2] Eski dosyalar temizleniyor..."
echo ""
rm -rf build dist *.spec

echo ""
echo "[ADIM 3] Executable oluşturuluyor..."
echo ""
python3 -m PyInstaller --onefile --windowed --name "HashTool" hashTool.py

echo ""
echo "[ADIM 4] Wordlist kopyalanıyor..."
echo ""
if [ -f "wordlist.txt" ]; then
    cp wordlist.txt dist/
else
    echo "UYARI: wordlist.txt bulunamadı, kopyalanmadı."
fi

echo ""
echo "============================================"
echo "TAMAMLANDI!"
echo "============================================"
echo ""
echo "Uygulama şurada: dist/HashTool"
echo ""
echo "Çalıştırmak için:"
echo "  cd dist"
echo "  ./HashTool"
echo ""