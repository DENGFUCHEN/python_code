import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication

file = 'E:\\python練習\\photo.jpg' #附件路徑
gmail_user = 'k4399888@gmail.com'
gmail_password = 'z10327061' # your gmail password
email_text = '此為測試郵件請勿回覆'   #郵件正文

msg = MIMEMultipart()
msg['Subject'] = '系統郵件'
msg['From'] = gmail_user
msg['To'] = 'dengfu24@gmail.com'

part_text=MIMEText(email_text)
msg.attach(part_text)             #把正文加到郵件體裡面去

#file = file           #獲取檔案路徑
part_attach1 = MIMEApplication(open(file,'rb').read())   #開啟附件
part_attach1.add_header('Content-Disposition','attachment',filename=file) #為附件命名
msg.attach(part_attach1)   #新增附件

with open('E:\\python練習\\photo.jpg', 'rb') as f:
    # 設定附件的MIME和檔名，這裡是png型別:
    mime = MIMEBase('image', 'jpg', filename='photo.jpg')
    # 加上必要的頭資訊:
    mime.add_header('Content-Disposition', 'attachment', filename='photo.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的內容讀進來:
    mime.set_payload(f.read())
    # 用Base64編碼:
    encoders.encode_base64(mime)
    # 新增到MIMEMultipart:
    msg.attach(mime)

#正文顯示附件圖片
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))


server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.send_message(msg)
server.quit()

print('Email sent!')