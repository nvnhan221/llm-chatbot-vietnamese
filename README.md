# LLM Chatbot nội bộ (Tiếng Việt)

## Hướng dẫn sử dụng:

1. Cài thư viện:
```
pip install -r requirements.txt
```

2. Cấu hình API key trong file `.env`:
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

3. Thêm tài liệu nội bộ vào thư mục `docs/` (PDF, DOCX, TXT)

4. Nạp dữ liệu:
```
python ingest.py
```

5. Chạy API:
```
uvicorn main:app --reload
```

6. Mở giao diện chat:
```
http://localhost:8000/static/index.html
```
