#############################################################
### ___ /           _ |  _ \ _) |   
###   _ \\ \  / __ \  | |   | | __| 
###    ) |`  <  |   | | |   | | |   
### ____/ _/\_\ .__/ _|\___/ _|\__| 
###            _|                   
###                                                          
### name: install_tesseract.sh
### function: auto install tesseract 
### date: 2016-09-03
### author: quanyechavshuo
### blog: https://3xp10it.github.io
#############################################################
# unbuntu
sudo apt-get install autoconf automake libtool
sudo apt-get install libpng12-dev
sudo apt-get install libjpeg62-dev
sudo apt-get install libtiff4-dev
sudo apt-get install zlib1g-dev
sudo apt-get install libicu-dev
sudo apt-get install libpango1.0-dev
sudo apt-get install libcairo2-dev
export PATH=/usr/local/lib:$PATH

#if leptonica update,should update the version
wget http://www.leptonica.org/source/leptonica-1.73.tar.gz
tar -zxvf leptonica-1.73.tar.gz
cd leptonica-1.73
./configure
make
make install
git clone https://github.com/tesseract-ocr/tesseract.git
cd tesseract
./autogen.sh
./configure
LDFLAGS="-L/usr/local/lib" CFLAGS="-I/usr/local/include" make
sudo LDFLAGS="-L/usr/local/lib" CFLAGS="-I/usr/local/include" make install
sudo ldconfig

