import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "tlb.python@gmail.com"
    password = "qobghdhymgyyaotl"

    receiver = "tlbutler007@gmail.com"
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

#on mac ssl error - go to directory for python and click "install certificates"
