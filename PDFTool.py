#!/usr/bin/env python3

# =========================== Import Section ===========================
import os
import re
import sys
import glob
import fitz
import tempfile
from pathlib import Path
import argparse
import functions
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger





# ==============================================================
# ======================== Main section ========================
# ==============================================================

# Ideas from :
# - https://indianpythonista.wordpress.com/2017/01/10/working-with-pdf-files-in-python/
# - https://www.geeksforgeeks.org/working-with-pdf-files-in-python/
# - http://www.blog.pythonlibrary.org/2018/04/10/extracting-pdf-metadata-and-text-with-python/
# - https://stackoverflow.com/questions/2693820/extract-images-from-pdf-without-resampling-in-python (post 15)
# - https://pymupdf.readthedocs.io/en/latest/tutorial/


# ================= Arg Parse section =================

# Initialization of the arguments parser
parser = argparse.ArgumentParser(
#usage=argparse.SUPPRESS,
formatter_class=argparse.RawDescriptionHelpFormatter,
description="""PDFTool is a simple tool to manage PDF files.\n
- PDFTool.py merge --help display help about merging
- PDFTool.py split --help display help about splitting
- PDFTool.py extract --help display help about extraction (text or images)
- PDFTool.py info --help display help about how to get info about a PDF

------------------------------------------------------------------------------
"""
)

# Initialize a subparser, with command destination
subParser = parser.add_subparsers(title="command",dest="command")

# Merge subparser
merge_parser = subParser.add_parser('merge',help='Merge PDF files together',description=functions.DisplayBanner())
merge_parser.add_argument('--mergeIn',help='Source must be a folder',required=True)
merge_parser.add_argument('--mergeOut',help='Destination must be a file (PDF)',required=True)

# Split subparser
split_parser = subParser.add_parser('split',help='Split specific page of PDF file, or all',description=functions.DisplayBanner())
split_parser.add_argument('--splitIn',help='Source file to split',required=True)
split_parser.add_argument('--splitOut', help='Destination folder',required=True)
split_parser.add_argument('--num',help='The number of page or "all" (all by default)',default='all')

# Extraction subparser
extract_parser = subParser.add_parser('extract',help='Extract text or images from a PDF file',description=functions.DisplayBanner())
extract_parser.add_argument('--extIn', help='Source file or folder for extraction',required=True)
extract_parser.add_argument('--extType', help='Type of the extract',choices=['img','text'],required=True)
extract_parser.add_argument('--extOut',help='Destination file (for text) or folder (for img) for extraction',required=True)

# Getting info subparser
info_parser = subParser.add_parser('info',help='Get info about a PDF document',description=functions.DisplayBanner())
info_parser.add_argument('--infoIn',help='Source file or folder to get info',required=True)
info_parser.add_argument('--infoOut',help='Destination dump file (display in console by default)',default='console')

# Reverse subparser
reverse_parser = subParser.add_parser('reverse',help='Reverse PDF file pages (1,2,3 will be 3,2,1)',description=functions.DisplayBanner())
reverse_parser.add_argument('--reverseIn',help='Source must be a file (PDF)',required=True)
reverse_parser.add_argument('--reverseOut',help='Destination must be a file (PDF)',required=True)


# Finally parse arguments
args = parser.parse_args()


# With a banner, it's a better ! ><))))°>
functions.DisplayBanner()

# If no arguments in command line, display help message
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
## Define action with command detected

# ====================================== Merge action
if args.command == 'merge':
    # Assign args to variables
    source = args.mergeIn
    dest = args.mergeOut

    # Check the source folder
    functions.InputIsValid(source,'folder')
    # Check the destination file
    functions.OutputIsValid(dest,'pdf')
    # Finally launch the merge
    engine.MergerTool(source,dest)



# ====================================== Split action
elif args.command == 'split':
    # Assign args to variables
    source = args.splitIn
    dest = args.splitOut
    page = args.num

    # Check the input PDF file
    functions.InputIsValid(source, 'pdf')
    # Check the output folder
    functions.OutputIsValid(dest, 'folder')
    # Finally launch the split
    engine.SplitFile(source, dest, page)



# ====================================== Extract action
elif args.command == 'extract':
    # Assign args to variables
    extractType = args.extType
    source = args.extIn
    dest = args.extOut

    # If extract image from PDF file
    if extractType == 'img':
        # Check the input file
        functions.InputIsValid(source, 'pdf')
        # Check the output folder
        functions.OutputIsValid(dest, 'folder')
        # Finally launch the extraction
        engine.ExtractImages(source, dest)

    # If extract text from PDF file
    elif extractType == 'text':
        # Check the input file
        functions.InputIsValid(source, 'pdf')
        # Check the output file
        functions.OutputIsValid(dest, 'file')
        # Finally launch the extraction
        engine.ExtractText(source, dest)

# ====================================== Info action
elif args.command == 'info':
    # Assign args to variables
    source = args.infoIn
    dest = args.infoOut

    # Check the source file
    functions.InputIsValid(source, 'pdf')
    
    # If output is in file, check the ouput file
    if dest != 'console':
        functions.OutputIsValid(dest, 'file')
    
    # Finally get info about a PDF file
    engine.GetPdfInfo(source, dest)


# ====================================== Reverse action
elif args.command == 'reverse':
    # Assign args to variables
    source = args.reverseIn
    dest = args.reverseOut

    # Check the source file
    functions.InputIsValid(source, 'pdf')
    # If output is in file, check the ouput file
    if dest != 'console':
        functions.OutputIsValid(dest, 'file')

    engine.ReverseFile(source, dest)
