# import os, sys
# from datetime import datetime
# import xml.dom.minidom


# currTime = datetime.now().strftime("%Y-%m-%d_%H")
# #print(currTime)

# path = "C:\AAA files"
# print("testing new ")
# s = os.path.basename(__file__).split(".")[0]
# print(s)


#===============================
# import PyPDF2
# filepath = "C:/Users/dalec/Desktop/3rd year/1st semester/CA357 User Interface and Completion/2_Human_Cognition_and_Perception/HumanPsychology.pdf"
# print(filepath)

# pdfFileObj = open(filepath,'rb')

# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# pages = pdfReader.numPages # prints the number of pages
# print(pages) 

# # for page in pdfReader.getPages:
# #     print()
 
# for i in range(pages):
#     pageObj = pdfReader.getPage(i)
#         # Printing Page Number
#     print("Page No: ", i)
#     print("")

#     # text = pageObj.extractText().split("  ")
#     text = pageObj.extractText().split("  ")
#     print(text)

#     for i in range(len(text)):
#         # Printing the line
#         # Lines are seprated using "\n"
#         print(text[i])#,end="\n\n")
    

# pdfFileObj.close()
#===============================

# import pptx
# from pptx.util import Inches



# prs = pptx.Presentation(filepath)

# text_runs = []
# for slide in prs.slides:
#     print(slide)
# #   for shape in slide.shapes:
# #     if not shape.has_text_frame:
# #       continue
# #   for paragraph in shape.text_frame.paragraphs:
# #     for run in paragraph.runs:
# #       text_runs.append(run.text)


# from os.path import isfile, join
# import os
# import re

# def getPptContent(path):
#     prs = Presentation(path)
#     text_runs = [] 
#     for slide in prs.slides:
#         for shape in slide.shapes:
#             if not shape.has_text_frame:
#                 continue
#             for paragraph in shape.text_frame.paragraphs:
#                 for run in paragraph.runs:
#                     text_runs.append(run.text)
#     return text_runs

# print(getPptContent(filepath))

# from pptx import Presentation
# import pptx
# from pptx.enum.action import PP_ACTION
# import docx
# filepath = "C:/Users/dalec/Desktop/test.pptx"
# filepath2 = "C:/Users/dalec/Desktop/Code/python/test/test_ppt_old.ppt"
# prs = pptx.Presentation(filepath)
# for slide in prs.slides:
#     for shape in slide.shapes:
#         if shape.has_text_frame:
#             for paragraph in shape.text_frame.paragraphs:
#                 for run in paragraph.runs:
#                     print(run.text)
            # click_action = shape.click_action
            # if click_action.action == PP_ACTION.HYPERLINK:
            #     print(click_action.hyperlink)




# for slide in prs.slides:
#     for rel in slide.part.rels.values():
#         if rel.is_external:
#             print(rel.target_ref)

# f = open(filepath.split(".")[0]+".txt" ,"w+", encoding="utf-8")
# print(f.readlines())
# f.close

# for slide in prs.slides:
#     for rel in slide.part.rels.values():
#         print(rel._target.encoding)


# for rel in prs.slides.part.rels.values():

#     if rel.is_external:
#         print(rel._baseURI)

# import zipfile
# with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
#     zip_ref.extractall(directory_to_extract_to)
#======================================

# import docx

# filename = "C:\\Users\\dalec\Desktop\\3rd year\\1st semester\\CA304 Computer Networks 2\\labs\\Apache Lab-2019-2020.docx"

# def getText(filename):
#     doc = docx.Document(filename)
#     fullText = []
#     for para in doc.paragraphs:
#         fullText.append(para.text)
#     print('\n'.join(fullText))

# getText(filename)

# from docx import Document

# document = Document(filename)
# # print(document.paragraphs[0].text[:])
# for para in document.paragraphs:
#     print(para.text)


#=======================================

# from xml.dom import minidom

# filename = "C:\\Users\\dalec\\Desktop\\Code\\python\\test\\books.xml"
# filename = "C:/Users/dalec/Desktop/test.pptx"
# # mydoc = minidom.parse('items.xml')

# f = open(filename, "r")
# print(f.readline())
# f.close()

# import xml.etree.ElementTree as ET
# tree = ET.parse(filename)
# root = tree.getroot()
# s = ET.tostring(root, encoding='utf8').decode('utf8')

# print(root.tag, root.attrib)
# for child in root:
#     print(child.tag, child.attrib)
# tags = [child.tag for child in root.iter()]
# # print(tags)
# stags = set(tags)
# print(stags)

# lst = []
# for tag in stags:
#     for para in root.iter(tag):
#         if para.text != "\n" or {}:
#             # print(text.text)
#             lst.append(para.text)

# print(lst)
# s = ET.tostring(root, encoding='utf8').decode('utf8')


# for i in s:
#     print(i)


#=======================================


# path = os.path.dirname(os.path.realpath(__file__))
# print(path)
# print(sys.argv[0])

# print("AWEES".lower())
# fn = "C:\\Users\\dalec\\Desktop\\Code\\python\\test\\excel_test.xlsx"
# import xlrd
# import pandas as pd

# df = pd.concat(pd.read_excel(fn, sheet_name=None), ignore_index=True)

# for row in df.iterrows():
#     print(row)

# ncols = xl.book.sheet_by_index(0).ncols
# df = xl.parse(0, converters={i : str for i in range(ncols)})

# print(df)
# print(type(df)))

# # data = pd.read_csv(fn)
# # print(data)

# import pdfx # pip install pdfx

# path = "C:\\Users\\dalec\\Desktop\\Code\\python\\test\\CA304_exam_papers.pdf"
# pdf = pdfx.PDFx(path)
# metadata = pdf.get_metadata()
# reference_list = pdf.get_references()
# reference_dict = pdf.get_references_as_dict()
# pdf.download_pdfs("C:\\Users\\dalec\\Desktop\\Code\\python\\test\\test.xml")
# s = pdf.get_text()
# print(s)


#==================


# import os, subprocess

# main_dir = os.path.join('/', 'Users', 'username', 'Desktop', 'foldername')

# filename = "test.doc"
# subprocess.call(['soffice', '--headless', '--convert-to', 'docx', filename])
# print("converted")

# import docx2txt
# my_text = docx2txt.process("test.docx")
# print(my_text)

#================================
# import pandas as pd
# # filepath = "C:/Users/dalec/Desktop/Code/python/test/excel_test_old.xls"
# filepath2 = "C:/Users/dalec/Desktop/Code/python/test/excel_test.xlsx"
# # links = []

# xl = pd.read_excel(filepath2, sheet_name = None)

# # for sheet in xl:
# #     for col in xl[sheet]:
# #         for cell in xl[sheet][col]:
# #             if type(cell) == str:
# #                 print(cell)


# for sheet in xl:
#     for col in xl[sheet]:
#         if (type(col) == str) and ("Unnamed" not in col):
#             print(col)
#         for cell in xl[sheet][col]:
#             if type(cell) == str:
#                 print(cell)

            # for row in xl[sheet][cell]:
            #     print(row)
            # if type(cell) == str:
            #     print(cell)


# import sys  
# import os  
# import glob  
# import win32com.client  
  
# def convert(files, formatType = 32):  
#     powerpoint = win32com.client.Dispatch("Powerpoint.Application")  
#     powerpoint.Visible = 1  
#     for filename in files:  
#         newname = os.path.splitext(filename)[0] + ".pdf"  
#         deck = powerpoint.Presentations.Open(filename)  
#         deck.SaveAs(newname, formatType)  
#         deck.Close()  
#     powerpoint.Quit()  


# pPATH_TO_MY_PPTX = "C:\\Users\\dalec\\Desktop\\Code\\python\\test\\test_ppt_old.ppt"
# files = glob.glob(r'PATH_TO_MY_PPTX') # <--- ONLY CHANGE  
# # convert(files) 

# import sys  
# import os  
# import glob  
# import win32com.client  
  
# dir =  r"C:\\Users\\dalec\\Desktop\\Code\\python\\test\\test_ppt_old.ppt"  
# outputdir = r"C:\\Users\\dalec\\Desktop\\Code\\python\\test\\pdf"  
  
# def convert(files, formatType = 32):  
#     powerpoint = win32com.client.Dispatch("Powerpoint.Application")  
#     powerpoint.Visible = 1  
#     for filename in files:  
#         newname = os.path.splitext(filename)[0] + ".pdf"  
#         newname = os.path.split(newname)[1]   
#         newname = os.path.join(outputdir,newname)  
#         deck = powerpoint.Presentations.Open(filename)          
#         deck.SaveAs(newname, formatType)  
#         deck.Close()  
#     powerpoint.Quit()  
                           
# files = glob.glob(os.path.join(dir,"*.ppt*"))  
# #print(files)  
# convert(files)  

# =======================

# # new pdf reader
# import PyPDF2
# filepath2 = "C:\\Users\\dalec\\Desktop\\Code\\python\\test\\test.pdf"
# filepath = "C:/Users/dalec/Desktop/3rd year/1st semester/CA357 User Interface and Completion/2_Human_Cognition_and_Perception/HumanPsychology.pdf"

# PDFFile = open(filepath2,'rb')

# PDF = PyPDF2.PdfFileReader(PDFFile)
# pages = PDF.getNumPages()
# key = '/Annots'
# uri = '/URI'
# ank = '/A'

# for page in range(pages):
#     print("Current Page: {}".format(page))
#     pageSliced = PDF.getPage(page)
#     pageObject = pageSliced.getObject()
#     if key in pageObject.keys():
#         ann = pageObject[key]
#         for a in ann:
#             u = a.getObject()
#             if uri in u[ank].keys():
#                 # print(u[ank]['/Type'])
#                 # print(uri)
#                 # print(u[ank]['/S'])
#                 print(u[ank][uri])
#                 # print(u['/A']['/URI'])

# filepath = 'C:\\Users\\dalec\\Desktop\\Code\\python\\test\\test.pptx'

# from tika import parser
# parsed = parser.from_file(filepath)
# print(parsed["metadata"]) #To get the meta data of the file
# print(parsed["content"]) # To get the content of the file

# import olefile

# ole = olefile.OleFileIO(r'C:\\Users\\dalec\\Desktop\\Code\\python\\test\\test.pptx')

# print(ole.listdir())
# data = ole.openstream('PowerPoint Document')
# print(data)
# ole.close()


#specific to extracting information from word documents
import os
import zipfile
#other tools useful in extracting the information from our document
import re
#to pretty print our xml:
import xml.dom.minidom

# s = os.listdir('.')
# f = os.listdir('..')


# print(s)

# filename = "C:\\Users\\dalec\\Desktop\\Code\\python\\test\\test.pptx"

# document = zipfile.ZipFile(filename)



# ZipFile.read(name, pwd=None)
# print(document)

# print(document.namelist())

# print("===============================this is the start")

# for i in document.namelist():
#     uglyXml = xml.dom.minidom.parseString(document.read(i)).toprettyxml(indent='  ')

#     text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)    
#     prettyXml = text_re.sub('>\g<1></', uglyXml)

#     print(prettyXml)

#     print("\n")


# #===============================
# uglyXml = xml.dom.minidom.parseString(document.read('ppt/slides/slide1.xml')).toprettyxml(indent='  ')

# text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)    
# prettyXml = text_re.sub('>\g<1></', uglyXml)

# print(prettyXml)
# #===============================


# outF = open("C:\\Users\\dalec\\Desktop\\Code\\python\\test\\myOutFile.txt", "w")

# filename = "C:\\Users\\dalec\\Desktop\\Code\\python\\test\\test_doc.docx"
# document = zipfile.ZipFile(filename)
# print(document.namelist())
# outF.write(filename)
# outF.write("\n")


# for i in document.namelist():
    
#     outF.write(i)
#     outF.write("\n")
#     outF.write("\n")
#     uglyXml = xml.dom.minidom.parseString(document.read(i)).toprettyxml(indent='  ')

#     text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)    
#     prettyXml = text_re.sub('>\g<1></', uglyXml)

#     outF.write(prettyXml)
#     outF.write("\n")
#     outF.write("================================")
#     outF.write("\n")

# outF.close()

# ==================================


# f1 = "C:\\Users\\dalec\\Desktop\\Code\\python\\test\\test_doc_old_verison.doc"
# f2 = "C:\\Users\\dalec\\Desktop\\Code\\python\\test\\test_doc.docx"
# files = [f1, f2]

# for i in files:
#     document = zipfile.ZipFile(i)
#     # print(document.read(filename))

# with open("", encoding: ansi)


# outF = open("C:\\Users\\dalec\\Desktop\\Code\\python\\test\\myOutFile.txt", "w")

# filename = "C:\\Users\\dalec\\Desktop\\Code\\python\\test\\test.pdf"

# document = zipfile.ZipFile(filename)
# for i in document.namelist():
#     print(i)
    # uglyXml = xml.dom.minidom.parseString(document.read(i)).toprettyxml(indent='  ')
    # text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)    
    # prettyXml = text_re.sub('>\g<1></', uglyXml)





# outF.close()

# outF = open("C:\\Users\\dalec\\Desktop\\Code\\python\\test\\myOutFile.txt", "w")



# outF.close()


# filename = "C:\\Users\\dalec\\Desktop\\Code\\python\\test\\test.pptx"
# document = zipfile.ZipFile(filename)
# print(document.namelist())

# uglyXml = xml.dom.minidom.parseString(document.read("ppt/slides/slide1.xml")).toprettyxml(indent='  ')

# text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)    
# prettyXml = text_re.sub('>\g<1></', uglyXml)

# print(prettyXml)
# outF.write(uglyXml)

# outF.close()


# ppt/slides/slide1.xml
# ppt/slides/_rels/slide1.xml.rels


# len(prs.slides())



#===============================================

# import subprocess
# import os
# import uuid # pip install uuid

# def document_to_html(file_path):
#     tmp = "/tmp"
#     guid = str(uuid.uuid1())
#     # convert the file, using a temporary file w/ a random name
#     command = "abiword -t %(tmp)s/%(guid)s.html %(file_path)s; cat %(tmp)s/%(guid)s.html" % locals()
#     p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=os.path.join(settings.PROJECT_DIR, "website/templates"))
#     error = p.stderr.readlines()
#     if error:
#         raise Exception("".join(error))
#     html = p.stdout.readlines()
#     return "".join(html)

# file_path = "C:\\Users\\dalec\\Desktop\\Code\\python\\test\\test.pdf"
# print(document_to_html(file_path))

# ===============================================
import PyPDF2
import pdfminer

filepath2 = "C:\\Users\\dalec\\Desktop\\Code\\python\\test\\test.pdf"
PDFFile = open(filepath2,'rb')

PDF = PyPDF2.PdfFileReader(PDFFile)
pages = PDF.getNumPages()
key = '/Annots'
uri = '/URI'
ank = '/A'
rect = '/Rect'

for page in range(pages):
    print("Current Page: {}".format(page))
    pageSliced = PDF.getPage(page)
    # print(pageSliced)
    pageObject = pageSliced.getObject()
    # print(pageObject)   
    if key in pageObject.keys():
        ann = pageObject[key]
        for a in ann:
            u = a.getObject()
            print(u)
            if uri in u[ank].keys():
                # print(uri)
                print(u[rect])
                print(u[ank][uri])


    
#     annotationList = []
#     if pageObject.annots:
#         for annotation in pageObject.annots.resolve():
#             annotationDict = annotation.resolve()
#             if str(annotationDict["Subtype"]) != "/Link":
#                 # Skip over any annotations that are not links
#                 continue
#             position = annotationDict["Rect"]
#             uriDict = annotationDict["A"].resolve()
#             # This has always been true so far.
#             assert str(uriDict["S"]) == "/URI"
#             # Some of my URI's have spaces.
#             uri = uriDict["URI"].replace(" ", "%20")
#             annotationList.append((position, uri))

# print(annotationList)