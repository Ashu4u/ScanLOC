
import dload
import os
import third
from colorama import init, Fore, Back, Style
import shutil


# Initializes Colorama
init(autoreset=True)

url = input("Please Enter Your Github Repo: ")
if url=="" or url==None:
	print("No path entered.\n")
	raise SystemExit
folderName="gitRepo"
path=os.getcwd()+"//"+folderName
if os.path.exists(path)==False:
    os.makedirs(path)
else:
    shutil.rmtree(path)
dload.git_clone(url,clone_dir=path)

print("Repo cloned sucessfully.\n")

#we shall store all the file names in this list  
filelist = []

for root, dirs, files in os.walk(path):
	for file in files:
        #append the file name to the list
		filelist.append(os.path.join(root,file))

body="\nPlease find result of CLOC of repo: " +url+"\n"
#print all the file names
#body=''
for name in filelist:
    #print(name)
    # Opening a file
    file = open(name,"r")
    Counter = 0
    # Reading from file
    Content = file.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            Counter += 1

    basename = os.path.basename(name)       
    print("File "+basename+" has "+Style.BRIGHT + Back.YELLOW + Fore.RED +str(Counter)+" Lines")
    body=body+"File "+basename+" has "+str(Counter)+" Lines\n"
   
value = input("Please Enter Your Email: ")

third.my_function(value,body)