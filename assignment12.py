#Q=1
import datetime as d
date=d.date.today()
print('DATE IS:',date)
print('WEEKDAY IS:',date.strftime("%A"))



#Q=2
import webbrowser
webbrowser.open("https://www.youtube.com/watch?v=41qgdwd3zAg&list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n")



#Q=3
import os,sys
folder = r'C:\Users\HP\Desktop\python'
for file in os.listdir(folder):
    infile = os.path.join(folder,file)
    if not os.path.isfile(infile):
        continue
    oldbase = os.path.splitext(file)
    newname = infile.replace('.txt', '.jpg')
    output = os.rename(infile, newname)
