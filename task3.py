from PyPDF2 import PdfMerger

merger = PdfMerger()

# Add 3 PDF files
merger.append("EXP NO.1.pdf")
merger.append("EXP NO.2.pdf")
merger.append("EXP NO.3.pdf")
merger.append("EXP NO.4.pdf")

# Create one merged PDF
merger.write("merged.pdf")

merger.close()

print("4 PDF files merged successfully!")