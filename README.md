# financiAI
* Gemini 是谷歌大型語言模型, 並具有視覺能力
  
## 資料集

dataset/Reports (存摺影本, 財務報表, 零用金明細表)<br>

dataset/csv (從影本.jpg 轉成 .csv格式)<br>

---
## 存摺影本資料庫化

### Step 1. Convert Image to CSV file
使用 `Gemini-1.5-Flash` AI模型 將存摺影本轉成.csv格式檔案<br>

`gemini_jpg2csv.py dataset/Reports/113-07/*.jpg > dataset/csv/*.csv`<br>

---
### Step 2. Transfer CSV to SQLite3 
將CSV檔案轉換為SQLite3資料庫<br>

---
### Step 3. Query SQLite3 Database
查詢SQLite3資料庫<br>
