from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import functions
import tempfile
import glob
import fitz
import sys
import os
import re





# -------------------------------------------------> PDF merger function
def MergerTool(src, dst):
# Simple function to merge pdf files together

    try:
        # Get all PDF files in source path
        all_pdf = glob.glob(f"{src}/*.pdf")
        # Sort all PDF by name
        all_pdf.sort()
        # If pdfFiles array is empty (no PDF detected), return an error message
        if not all_pdf:
            print("[!] Not PDF files detected in source directory")
            print(f"[!] Check your source path : {src}")
            return
        # Else if pdfFiles array got only one element (one PDF find)
        elif len(all_pdf) == 1:
            print("[!] Only one PDF file detected in source directory")
            print("[!] Cannot merge one PDF file to one PDF...")
            return

        # Initialize the merger
        pdf_merger = PdfFileMerger()
        # Loop to get all PDF files and add
        for pdf in all_pdf:
            # Get PDF basename (because fullname in each loop can be too much)
            pdf_basename = os.path.basename(pdf)
            if functions.CheckPdf(pdf) == 'pdfOK':
                print(f"[+] Adding {pdf_basename} for merging")
                pdf_merger.append(pdf)
            elif functions.CheckPdf(pdf) != 'pdfOK':
                print(f"[!] Cannot add {pdf_basename}, the file can't be read")

        # Finally write the final PDF to output.pdf file in destination folder
        with open(f"{dst}",'wb') as final_pdf:
            pdf_merger.write(final_pdf)
            print(f"\n[+] Successfully writed {dst}")

    # Get exception
    except Exception as error:
        print("\n[!] An error occured during merging :")
        print(f"{error}")

    return



# -------------------------------------------------> GetPdfInfo
def GetPdfInfo(file,output):
# Simple function to get info about a PDF file
# The method getDocumentInfo does'nt give all informations
# So, with a dictionnary, we can fix it an we can be sure to get all info !

    try:
        # Open file given in argument in RB mode
        with open(file,'rb') as stream:
            # Read file with PdfFileReader
            pdf_reader = PdfFileReader(stream)
            # Get all info about the document
            all_info = str(pdf_reader.getDocumentInfo())
            # Get the number of page...can be usefull
            nb_page = pdf_reader.getNumPages()

        # Initialization of an empty dictionnary
        info_array = {}
        # Process to a loop with multi split
        # This first split get the title of information and the value (Author and the given name)
        for info in all_info.split(','):
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
            info_array[key] = value

        # Add a best output with an header
        header = f"Informations about {os.path.basename(file)}"
        # Repeat a char to have a separator
        top_separator = '=' * len(header)
        # Define a footer section
        footer = f"Total number of pages in document : {nb_page}"
        # Repeat a char to have a separator in case of multi files
        bottom_separator = '-' * len(footer)

        # Default behaviour, display directly in console
        if output == 'console':

            # Print header and separator
            print(header)
            print(top_separator)
            # Finally display the content of the dictionnary (keys and values)
            for key in info_array.keys():
                print(f"{key} {info_array[key]}")
            # Print the footer and the bottom separator (with 2 new lines)
            print(footer)
            print(f"{bottom_separator}\n\n")

        # Else if the command line indicate the output is in a log file
        elif output != 'console':
            # With statement to open a file, in append mode (in case of multi PDF file)
            with open(output,'a') as stream:
                # Write header and top separator
                stream.write(f"{header}\n")
                stream.write(f"{top_separator}\n")
                # Loop on the dictionnary to get keys and values
                for key in info_array.keys():
                    stream.write(f"{key} {info_array[key]}\n")
                # Finally write the footer and the bottom separator
                stream.write(f"{footer}\n")
                stream.write(f"{bottom_separator}\n\n")
                print(f"[+] Info successfully dumped to {output}")

    # Catch a possible error...
    except Exception as error:
        print(f"[!] An error occured during get information : ")
        print(f"{error}")
        return

    return    



# -------------------------------------------------> SplitFile
def SplitFile(file, out_split, page):
# Simple function to extract a specific page of a PDF file
    try:

        # Open input file in reading mode
        with open(f"{file}", 'rb') as stream_in:

            # Initialize reader and writer
            pdf_reader = PdfFileReader(stream_in)
            nb_page = pdf_reader.getNumPages()
            pdf_writer = PdfFileWriter()

            if page != 'all':
                if int(page) > nb_page:
                    print(f"[!] The maximum page number allowed for {file} is {nb_page}")
                    print("[!] Please, specify a lower page number")
                    exit()
                elif int(page) < 0:
                    print(f"[!] The minimum page number allowed is 0")
                    print(f"[!] Please specify a greater page number")
                    exit()
                # Read needed page (-1 because number begin at 0...like an index...)
                pdf_writer.addPage(pdf_reader.getPage(int(page) - 1))
                # Define a name for out_file, based of the page number
                name_out = f"Page_{page}.pdf"

                # Finally write the output file in the output folder
                with open(f"{out_split}/{name_out}", 'wb') as stream_out:
                    pdf_writer.write(stream_out)
                    print(f"[+] Successfully write {out_split}/{name_out}")

            elif page == 'all':
                for page in range(nb_page):
                    # Initialize a new pdf_writer for each loop
                    # otherwise output add page at each other
                    # E.G page 3 contains page 1-2-3, page 4 contains page1-2-3-4...
                    pdf_writer = PdfFileWriter()
                    # Read needed page
                    pdf_writer.addPage(pdf_reader.getPage(int(page)))
                    # Define a name for out_file, based of the page number
                    name_out = f"Page_{page + 1}.pdf"

                    # Finally write the output file in the output folder
                    with open(f"{out_split}/{name_out}", 'wb') as stream_out:
                        pdf_writer.write(stream_out)
                        print(f"[+] Successfully write {out_split}/{name_out}")

    # Except a possible error...
    except Exception as error:
        print(f"An error occured when splitting {os.path.basename(file)} :")
        print(f"{error}")

    return





# -------------------------------------------------> ExtractImages
def ExtractImages(file, output):
# Function to extract images from a PDF file
# All images from PDF will be extracted

    # Open pdf file with fitz module
    pdf = fitz.open(file)
    # Loop with the max number of page
    for i in range(len(pdf)):
        # Add image counter
        image_counter = 0
        # Get image in the page
        for img in pdf.getPageImageList(i):
            xref = img[0]
            pix = fitz.Pixmap(pdf, xref)
            if pix.n < 5:       # this is GRAY or RGB
                if os.path.isfile(f"{output}/Page{i}_Image{image_counter}.png"):
                    print(f"[!] The file Page{i}_Image{image_counter}.png yet exist in {output}")
                else:
                    pix.writePNG(f"{output}/Page{i}_Image{image_counter}.png")
                    print(f"[+] Write {output}/Page{i}_Image{image_counter}.png")
            else:               # CMYK: convert to RGB first
                if os.path.isfile(f"{output}/Page{i}_Image{image_counter}.png"):
                    print(f"[!] The file Page{i}_Image{image_counter}.png yet exist in {output}")
                else:
                    pix1 = fitz.Pixmap(fitz.csRGB, pix)
                    pix1.writePNG(f"{output}/Page{i}_Image{image_counter}.png")
                    print(f"[+] Write {output}/Page{i}_Image{image_counter}.png")
                    pix1 = None
            pix = None
            image_counter = image_counter + 1 

    return


# -------------------------------------------------> ExtractText
def ExtractText(file, out_file):
# Function to extract all text from a PDF file
# The result can't work very well
# Depend of the PDF construction

    # Open the PDF file with fitz
    pdf = fitz.open(file)
        
    # Loop in all page with a range
    for num in range(len(pdf)):
        # Load the page n° num
        page = pdf.loadPage(num)
        # Get text of this page
        text = page.getText()

        # Open the output file, in append mode
        with open(out_file, 'a') as output:
            # Define a header to know from where the text is extract
            header = f"========================================== From page {num + 1} ==========================================\n"
            # Write header first
            output.write(header)
            # Finally write the text of the page in the ouput file
            output.write(text)
            print(f"[+] Text from page {num + 1} writted to {out_file}")

    return



# -------------------------------------------------> ReverseFile
def ReverseFile(source, dest):

    # Get temporary directory
    temporary_directory = tempfile.gettempdir()
    # Create empty list to contain temporary pdf files fullpath
    temporary_files = []


    try:

        # Open source file in read mode
        with open(source, 'rb') as stream_in:
            # Create a PDF reader object
            pdf_reader = PdfFileReader(stream_in)
            # Get total of pages in the source file
            nb_page = pdf_reader.getNumPages()
            print(f"[+] {nb_page} pages detected in PDF file {source}")


            # Loop over total of pages
            for i in range(nb_page):
                # Get current page
                current_page = pdf_reader.getPage(i)
                # Create a PDF writer object
                pdf_writer = PdfFileWriter()
                # Add current page from the loop
                pdf_writer.addPage(current_page)
                # Create a temporary file
                temporary_pdf_file = f"{temporary_directory}/reverse_temp_{i}.pdf"
                # Append the fullname of the temporary file in a list, to retrieve all PDF files for final merge
                temporary_files.append(temporary_pdf_file)
                # Open temporary file in write mode
                with open(temporary_pdf_file, 'wb') as stream_out:
                    print(f"  - Writting page {i} in temporary file {temporary_pdf_file}")
                    # Use PDF writer to write single page
                    pdf_writer.write(stream_out)

        # Sort temporary PDF files list
        temporary_files.sort(reverse=True)
        # Create a PDF merger object
        pdf_merger = PdfFileMerger()

        # Iterate over temporary files list
        for file in temporary_files:
            # Check PDF file
            if functions.CheckPdf(file) == 'pdfOK':
                # Add each temporary PDF file in the merger
                pdf_merger.append(file)
                # Remove merged PDF file
                os.remove(file)

            elif functions.CheckPdf(pdf) != 'pdfOK':
                print(f"[!] Cannot add {file}, the file can't be read (file won't be deleted)")

        # Open destination PDF file in write mode
        with open(dest, 'wb') as stream_out:
            # Write merger content in final PDF file
            pdf_merger.write(stream_out)
            print(f"[+] Successfuly created reversed file {dest}")


    except Exception as error:
        print(f"[!] An error occured during PDF file reversing : {error}")
        exit()

    return