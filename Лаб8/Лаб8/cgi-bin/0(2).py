#!/usr/bin/env python3
import cgi
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
t1 = form.getfirst("t1", "Значение не указано")
t2 = form.getfirst("t2", "Значение не указано")

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

print("""<p>Логин: {}</p>""".format(t1))
print("""<p>Пароль: {}</p>""".format(t2))

print("""</div></body>
        </html>""")
