import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from typing import List, Optional
import os
from dotenv import load_dotenv

class GmailSender:
    def __init__(self, email: str = None, password: str = None):
        """
        Initialize Gmail sender with email and app password
        
        Args:
            email (str, optional): Gmail address. If None, will try to get from environment variable GMAIL_EMAIL
            password (str, optional): Gmail app password. If None, will try to get from environment variable GMAIL_APP_PASSWORD
        """
        load_dotenv()  # Load environment variables from .env file
        
        self.email = email or os.getenv('GMAIL_EMAIL')
        self.password = password or os.getenv('GMAIL_APP_PASSWORD')
        
        if not self.email or not self.password:
            raise ValueError("Email and password must be provided either directly or through environment variables")
            
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    def create_message(
        self,
        to_emails: List[str],
        subject: str,
        body: str,
        is_html: bool = False,
        attachments: Optional[List[str]] = None
    ) -> MIMEMultipart:
        """
        Create email message with optional HTML and attachments
        
        Args:
            to_emails (List[str]): List of recipient email addresses
            subject (str): Email subject
            body (str): Email body content
            is_html (bool): Whether the body is HTML format
            attachments (List[str], optional): List of file paths to attach
            
        Returns:
            MIMEMultipart: Composed email message
        """
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = ', '.join(to_emails)
        msg['Subject'] = subject

        # Add body
        content_type = 'html' if is_html else 'plain'
        msg.attach(MIMEText(body, content_type))

        # Add attachments if any
        if attachments:
            for file_path in attachments:
                if os.path.exists(file_path):
                    with open(file_path, 'rb') as f:
                        attachment = MIMEApplication(f.read())
                        attachment.add_header(
                            'Content-Disposition',
                            'attachment',
                            filename=os.path.basename(file_path)
                        )
                        msg.attach(attachment)

        return msg

    def send_email(
        self,
        to_emails: List[str],
        subject: str,
        body: str,
        is_html: bool = False,
        attachments: Optional[List[str]] = None
    ) -> bool:
        """
        Send email using Gmail SMTP
        
        Args:
            to_emails (List[str]): List of recipient email addresses
            subject (str): Email subject
            body (str): Email body content
            is_html (bool): Whether the body is HTML format
            attachments (List[str], optional): List of file paths to attach
            
        Returns:
            bool: True if email sent successfully, False otherwise
        """
        try:
            # Create message
            msg = self.create_message(to_emails, subject, body, is_html, attachments)

            # Connect to Gmail SMTP
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email, self.password)
                server.send_message(msg)

            print("Email sent successfully!")
            return True

        except Exception as e:
            print(f"Failed to send email: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    try:
        # Initialize sender using environment variables
        sender = GmailSender()
        
        # Example: Send plain text email
        sender.send_email(
            to_emails=["recipient@example.com"],
            subject="Test Email",
            body="This is a test email sent from Python!",
        )
        
        # Example: Send HTML email
        html_content = """
        <html>
            <body>
                <h1>Hello!</h1>
                <p>This is a <b>HTML</b> email sent from Python!</p>
            </body>
        </html>
        """
        sender.send_email(
            to_emails=["recipient@example.com"],
            subject="HTML Test Email",
            body=html_content,
            is_html=True,
        )

        # Example: Send email with attachment
        sender.send_email(
            to_emails=["recipient@example.com"],
            subject="Email with Attachment",
            body="Please find the attached file.",
            attachments=["path/to/your/file.pdf"],
        )
    except Exception as e:
        print(f"Failed to initialize sender: {str(e)}") 