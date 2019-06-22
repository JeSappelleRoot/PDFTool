# =========================== Import Section ===========================
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import glob
import os


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

# -------------------------------------------------> PDF merger function
def mergerTool(src, dst):
# Simple function to merge pdf files together

    # Simple error checking on source and destination folder
    if not os.path.exists(src):
        print("[!] Source folder does not exist !")
        # exit()
    elif not os.path.exists(dst):
        print("[!] Destination folder does not exist !")
        # exit()

    # Get all PDF files in source path
    allPDF = glob.glob(f"{src}/*.pdf")
    # If pdfFiles array is empty (no PDF detected), return an error message
    if not allPDF:
        print("[!] Not PDF files detected in source directory")
        print(f"[!] Check your source path : {src}")
        # exit()
    # Else if pdfFiles array got only one element (one PDF find)
    elif len(allPDF) == 1:
        print("[!] Cannot merge one PDF file to one PDF...")
        print("[!] Use your mind and add more PDF files")
        # exit()

    # Initialize the merging
    pdfMerger = PdfFileMerger()
    # Loop to get all PDF files
    for pdf in allPDF:
        pdfMerger.append(pdf)
    # Finally write the final PDF
    pdfMerger.write(f"{destination}/output.pdf")
    # Close the merger
    pdfMerger.close()


    return






# ==============================================================
# ======================== Main section ========================
# ==============================================================

# Define somes variables
source = r'~/Downloads/sources'
destination = r'~/Downloads/destination'

displayBanner()

mergerTool(source,destination)
