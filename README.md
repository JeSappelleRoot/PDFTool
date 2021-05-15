Table of Contents
=================


- [Table of Contents](#table-of-contents)
- [PDFTool](#pdftool)
  - [Requirements](#requirements)
    - [Requirements file](#requirements-file)
    - [Sources, ideas from...](#sources-ideas-from)
- [About functionalities of PDFTool](#about-functionalities-of-pdftool)
  - [About merging](#about-merging)
  - [About splitting](#about-splitting)
  - [About extraction](#about-extraction)
  - [About getting info](#about-getting-info)
  - [About reversing a PDF file](#about-reversing-a-pdf-file)




# PDFTool


PDFTool is a simple tool to manage pdf files, write in Python 3. With PDFTool you can :   
-merge PDF files together  
-split a PDF to get a specific page or split all pages of a PDF document  
-extract text or image for a document  
-get info about a PDF file
-reverse pages from a PDF file

## Requirements

PDFTool use the following python modules :
- `os` to launch system command
- `re` to use regex search (in getInfo function)
- `glob` to find all PDF files if a folder is gived in source (`glob.glob(f"{src}/*.pdf")` for example in mergeTool function)
- `argparse` to parse arguments in command line
- `PyPDF2` to have fun with PDF files
- `fitz` to extract pictures and text from PDF
- `Path` from `pathlib` to get parent folder of a file
- `filetemp` to detected temporary folder (OS distribution dependency)
### Requirements file  
```
PyPDF2==1.26.0
PyMuPDF==1.14.16
```
Just run `pip3 install -r requirements.txt` to install all modules needed by PDFTool

### Sources, ideas from...  

- https://indianpythonista.wordpress.com/2017/01/10/working-with-pdf-files-in-python/
 - https://www.geeksforgeeks.org/working-with-pdf-files-in-python/
 - http://www.blog.pythonlibrary.org/2018/04/10/extracting-pdf-metadata-and-text-with-python/
 - https://stackoverflow.com/questions/2693820/extract-images-from-pdf-without-resampling-in-python (post 15)
 - https://pymupdf.readthedocs.io/en/latest/tutorial/

*Thanks to all people, from JeSappelleRoot*


# About functionalities of PDFTool

## About merging

The merging function in PDFTool allow to merge many PDF files in a simple output file.

The source must be a folder and **not a single file**. PDFTool will find all PDF files with `.pdf` extension (using Glob module).
The output file must be a valid PDF file (with the right extension).

**Be sure your files are sorted and organized. PDFTool will merge files successively, in alphabetical order**

Usage examples :  
`PDFTool.py merge --mergeIn /home/Doe/source --mergeOut /home/Doe/result.pdf `  

```
  _____  _____  ______ _______          _
 |  __ \|  __ \|  ____|__   __|        | |
 | |__) | |  | | |__     | | ___   ___ | |
 |  ___/| |  | |  __|    | |/ _ \ / _ \| |
 | |    | |__| | |       | | (_) | (_) | |
 |_|    |_____/|_|       |_|\___/ \___/|_|


    
[+] Adding file1.pdf for merging
[+] Adding file2.pdf for merging
[+] Adding file3.pdf for merging
[+] Adding file4.pdf for merging
[+] Adding file5.pdf for merging

[+] Successfully writed /home/Doe/result.pdf
```

## About splitting

PDFTool can split a specific page of a PDF file. You can also use the keyword `all` to specify at PDFTool you want to extract all pages in single PDF.

Usage examples :   
- Split and extract the 3th page of a document  
`PDFTool.py split --splitIn /home/Doe/file.pdf --splitOut /home/Doe/resultFolder/ --num 3`
- Split all pages of a document  
`PDFTool.py split --splitIn /home/Doe/file.pdf --splitOut /home/Doe/resultFolder/ --num all`

PDFTool will automaticly named the extract page by number of the needed page :   
-Page_2.pdf for the 2nd page  
-Page_5.pdf for the 5th page  


**The `--splitOut` argument must be a destination folder**
**The split function can't work with entire folder, which contains multiple PDF files**

```
  _____  _____  ______ _______          _
 |  __ \|  __ \|  ____|__   __|        | |
 | |__) | |  | | |__     | | ___   ___ | |
 |  ___/| |  | |  __|    | |/ _ \ / _ \| |
 | |    | |__| | |       | | (_) | (_) | |
 |_|    |_____/|_|       |_|\___/ \___/|_|


    
[+] Successfully write /home/Doe/destination/Page_1.pdf
[+] Successfully write /home/Doe/destination/Page_2.pdf
[+] Successfully write /home/Doe/destination/Page_3.pdf
[+] Successfully write /home/Doe/destination/Page_4.pdf
[+] Successfully write /home/Doe/destination/Page_5.pdf
[+] Successfully write /home/Doe/destination/Page_6.pdf
[+] Successfully write /home/Doe/destination/Page_7.pdf
[+] Successfully write /home/Doe/destination/Page_8.pdf
```


## About extraction

PDFTool can extract text or images from a PDF file.  
The extraction of text does not work with all PDF, depend of the construction of the file. The layout may not be respected when extract text.   
The image extraction use the page number and the image number (in the targeted page) to get the output name file.  


When you want extract image, **you must specify a destionation folder**
When you want extract text to a custom file (TXT in example), **you must specify a destination file, not a folder**

Usage examples :  
* extract text from a PDF file 
`PDFTool.py extract --extType text --extIn /home/Doe/source/file.pdf --extOut /home/Doe/destination/output.txt` 
* extract images from a PDF file  
`PDFTool.py extract --extType img --extIn /home/Doe/source/file.pdf --extOut /home/Doe/destination/`

**Text extraction**

```

  _____  _____  ______ _______          _
 |  __ \|  __ \|  ____|__   __|        | |
 | |__) | |  | | |__     | | ___   ___ | |
 |  ___/| |  | |  __|    | |/ _ \ / _ \| |
 | |    | |__| | |       | | (_) | (_) | |
 |_|    |_____/|_|       |_|\___/ \___/|_|


    
[+] Text from page 1 writted to /home/Doe/destination/output.txt
[+] Text from page 2 writted to /home/Doe/destination/output.txt
[+] Text from page 3 writted to /home/Doe/destination/output.txt
[+] Text from page 4 writted to /home/Doe/destination/output.txt
[+] Text from page 5 writted to /home/Doe/destination/output.txt
[+] Text from page 6 writted to /home/Doe/destination/output.txt

[...]
```



**Image extraction**
```
  _____  _____  ______ _______          _
 |  __ \|  __ \|  ____|__   __|        | |
 | |__) | |  | | |__     | | ___   ___ | |
 |  ___/| |  | |  __|    | |/ _ \ / _ \| |
 | |    | |__| | |       | | (_) | (_) | |
 |_|    |_____/|_|       |_|\___/ \___/|_|


    
[+] Write /home/Doe/destination/Page2_Image0.png
[+] Write /home/Doe/destination/Page2_Image1.png
[+] Write /home/Doe/destination/Page4_Image0.png
[+] Write /home/Doe/destination/Page4_Image1.png
[+] Write /home/Doe/destination/Page4_Image2.png
[+] Write /home/Doe/destination/Page5_Image0.png


[...]
```

## About getting info

PDFTool can extract information about a PDF file.  
PyPDF2 module with PdfFileReader give `getDocumentInfo()` method. We can use it to extract many informations like :  
- Author
- Title
- Producer
- ...

But this method seems to be incomplete. So, with a dictionnary we can get all infos about a document.

Usage examples :
- Get info about a single file and dump the result to a TXT file  
`PDFTool.py info --infoIn /home/Doe/file.pdf --infoOut /home/Doe/infos.txt`  
- Get info about multiple files in a directory and display it in the console  
`PDFTool.py info --infoIn /home/Doe/files/`

**By default, the `info` functionality make the output directly in the console**


**Console output (default behaviour)**
```
  _____  _____  ______ _______          _
 |  __ \|  __ \|  ____|__   __|        | |
 | |__) | |  | | |__     | | ___   ___ | |
 |  ___/| |  | |  __|    | |/ _ \ / _ \| |
 | |    | |__| | |       | | (_) | (_) | |
 |_|    |_____/|_|       |_|\___/ \___/|_|


Informations about file.pdf
==================================
Author ?
Title ?
Subject ?
Creator : 'LaTeX with hyperref'
Producer : 'pdfTeX-1.40.19'
Keywords ?
CreationDate : "D:20190212124237+01'00'"
ModDate : "D:20190212124237+01'00'"
Trapped : '/False'
PTEX : 'This is pdfTeX
Version ?
Total number of pages in document : 12
--------------------------------------
```


**Dump information to file**

```
  _____  _____  ______ _______          _
 |  __ \|  __ \|  ____|__   __|        | |
 | |__) | |  | | |__     | | ___   ___ | |
 |  ___/| |  | |  __|    | |/ _ \ / _ \| |
 | |    | |__| | |       | | (_) | (_) | |
 |_|    |_____/|_|       |_|\___/ \___/|_|


    
[+] Info successfully dumped to /home/scratch/destination/file.txt
```

## About reversing a PDF file

PDFTool can reverse a PDF file.  
A PDF file with pages 1, 2 and 3 will be reversed with pages 3, 2 and 1

Usage example :  
`PDFTool.py reverse --reverseIn /home/Doe/input.pdf --reverseOut /home/Doe/output.pdf` 

PDFTool will detected default temporary directory with `tempfile.gettempdir()` method. 
Each pages will be extracted in a temporary PDF file and finally merged but from the last page to the first page.  

**All the temporary PDF files are deleted after merging (only if file is valid for merging**


```
  _____  _____  ______ _______          _
 |  __ \|  __ \|  ____|__   __|        | |
 | |__) | |  | | |__     | | ___   ___ | |
 |  ___/| |  | |  __|    | |/ _ \ / _ \| |
 | |    | |__| | |       | | (_) | (_) | |
 |_|    |_____/|_|       |_|\___/ \___/|_|


    
[+] 7 pages detected in PDF file /home/Doe/input.pdf
  - Writting page 0 in temporary file /tmp/reverse_temp_0.pdf
  - Writting page 1 in temporary file /tmp/reverse_temp_1.pdf
  - Writting page 2 in temporary file /tmp/reverse_temp_2.pdf
  - Writting page 3 in temporary file /tmp/reverse_temp_3.pdf
  - Writting page 4 in temporary file /tmp/reverse_temp_4.pdf
  - Writting page 5 in temporary file /tmp/reverse_temp_5.pdf
  - Writting page 6 in temporary file /tmp/reverse_temp_6.pdf
[+] Successfuly created reversed file /home/Doe/output.pdf
```