from PyPDF2 import PdfMerger
import os
 
pdf_folder = "D:/A-Materials/PDF"
 
#遍历文件夹中所有PDF文件
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
 
#创建一个PdfMerger对象
merger = PdfMerger()
 
#逐个合并PDF文件
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_folder, pdf_file)
    merger.append(pdf_path)
 
#指定合并后的PDF文件路径
output_path = "D:/A-Materials/PDF/file.pdf"
 
merger.write(output_path)
merger.close()
 
print("pdf文件合并完成!")