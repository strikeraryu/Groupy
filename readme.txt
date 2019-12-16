1. Setup
 
  	1 install python in your system
  	2 add the path to environment variable

2. how to use it

	2.1 change the setting in settings.json

		1 enter the path of the folder which you want to manage in track Field
		2 place the groupy folder anywhere but ( !!!! it should be in same disk as track !!!)
		3 enter its path in destination_base

	2.2 just the groupy.py



3. settings

	open setting.json


	######################################################################################################
					!!!           use "/" not "\"           !!!
		enter the path of the folder which you want to manage in track Field
		place the groupy folder anywhere but ( !!!! it should be in same disk as track !!!)
		enter its path in destination_base
		 
		In destinatination_folder there are different folder which are there in main folder
		and the extensions according to which you want to manage
		you can add new folder ------>        "folder name": [list of extension]
		enter the name of the folder in extra in which all files with other extension will be moved
	######################################################################################################



	{
		"track": "C:/Users/asus/downloads ",             ----> example path
		"destination_base": " C:/Users/asus/groupy" ,  ----> example path
		"destination_folder": {            
			"documents": ["doc","txt","pdf"],
			"sound": ["mp3","wav"],
			"video": ["mp4","3gp"],
			"images": ["jpg","png","jpeg","gif"],
			"softwares": ["exe"],
			"zip files": ["zip"]
		},
		"junkfolder": "extra"    ----> folder for files with other extension
	}	