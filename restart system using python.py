import os
restart= input("Do you wish to restart your computer?(y/n):")
if restart=='y' or restart=='Y':
    os.system("shutdown /s /t 1")#shutdown
     os.system("restart /r /t 1")#restart
else:
    print("No problem")
    print("Exiting the program")
    
                        
    
