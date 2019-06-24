## PDFTool


PDFTool is a simple tool to manage pdf files, write in Python 3. You can :   
-merge PDF files together  
-split a PDF to get a specific page or split all pages of a PDF document  
-extract text or image for a document  
-get info about a PDF file

Except for the merging action, you can specify a folder. So, PDFTool will loop on each PDF inside the source folder.

## Requirements


PDFTool use the following python modules :
- `os` to launch system command
- `glob` to find all PDF files if a folder is gived in source (`glob.glob(f"{src}/*.pdf")` for example in mergeTool function)
- `argparse` to parse arguments in command line
- `PyPDF2` to have fun with PDF files

### Requirements file
```
PyPDF2==1.26.0
```

## About merging

The merging function in PDFTool allow to merge many PDF files in a simple output file.

The source must be a folder and not a single file. PDFTool will find all PDF files with `.pdf` extension (using glob.glob module).
The output file must be a valid PDF file (with the right extension).

**Be sure your files are sorted and organized. PDFTool will merge files successively, in alphabetical order**

Usage examples :  
`PDFTool.py -merge --mergeIn /home/Doe/folderContainPDF --mergeOut /home/Doe/result.pdf`  


## About splitting  

PDFTool can split a specific page of a PDF file. You can also use the word `all` to specify at PDFTool you want to extract all pages in single PDF.

Usage examples :   
- Split the 3th page of a document  
`PDFTool.py -split --splitIn /home/Doe/file.pdf --splitOut /home/Doe/splitted.pdf --num 3`
- Split all pages of a document  
`PDFTool.py -split --splitIn /home/Doe/file.pdf --splitOut /home/Doe/resultFolder/ --num all`

**If you want to split all pages of a PDF files, `--splitOut` argument must be a folder destination, PDFTool create a PDF for each pages**


## About extraction

## About getting info
