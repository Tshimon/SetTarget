import pytesseract
from pdf2image import convert_from_path
import csv

# Tesseractのパスを指定
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def pdf_to_text(pdf_path):
    # PDFを画像に変換
    images = convert_from_path(pdf_path)
    text_list = []

    # 各画像に対してOCRを実行
    for image in images:
        text = pytesseract.image_to_string(image, lang='jpn')
        text_list.append(text)

    return text_list

def write_to_csv(text_list, csv_path):
    with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for text in text_list:
            writer.writerow([text])

# PDFからテキストを抽出し、CSVに書き出す
text_list = pdf_to_text('特別プレイスメント申請書 (version 1.3).pdf')
write_to_csv(text_list, 'output.csv')