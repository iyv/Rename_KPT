#!/usr/bin/env python3
import os
from zipfile import *
from lxml import etree


FileList=os.listdir(path='KPT')
#os.mkdir('output')
#os.mkdir('temp')
for namef in FileList:
    #print(namef)
    pathF='KPT/'+namef
    #print(is_zipfile(pathF))
    z = ZipFile(pathF, 'r')
    z.extractall('temp')

FileList=os.listdir(path='temp')
listFile=[]
for file_name in FileList:
    if (file_name[-3:])=='xml':
        doc=etree.parse('temp/'+file_name)
        for elem in doc.iter("Cadastral_Block"):
            cadNumber=elem.get("CadastralNumber")
        for elem in doc.iter("Date"):
            temp_elem=elem.text
            year=temp_elem[0:4]
            months=temp_elem[5:7]
            day=temp_elem[-2:]
            
        #print(cadNumber)
        file_name_new=cadNumber[0:2]+' '+cadNumber[3:5]+' '+cadNumber[6:]
        file_name_new+=' '+year+'-'+months+'-'+day
        indexFileName=1
        tempFileName=file_name_new
        NewSeach=True
        while (NewSeach):
            NewSeach=False
            for listfilename in listFile:
                if (listfilename==tempFileName):
                    tempFileName=file_name_new 
                    tempFileName +='-'+str(indexFileName)
                    indexFileName+=1
                    NewSeach=True
        file_name_new=tempFileName            
        listFile.append(file_name_new)
        print(file_name_new)
        os.rename('temp/'+file_name,'output/'+file_name_new+'.xml')
