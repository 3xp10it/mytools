import os
command='''
brew cask install squirrel
rm ~/Library/Rime/default.custom.yaml
wget https://gist.githubusercontent.com/3xp10it/9f51ba895e47cdd5ed1b04f765298df9/raw/8d25bbcc5483e9f77ba24a3a5e84d28cc937fd9a/default.custom.yaml -O ~/Library/Rime/default.custom.yaml
'''
os.system(command)
print("请重新部署squirrel使设置生效")
