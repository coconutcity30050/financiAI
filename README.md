# financiAI
<table>
<tr>
<td><img width="50%" height="50%" src="https://github.com/coconutcity30050/financiAI/blob/main/assets/113-03-passbook.png?raw=true"></td>
<td><img widht="25%" height="25%" src="https://github.com/coconutcity30050/financiAI/blob/main/assets/113-04-csv.png?raw=true"></td>
</tr>
</table>

---
## 資料集

* dataset/Reports (存摺影本, 財務報表, 零用金明細表)<br>

* dataset/csv (從存摺影本.jpg 轉成 .csv格式)<br>

### Download & Start
```
git clone https://github.com/coconutcity30050/financiAI/
cd financiAI
ls dataset/Reports/113-06
ls dataset/csv
```

---
## 存摺影本資料庫化

### Step 1. Convert Image to CSV file
(Gemini 是谷歌的大型語言模型, 並具有視覺能力)<br>

#### 將單一存摺影本.jpg轉成.csv格式檔案<br>

`python gemini_img2csv.py dataset/Reports/113-07/113-07-存摺影本1.jpg > dataset/csv/113-07-1.csv`<br>

#### 將整個檔案夾裡的存摺影本都轉換成.csv
`python gemini_img2csv.py dataset/Reports/113-08`<br>

* 須注意存摺影本.jpg之清晰度, 可能需要先影像處理, 來提高辨識的正確率

---
### Step 2. Transfer CSV to SQLite3 
#### 將CSV檔案轉換為SQLite3資料庫<br>

---
### Step 3. Query SQLite3 Database
#### 使用AI模型產生能查詢SQLite3資料庫的程式碼
