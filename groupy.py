import os
import time
import json

with open('settings.json') as settings:
    setting = json.load(settings)
setting["track"] = str(setting["track"])
setting["track"] = setting["track"].strip()
setting["destination_base"] = str(setting["destination_base"])
setting["destination_base"] = setting["destination_base"].strip()

class Groupy(object):
    def  organise(self):
        for filename in os.listdir(setting["track"]):
            src = setting["track"] + "/" + filename
            dst = ""
            try:
                extension = filename.split(".")
            except ValueError:
                extension = filename
            folder_name = ""
            for folder in setting["destination_folder"]:
                if extension[-1] in setting["destination_folder"][folder]:
                    folder_name = folder
                    break
            if folder_name == "":
                folder_name =  setting["junkfolder"]
            dst = setting["destination_base"] + "/" + folder_name  + "/" + filename 
            for i in range(30):
                try :
                    os.rename(src,dst)
                    break
                except FileExistsError:
                    dst = setting["destination_base"] + "/" + folder_name  + "/" 
                    for j in extension:
                        if len(extension) > 1 and extension.index(j) == len(extension) - 1:
                            dst+="."
                        dst += j
                        if extension.index(j) == len(extension) - 2:
                            dst += " copy(" + str(i+1) + ")"
            
    def unorganise(self):
        for folder in os.listdir(setting["destination_base"]):
            for filename in os.listdir(setting["destination_base"] + "/" + folder):
                src =  setting["destination_base"] + "/" + folder  + "/" + filename
                dst =  setting["track"] + "/" + filename
                os.rename(src,dst)  

try:
    groupy  = Groupy()
    chc = int(input("1: Organise the files\n2: To undo all effects\nenter your choice :- "))
    if chc == 1:
        groupy.organise()
    elif chc == 2:
        groupy.unorganise()
    print("Done")

except Exception as err:
    print(err)
n = input("enter to continue")