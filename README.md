# financiAI

## 資料集
dataset/Reports (raw data = jpg/pdf)<br>
dataset/csv (converted data)<br>

---
## 存摺影本資料庫化

### Step 1. Convert Image to CSV file 
將存摺影本轉成.csv格式檔案<br>

`gemini_jpg2csv.py dataset/Reports/113-07/*.jpg > dataset/csv/*.csv`<br>

---
### Step 2. Transfer CSV to SQLite3 
將CSV檔案轉換為SQLite3資料庫<br>

---
### Step 3. Query SQLite3 Database
查詢SQLite3資料庫<br>
