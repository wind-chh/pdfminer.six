from pdfminer.settings import STRICT
import sys
print(sys.path)

from pdfminer import high_level

STRICT = True

# pdf_file = '/home/huan_cheng/workspace/algrithm/contractsimilarity/data/pdf/B3.pdf'
# pdf_file = '/home/huan_cheng/Documents/pdf_files/A0095607-010169.pdf'
pdf_file = '/tmp/aa.pdf'

text = high_level.extract_text(
    pdf_file, 
    password='', 
    # page_numbers=[13], 
    # page_numbers=[0], 
    maxpages=0, 
    caching=True, 
    codec='utf-8', 
    laparams=None
)
print(text)

print("-------> Done!")