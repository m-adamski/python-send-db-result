import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def generate_message(config, workbook_stream):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = config.smtp_sender
    message["To"] = config.smtp_receiver
    message["Subject"] = config.smtp_subject

    # Add body to email
    message.attach(MIMEText(config.smtp_message, "plain"))

    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(workbook_stream)

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {config.smtp_attachment}"
    )

    # Add attachment to message and convert message to string
    message.attach(part)

    return message


def send(config, message):
    try:
        with smtplib.SMTP(config.smtp_server, config.smtp_port, timeout=10) as server:
            if config.smtp_protocol == "STARTTLS":
                server.starttls()

            server.login(config.smtp_user, config.smtp_password)
            server.sendmail(config.smtp_sender, config.smtp_receiver.replace(" ", "").split(","), message.as_string())

            return True
    except Exception as error:
        print("An error occurred while trying to send a message:", error)
        return False
