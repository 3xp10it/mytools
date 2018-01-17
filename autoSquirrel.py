import os
command='''
brew cask install squirrel
rm ~/Library/Rime/default.custom.yaml
'''
os.system(command)
input("Attention!!!\n_please do:\n1.add squirrel as your input method \n2.set up your squirrel as you like with this tool:\nhttps://github.com/neolee/SCU\n3.restart your squirrel or just make your setting take effect \n4.press any key after you finish it...")
command="wget --no-cache https://raw.githubusercontent.com/3xp10it/AutoIM/master/default.custom.yaml -O ~/Library/Rime/default.custom.yaml"
os.system(command)
input("Attention!!!\n_please do:\n1.restart your squirrel or just make your setting take effect \n2.press any key after you finish it...")
