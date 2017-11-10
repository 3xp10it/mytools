#############################################################
###                             
###  mm         .m   mm  '   .  
### ' '[. . .m,  ]  .`',.m  .dm 
###  .m` b[ ]`T  ]  ] ,[ ]   ]  
###   '[ d, ] ]  ]  ]  [ ]   ]  
### 'md`.`\ ]bP .dm  bd .dm  'm 
###         ]                   
###         '                   
###                                                          
### name: install_tesseract.sh
### function: auto install tesseract
### date: 2016-09-03
### author: quanyechavshuo
### blog: https://3xp10it.github.io
#############################################################
# unbuntu
sudo echo y | apt-get install autoconf automake libtool
sudo echo y | apt-get install libpng12-dev
sudo echo y | apt-get install libjpeg62-dev
sudo echo y | apt-get install libtiff4-dev
sudo echo y | apt-get install zlib1g-dev
sudo echo y | apt-get install libicu-dev
sudo echo y | apt-get install libpango1.0-dev
sudo echo y | apt-get install libcairo2-dev
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

#refer from http://stackoverflow.com/questions/14800730/tesseract-running-error
wget https://github.com/tesseract-ocr/tessdata/raw/master/eng.traineddata
sudo mv -v eng.traineddata /usr/local/share/tessdata/

#if you want use pytesser(google module,but not updated since 2007),below are needed,otherwise,till here,
#everything is ok,that is to say,if you want to use tesseract directlly to recognize yanzhengma other than 
#use pytesser to recognize yanzhengma,you don't need to execute below commands
#these refer from http://www.jinglingshu.org/?p=9281
#下面的不执行是可以的,为了更好地识别验证码,Imaging-1.1.7的安装最好执行下,根据
#http://www.debasish.in/2012/01/bypass-captcha-using-python-and.html
#暂时都将下面的执行吧

pip install pytesseract
wget http://effbot.org/downloads/Imaging-1.1.7.tar.gz
tar -zxvf Imaging-1.1.7.tar.gz
cd Imaging-1.1.7
python setup.py install
