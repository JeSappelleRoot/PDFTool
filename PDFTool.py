# =========================== Import Section ===========================
import os
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
def checkPDF(pdf):
# A little function to check if PDF file is Invalid
# Based only on the capacity of PyPDF2 to correctly open the file passed in argument
# May be a poor method...
# Added check extension first
    try:
        # Get extension and basename of given file in argument
        fileExtension = os.path.splitext(pdf)[1]
        baseName = os.path.basename(pdf)
        # Simple extension check
        if fileExtension != '.pdf':
            return 'extensionNONOK'
        else:
            # Open pdf for testing correct reading
            with open(pdf,'rb') as file:
                # Test the reading capacity
                openPdf = PdfFileReader(file)
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






# ==============================================================
# ======================== Main section ========================
# ==============================================================

# Ideas from :
# - https://indianpythonista.wordpress.com/2017/01/10/working-with-pdf-files-in-python/
# - https://www.geeksforgeeks.org/working-with-pdf-files-in-python/


# ================= Arg Parse section =================
argParser = argparse.ArgumentParser()


# Define somes variables
source = r'/home/scratch/Downloads/sources'
destination = r'/home/scratch/Downloads/destination/output.pdf'
file = r'/home/scratch/Downloads/sources/Deploiement.pdf'

#displayBanner()
checkPDF(file)

#mergerTool(source,destination)
