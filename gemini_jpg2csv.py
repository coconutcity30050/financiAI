# pip install google.generativeai
# usage: python gemini_img2csv.py dataset/Reports/113-07/113-07-存摺影本1.jpg > dataset/csv/113-07-1.csv
import sys
import google.generativeai as genai
import PIL.Image
import os

## please get API_KEY from https://aistudio.google.com/app/apikey
GOOGLE_API_KEY="---------------------------------------"
genai.configure(api_key=GOOGLE_API_KEY)

## for table in jpg
#img = PIL.Image.open("images/Bldg_E_neighbors.jpg")
#prompt = "根據這張圖片,請按照樓層與住戶姓名列出一個表格"

## for 存摺影本
filename = sys.argv[1]

img = PIL.Image.open( filename)
prompt = "根據這張圖片,按年月日,摘要,支出, 存入, 結存, 備註, 產生csv表格,並去掉數值的逗點"

model = genai.GenerativeModel("gemini-1.5-flash")

result = model.generate_content( [prompt , img] )
print(result.text)
