# Gmail Automated Email Sender

這個 Python 腳本使用 Gmail SMTP 來發送自動化郵件，支援純文字、HTML 格式以及附件。

## 功能特點

- 支援純文字和 HTML 格式郵件
- 可發送附件
- 支援多個收件人
- 使用 Gmail SMTP 服務
- 完整的錯誤處理
- 類型提示支援
- 環境變數支援

## 設置步驟

1. 首先，你需要設置 Gmail 的應用程式密碼：

   - 登入你的 Google 帳戶
   - 前往 [Google Account Security](https://myaccount.google.com/security)
   - 開啟兩步驟驗證
   - 在"應用程式密碼"中生成一個新的應用程式密碼

2. 安裝必要的 Python 套件：

   ```bash
   pip install -r requirements.txt
   ```

3. 設置環境變數：
   - 複製 `.env.example` 到 `.env`
   ```bash
   cp .env.example .env
   ```
   - 編輯 `.env` 文件，填入你的 Gmail 認證資訊：
   ```
   GMAIL_EMAIL=your.email@gmail.com
   GMAIL_APP_PASSWORD=your-app-password
   ```

## 使用方法

1. 使用環境變數（推薦）：

   ```python
   # 初始化寄件者（會自動讀取環境變數）
   sender = GmailSender()
   ```

2. 或直接提供認證資訊：

   ```python
   sender = GmailSender(
       email="your.email@gmail.com",
       password="your-app-password"
   )
   ```

3. 發送郵件範例：

   ```python
   # 發送純文字郵件
   sender.send_email(
       to_emails=["recipient@example.com"],
       subject="測試郵件",
       body="這是一封測試郵件！"
   )

   # 發送HTML格式郵件
   html_content = """
   <html>
       <body>
           <h1>你好！</h1>
           <p>這是一封<b>HTML</b>格式的郵件！</p>
       </body>
   </html>
   """
   sender.send_email(
       to_emails=["recipient@example.com"],
       subject="HTML測試郵件",
       body=html_content,
       is_html=True
   )

   # 發送帶附件的郵件
   sender.send_email(
       to_emails=["recipient@example.com"],
       subject="帶附件的郵件",
       body="請查看附件。",
       attachments=["path/to/your/file.pdf"]
   )
   ```

## 注意事項

- 請勿在程式碼中直接存儲 Gmail 密碼
- 建議使用環境變數來存儲敏感資訊
- 確保你的 Gmail 帳戶已開啟"低安全性應用程式存取"或使用應用程式密碼
- 注意 Gmail 的發送限制（每日限制等）
- 確保 `.env` 文件已加入到 `.gitignore`

## 安全提醒

- 永遠不要將你的 Gmail 密碼或應用程式密碼提交到版本控制系統
- 建議使用環境變數或配置文件來存儲敏感資訊
- 定期更換應用程式密碼以提高安全性
- 確保 `.env` 文件的權限設置正確（建議設為 600）
