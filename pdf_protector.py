import sys
import os
from PyPDF2 import PdfReader, PdfWriter
from colorama import init, Fore

def print_header():
    anon_mask = f"""
{Fore.GREEN}     █▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
{Fore.GREEN}     █░░╦╦╦╦╦╦╦░░█
{Fore.GREEN}     █░░║║║║║║║░░█
{Fore.GREEN}     █░░║║║║║║║░░█
{Fore.GREEN}     █░░╩╩╩╩╩╩╩░░█
{Fore.GREEN}     █▄▄▄▄▄▄▄▄▄▄▄▄█
{Fore.GREEN}   ▄▀░░░░░░░░░░░░░▀▄
{Fore.GREEN} ▄▀░░░░░░░░░░░░░░░░░▀▄
{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░█
{Fore.CYAN}  ~ made by ketaxpl0it ~
"""
    print(anon_mask)

def protect_pdf(input_file, output_file, password):
    try:
     
        if not os.path.exists(input_file):
            print(f"Error: File '{input_file}' does not exist.")
            return

        reader = PdfReader(input_file)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(password)

        with open(output_file, 'wb') as f_out:
            writer.write(f_out)

        print(f"Success: '{output_file}' has been created and protected with a password.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print_header()
    if len(sys.argv) != 4:
        print("Usage: python pdf_protector.py <input_pdf> <output_pdf> <password>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    password = sys.argv[3]

    protect_pdf(input_pdf, output_pdf, password)
