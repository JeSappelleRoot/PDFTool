# =========================== Import Section ===========================
import os
import re
import glob
import argparse
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

# -------------------------------------------------> displayBanner
def displayBanner():
# Simple function to display a displayBanner
# Can be disabled if you prefer boring console !

    os.system('clear')
    print("""
  _____  _____  ______ _______          _
 |  __ \|  __ \|  ____|__   __|        | |
 | |__) | |  | | |__     | | ___   ___ | |
 |  ___/| |  | |  __|    | |/ _ \ / _ \| |
 | |    | |__| | |       | | (_) | (_) | |
 |_|    |_____/|_|       |_|\___/ \___/|_|


    """)
    return

# -------------------------------------------------> checkPdf
def checkPDF(file):
# A little function to check if PDF file is Invalid
# Based only on the capacity of PyPDF2 to correctly open the file passed in argument
# May be a poor method...
# Added check extension first
    try:
        # Get extension and basename of given file in argument
        fileExtension = os.path.splitext(file)[1]
        baseName = os.path.basename(file)
        # Simple extension check
        if fileExtension != '.pdf':
            return 'extensionNONOK'
        else:
            # Open pdf for testing correct reading
            with open(file,'rb') as stream:
                # Test the reading capacity
                openPdf = PdfFileReader(stream)
                return 'pdfOK'
    # Except reading error
    except Exception as error:
        return False

# -------------------------------------------------> PDF merger function
def mergerTool(src, dst):
# Simple function to merge pdf files together

    try:
        # Get all PDF files in source path
        allPDF = glob.glob(f"{src}/*.pdf")
        # If pdfFiles array is empty (no PDF detected), return an error message
        if not allPDF:
            print("[!] Not PDF files detected in source directory")
            print(f"[!] Check your source path : {src}")
            return
        # Else if pdfFiles array got only one element (one PDF find)
        elif len(allPDF) == 1:
            print("[!] Cannot merge one PDF file to one PDF...")
            print("[!] Use your mind and add more PDF files")
            return

        # Initialize the merger
        pdfMerger = PdfFileMerger()
        # Loop to get all PDF files and add
        for pdf in allPDF:
            # Get PDF basename (because fullname in each loop can be too much)
            pdfBaseName = os.path.basename(pdf)
            if checkPDF(pdf) == 'pdfOK':
                print(f"[+] Adding [{pdfBaseName}] for merging")
                pdfMerger.append(pdf)

        # Finally write the final PDF to output.pdf file in destination folder
        with open(f"{destination}",'wb') as finalPDF:
            pdfMerger.write(finalPDF)

    # Get exception
    except Exception as error:
        print("\n[!] An error occured during merging :")
        print(f"{error}")

    return

# -------------------------------------------------> getInfo
def getInfo(file,output):
# Simple function to get info about a PDF file
# The method getDocumentInfo does'nt give all informations
# So, with a dictionnary, we can fix it an we can be sure to get all info !

    try:
        # Open file given in argument in RB mode
        with open(file,'rb') as stream:
            # Read file with PdfFileReader
            readPdf = PdfFileReader(stream)
            # Get all info about the document
            allInfo = str(readPdf.getDocumentInfo())
            # Get the number of page...can be usefull
            nbPage = readPdf.getNumPages()

        # Initialization of an empty dictionnary
        infoArray = {}
        # Process to a loop with multi split
        # This first split get the title of information and the value (Author and the given name)
        for info in allInfo.split(','):
            # This second split give the title of the information (Author, Title...)
            reference = info.split(':')[0]
            # With a regex, we extract only text (exclude [], /, quotes...)
            key = str(re.findall('\w+', reference)[0])
            # Finally, replace the second split by nothing, to get the opposit
            value = info.replace(reference,"")
            # Add condition if the value is empty (equal to : '' due to the extraction method...)
            if value == r": ''" or not value:
                value = '?'
            # Add key and value in the dictionnary
            infoArray[key] = value

        # Add a best output with an header
        header = f"Informations about {os.path.basename(file)}"
        # Repeat a char to have a separator
        topSeparator = '=' * len(header)
        # Define a footer section
        footer = f"Total number of pages in document : {nbPage}"
        # Repeat a char to have a separator in case of multi files
        bottomSeparator = '-' * len(footer)

        # Default behaviour, display directly in console
        if output == 'console':

            # Print header and separator
            print(header)
            print(topSeparator)
            # Finally display the content of the dictionnary (keys and values)
            for key in infoArray.keys():
                print(f"{key} {infoArray[key]}")
            # Print the footer and the bottom separator (with 2 new lines)
            print(footer)
            print(f"{bottomSeparator}\n\n")

        # Else if the command line indicate the output is in a log file
        elif output != 'console':
            # With statement to open a file, in append mode (in case of multi PDF file)
            with open(output,'a') as stream:
                # Write header and top separator
                stream.write(f"{header}\n")
                stream.write(f"{topSeparator}\n")
                # Loop on the dictionnary to get keys and values
                for key in infoArray.keys():
                    stream.write(f"{key} {infoArray[key]}\n")
                # Finally write the footer and the bottom separator
                stream.write(f"{footer}\n")
                stream.write(f"{bottomSeparator}\n\n")

    # Catch a possible error...
    except Exception as error:
        print(f"[!] An error occured during get information : ")
        print(f"{error}")
        return

    return


# ==============================================================
# ======================== Main section ========================
# ==============================================================

# Ideas from :
# - https://indianpythonista.wordpress.com/2017/01/10/working-with-pdf-files-in-python/
# - https://www.geeksforgeeks.org/working-with-pdf-files-in-python/
# - http://www.blog.pythonlibrary.org/2018/04/10/extracting-pdf-metadata-and-text-with-python/


# ================= Arg Parse section =================



# Define somes variables
source = r'/home/scratch/Downloads/sources'
destination = r'/home/scratch/Downloads/destination/output.pdf'

#displayBanner()
#mergerTool(source,destination)
#checkPDF(file)


# ================ Test getInfo function ================
#getInfoSRCFOLDER = r'/home/scratch/Downloads/sources/'
#getInfoSINGLEFILE = r'/home/scratch/Downloads/sources/file.pdf'
#getInfoFILEOUTPUT = r'/home/scratch/Downloads/destination/output.txt'
#getInfoCONSOLEOUTPUT = 'console'

#if os.path.isdir(folder):
#    for file in glob.glob(f"{folder}/*.pdf"):
#        print(file)
#        getInfo(file, output)
#else:
#    getinfo(file,output)
