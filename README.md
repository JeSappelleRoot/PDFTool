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
