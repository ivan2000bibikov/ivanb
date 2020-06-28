#!/usr/bin/env python3
import cgi
import sys
import codecs
import sqlite3
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

db = sqlite3.connect('book.db')
sql = db.cursor()
sql2 = db.cursor()

sql.execute("SELECT * FROM books WHERE name = 'Граф Монте-Кристо'")
sql2.execute("SELECT opis, god FROM books WHERE name = 'Граф Монте-Кристо'")

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
			margin-top: 10px;
			}
			body {
			background-color: rgb(241, 241, 241);
			}
			.p1 {
			font-weight: bold;
			font-size: 24px;
			margin-left: 118px;
			}
			.p2 {
			font-style: italic;
			font-size: 20px;
			margin-left: 148px;
			}
			.p3 {
			text-align: justify;
			font-size: 18px;
			margin-left: 20px;
			margin-right: 20px;
			}
			.p4 {
			text-align: justify;
			font-size: 18px;
			margin-top: 2px;
			margin-left: 384px;
			}
			img {
			width: 400px;
			height: 600px;
			margin-top: 20px;
			margin-left: 20px;
			}
			div {
			margin-top: 1%;
			margin-left: 1%;
			padding-bottom: 20px;
			width: 440px;
			background-color: white;
			border: solid 1px rgb(180, 180, 180);
			border-radius: 25px;
			float: left;
			}
            </style>
        </head>
        <body><div>""")

print("""<p class="p1">{}</p>""".format(sql.fetchone()[0]))
print("""<p class="p2">{}</p>""".format(sql.fetchone()[1]))
print("""<img src="https://s1.livelib.ru/boocover/1003012244/o/4d2a/Aleksandr_Dyuma__Graf_MonteKristo.jpeg">""")
print("""<p class="p3">{}</p>""".format(sql2.fetchone()[0]))
print("""<p class="p4">{}</p>""".format(sql2.fetchone()[1]))
print("""</div></body></html>""")