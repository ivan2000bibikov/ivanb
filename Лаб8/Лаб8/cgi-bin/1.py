#!/usr/bin/env python3
import smtplib
import cgi
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
name = form.getfirst("os1")
mail = form.getfirst("os2")
message = form.getfirst("os3")

Body = "\n" + "Letter from: ".format() + name + ". Sender address: ".format() + mail + "\n" + "Message text: ".format() + message

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("G111g333ggg111@gmail.com", "jjgjidgjidfkokosfkosf")
server.sendmail(name, "G111g333ggg111@gmail.com", Body)
server.quit()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
        <meta charset="utf-8">
        <style>
        * {
		margin: 0;
		padding: 0;
		border: 0;
		font-family: Calibri;
		}
		p {
		color: white;
		font-weight: bold;
		margin-top: 10px;
		margin-bottom: 10px;
		margin-left: 10px;
		margin-right: 10px;
		font-size: 18px;
		background-color: rgb(40, 167, 68);
		border-radius: 5px;
		padding-left: 10px;
		padding-right: 10px;
		}
		div {
		position: absolute;
		min-width: 1px;
		min-height: 1px;
		background-color: rgb(100, 222, 137);
		border-radius: 15px;
		z-index: -1;
		top: 1%;
		left: 1%;
		}
		</style>
        </head>
        <body><div>""")

print("""<p>Вы отправили сообщение на почту. Нажмите <a href="/index1.html">сюда</a>, чтобы вернуться назад</p>""")

print("""</div></body>
        </html>""")