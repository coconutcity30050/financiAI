# pip install google.generativeai
# usage: python gemini_img2csv.py dataset/Reports/113-06
# output: dataset/csv/113-06-*.csv
import sys
import google.generativeai as genai
import PIL.Image
import os
import glob

src_path = sys.argv[1]
dst_path = "dataset/csv/"

GOOGLE_API_KEY="AIzaSyCnRzbxgrMX1GjIHnN7U6EQVM8YKy9Ikw4" ## https://aistudio.google.com/app/apikey
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

## for 存摺影本
path_name = src_path
file_name = path_name[-6:]
filelist = glob.glob(path_name+"/"+file_name+"-存摺影本*.jpg")

for file in filelist:
    print(file)
    img = PIL.Image.open(file)
    prompt = "根據這張圖片,按年月日,摘要,支出, 存入, 結存, 備註, 產生csv表格,並去掉數值的逗點"
    result = model.generate_content( [prompt , img] )

    file1 = file.replace(path_name+"/", "")
    fname = file1.replace(".jpg", ".csv")
    fname = fname.replace("存摺影本", "")
    print(fname)
    
    f = open("dataset/csv/"+fname, "a")
    f.write(result.text)
    f.close()
