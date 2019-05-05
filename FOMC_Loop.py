

#Download FOMC from here:
#https://github.com/souljourner/FOMC-Statements-Minutes-Scraper

#Place it in a folder and add it to sys.path so you can later import
import sys
cfrm_dir = 'C:\\Users\\Jason\\Desktop\\UW\\CFRM 521\\Project\\'
sys.path.append(cfrm_dir)



#Begin
from FOMC import FOMC
fomc = FOMC()

#Get the meeting statements back as a Pandas Dataframe
df = fomc.get_statements()


#Output one text file per announcement 
from datetime import datetime
out_dir = 'C:\\Users\\Jason\\Desktop\\UW\\CFRM 521\\Project\\FOMC\\'

N = len(df)
for i in range(1,N):
    #Prepare the out file name - It will be YYYYMMDD.txt
    t = df.index.tolist()[i]
    file = out_dir+str(t.year*10000+t.month*100+t.day)+'.txt'
    
    #Pull the statement text
    out_txt = df.iloc[i]['statements']
    if out_txt.find('Share')==-1:
        ind=1;
    else:
        ind = out_txt.find('Share')+5;
    
    #Write the file
    text_file = open(file, "ab")
    text_file.write(out_txt[ind:].encode('utf8'))
    text_file.close()





