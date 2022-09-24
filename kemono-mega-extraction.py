import os
import re
import sys

# usage: kemono-mega-extraction.py <folder to check recursively> <output folder>

txt_list = []
for dirpath, dirnames, filename in os.walk(sys.argv[1]):
    for filename in filename:
        txtfile_full_path = os.path.join(dirpath, filename)
        print(txtfile_full_path)
        if filename.endswith(".html"):
            with open(txtfile_full_path, 'r', encoding='utf-16', errors='ignore') as f:
                lines = f.readlines()
                for line in lines:
                    sline = line.strip()
                    if sline:
                        txt_list.append(sline)
                        
        if filename.endswith(".txt"):
            with open(txtfile_full_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                for line in lines:
                    sline = line.strip()
                    if sline:
                        txt_list.append(sline)
            
link_list = []
for text in txt_list:
    text_parts = text.split(' ')
    for part in text_parts:
        if part.startswith("http"):
            link_list.append(part + '\n')

if sys.argv[2]:
    mega_link_path = os.path.join(sys.argv[2], "mega_links.txt")
    txt_list_path = os.path.join(sys.argv[2], "txt_list.txt")
else:
    mega_link_path = "mega_links.txt"
    txt_list.path = "txt_list.txt"
    
with open(mega_link_path, "w") as f:
    for line in link_list:
        if "mega" in line:
            f.write(line)

with open(txt_list_path, "w", encoding='utf-8', errors='ignore') as f:
    for line in txt_list:
        f.write(line)