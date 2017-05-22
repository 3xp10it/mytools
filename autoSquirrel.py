import os
command='''
brew cask install squirrel
rm ~/Library/Rime/default.custom.yaml
'''
os.system(command)
input("Attention!!!\nPlease do:\n1.add squirrel as your input method \n2.set up your squirrel as you like with this tool:\nhttps://github.com/neolee/SCU\n3.restart your squirrel or just make your setting take effect \n4.press any key after you finish it...")
command="wget https://gist.githubusercontent.com/3xp10it/9f51ba895e47cdd5ed1b04f765298df9/raw/f5f8504fb831fa23f8d80eb34ac97491d6577d93/default.custom.yaml -O ~/Library/Rime/default.custom.yaml"
os.system(command)
input("Attention!!!\nPlease do:\n1.restart your squirrel or just make your setting take effect \n2.press any key after you finish it...")
