# Gmail Automated Email Sender

# Gmail 自動寄信系統

這個 Python 腳本使用 Gmail SMTP 來發送自動化郵件，支援純文字、HTML 格式以及附件。

## Features 功能特點

- Support for plain text and HTML format emails / 支援純文字和 HTML 格式郵件
- Attachment support / 可發送附件
- Multiple recipients support / 支援多個收件人
- Gmail SMTP service integration / 使用 Gmail SMTP 服務
- Comprehensive error handling / 完整的錯誤處理
- Type hints support / 類型提示支援
- Environment variables support / 環境變數支援

## Setup 設置步驟

1. First, set up Gmail App Password / 首先，設置 Gmail 應用程式密碼：

   - Sign in to your Google Account / 登入你的 Google 帳戶
   - Go to [Google Account Security](https://myaccount.google.com/security) / 前往 Google 帳戶安全性設定
   - Enable 2-Step Verification / 開啟兩步驟驗證
   - Generate an App Password in "App Passwords" section / 在"應用程式密碼"中生成新密碼

2. Install required Python packages / 安裝必要的 Python 套件：

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables / 設置環境變數：
   - Copy `.env.example` to `.env` / 複製 `.env.example` 到 `.env`
   ```bash
   cp .env.example .env
   ```
   - Edit `.env` file with your Gmail credentials / 編輯 `.env` 文件，填入你的 Gmail 認證資訊：
   ```
   GMAIL_EMAIL=your.email@gmail.com
   GMAIL_APP_PASSWORD=your-app-password
   ```

## Usage 使用方法

1. Using environment variables (recommended) / 使用環境變數（推薦）：

   ```python
   # Initialize sender (will automatically read from environment variables)
   # 初始化寄件者（會自動讀取環境變數）
   sender = GmailSender()
   ```

2. Or provide credentials directly / 或直接提供認證資訊：

   ```python
   sender = GmailSender(
       email="your.email@gmail.com",
       password="your-app-password"
   )
   ```

3. Example usage / 使用範例：

   ```python
   # Send plain text email / 發送純文字郵件
   sender.send_email(
       to_emails=["recipient@example.com"],
       subject="Test Email",
       body="This is a test email sent from Python!",
   )

   # Send HTML email / 發送 HTML 格式郵件
   html_content = """
   <html>
       <body>
           <h1>Hello! 你好！</h1>
           <p>This is a <b>HTML</b> email sent from Python!</p>
           <p>這是一封由 Python 發送的 <b>HTML</b> 格式郵件！</p>
       </body>
   </html>
   """
   sender.send_email(
       to_emails=["recipient@example.com"],
       subject="HTML Test Email",
       body=html_content,
       is_html=True
   )

   # Send email with attachment / 發送帶附件的郵件
   sender.send_email(
       to_emails=["recipient@example.com"],
       subject="Email with Attachment",
       body="Please find the attached file. / 請查看附件。",
       attachments=["path/to/your/file.pdf"]
   )
   ```

## Notes 注意事項

- Never store Gmail password in code / 請勿在程式碼中直接存儲 Gmail 密碼
- Use environment variables for sensitive information / 建議使用環境變數來存儲敏感資訊
- Ensure your Gmail account has "Less secure app access" enabled or use App Password / 確保你的 Gmail 帳戶已開啟"低安全性應用程式存取"或使用應用程式密碼
- Be aware of Gmail sending limits / 注意 Gmail 的發送限制（每日限制等）
- Ensure `.env` file is in `.gitignore` / 確保 `.env` 文件已加入到 `.gitignore`

## Security Reminders 安全提醒

- Never commit your Gmail password or App Password to version control / 永遠不要將你的 Gmail 密碼或應用程式密碼提交到版本控制系統
- Use environment variables or configuration files for sensitive information / 建議使用環境變數或配置文件來存儲敏感資訊
- Regularly rotate your App Password / 定期更換應用程式密碼
- Set proper permissions for `.env` file (recommended: 600) / 確保 `.env` 文件的權限設置正確（建議設為 600）

## License 授權條款

MIT License / MIT 授權條款

## Contributing 貢獻指南

Feel free to open issues or submit pull requests for any improvements.
歡迎開立 Issue 或提交 Pull Request 來改善這個專案。
