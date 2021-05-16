from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
from pathlib import Path
import os


# -------------------------------------------------> DisplayBanner
def DisplayBanner():
    
# Simple function to display a DisplayBanner
# Can be disabled if you prefer boring console !

    os.system('clear')
    print(r"""
  _____  _____  ______ _______          _
 |  __ \|  __ \|  ____|__   __|        | |
 | |__) | |  | | |__     | | ___   ___ | |
 |  ___/| |  | |  __|    | |/ _ \ / _ \| |
 | |    | |__| | |       | | (_) | (_) | |
 |_|    |_____/|_|       |_|\___/ \___/|_|


    """)
    return

# -------------------------------------------------> CheckPdf
def CheckPdf(file):
# A little function to check if PDF file is Invalid
# Based only on the capacity of PyPDF2 to correctly open the file passed in argument
# Added check extension first
    try:
        # Get extension and basename of given file in argument
        file_extension = os.path.splitext(file)[1]
        # Simple extension check
        if file_extension != '.pdf':
            return 'extensionNONOK'
        else:
            # Open pdf for testing correct reading
            with open(file,'rb') as stream:
                # Test the reading capacity
                PdfFileReader(stream)
                return 'pdfOK'
    # Except reading error
    except Exception:
        return False





# -------------------------------------------------> CheckInputFile
def CheckInputFile(file):
# Simple function to check if an input file exist
# Used in all functionality of the script

    if not os.path.isfile(file):
        print(f"[!] The file {file} does'nt exist")
        print(f"[!] Check your path")
        return False
    elif os.path.isfile(file):
        return True



# -------------------------------------------------> CheckOutputFolder
def CheckOutputFolder(path):
# Simple function to check if an output folder (in argument) exist
# Used to check an output directory before processing

    if not os.path.isdir(path):
        print(f"[!] The directory {path} does'nt exist or is invalid")
        print(f"[!] Check your path")
        return False
    elif os.path.isdir(path):
        return True


# -------------------------------------------------> InputIsValid
def InputIsValid(path,type_in):
# Function to check the input arg 
# Can check source folder or source file (valid PDF)

    # If need to check an input folder
    if type_in == 'folder':
        # If the folder does not exist
        if not os.path.isdir(path):
            print(f"[!] The source folder does not exist")
            print(path)
            exit()

    # If need to check an input pdf
    elif type_in == 'pdf':
        # Get extension and basename of given file in argument
        file_extension = os.path.splitext(path)[1]
        # Check if source file exist
        if not os.path.isfile(path):
            print(f"[!] The source file does not exist :")
            print(path)
            exit()
        # Simple extension check
        elif file_extension != '.pdf':
            print("The extension of source file does not match with PDF file :")
            print(path)
            exit()
        # Else, try to read the file to detect if it's a real PDF file
        else:
            try:
                # Open pdf for testing correct reading
                with open(path,'rb') as stream:
                    # Test the reading capacity
                    PdfFileReader(stream)
            except Exception:
                print("[!] The source file can't be read, may be a wrong PDF file :")
                print(path)
                exit()

    return



# -------------------------------------------------> OutputIsValid
def OutputIsValid(path,type_out):
# Function to check the output (file or folder)

    # If need to check an output folder
    if type_out == 'folder':
        # If folder does not exist
        if not os.path.isdir(path):
            print("[!] The output folder does not exist :")
            print(path)
            exit()
    #If need to check an output file
    elif type_out == 'file':
        # Get parent folder of output file
        parent_folder = Path(path).parent
        # If the parent folder does not exist
        if not os.path.isdir(parent_folder):
            print("[!] The parent folder of output file does not exist :")
            print(path)
            exit()
        elif os.path.isfile(path):
            print(f"[!] The file {path} already exist !")
            exit()
        elif os.path.isdir(path):
            print("[!] Please, specify an output file instead a folder :")
            print(path)
            exit()
    # If need to check an ouput PDF file
    elif type_out == 'pdf':
        # Get file extension
        file_extension = os.path.splitext(path)[1]
        # If output pdf file haven't got a pdf extension
        if os.path.isdir(path):
            print("[!] Please, specify an output file instead a folder :")
            print(path)
            exit()
        elif file_extension != '.pdf':
            print("The extension of destination file does not match with PDF file :")
            print(path)
            exit()
        elif os.path.isfile(path):
            print("[!] The output PDF file already exist !")
            print(path)
            exit()
        
    return    