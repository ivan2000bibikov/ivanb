#!/usr/bin/env python3
import cgi
import sys
import codecs
import sqlite3
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

db = sqlite3.connect('book.db')
sql = db.cursor()
sql2 = db.cursor()
sql3 = db.cursor()
sql4 = db.cursor()
sql5 = db.cursor()
sql6 = db.cursor()
sql7 = db.cursor()
sql8 = db.cursor()
sql9 = db.cursor()
sql10 = db.cursor()
sql11 = db.cursor()
sql12 = db.cursor()
sql13 = db.cursor()
sql14 = db.cursor()
sql15 = db.cursor()
sql16 = db.cursor()
sql17 = db.cursor()
sql18 = db.cursor()
sql19 = db.cursor()
sql20 = db.cursor()

sql.execute("SELECT name, avtor FROM books WHERE name = 'Граф Монте-Кристо'")
sql2.execute("SELECT opis, god FROM books WHERE name = 'Граф Монте-Кристо'")

sql3.execute("SELECT name, avtor FROM books WHERE name = 'Три мушкетера'")
sql4.execute("SELECT opis, god FROM books WHERE name = 'Три мушкетера'")

sql5.execute("SELECT name, avtor FROM books WHERE name = 'Время жить и время умирать'")
sql6.execute("SELECT opis, god FROM books WHERE name = 'Время жить и время умирать'")

sql7.execute("SELECT name, avtor FROM books WHERE name = 'Рождественская песнь'")
sql8.execute("SELECT opis, god FROM books WHERE name = 'Рождественская песнь'")

sql9.execute("SELECT name, avtor FROM books WHERE name = 'Евгений Онегин'")
sql10.execute("SELECT opis, god FROM books WHERE name = 'Евгений Онегин'")

sql11.execute("SELECT name, avtor FROM books WHERE name = 'Граф Монте-Кристо'")
sql12.execute("SELECT opis, god FROM books WHERE name = 'Граф Монте-Кристо'")

sql13.execute("SELECT name, avtor FROM books WHERE name = 'Три мушкетера'")
sql14.execute("SELECT opis, god FROM books WHERE name = 'Три мушкетера'")

sql15.execute("SELECT name, avtor FROM books WHERE name = 'Время жить и время умирать'")
sql16.execute("SELECT opis, god FROM books WHERE name = 'Время жить и время умирать'")

sql17.execute("SELECT name, avtor FROM books WHERE name = 'Рождественская песнь'")
sql18.execute("SELECT opis, god FROM books WHERE name = 'Рождественская песнь'")

sql19.execute("SELECT name, avtor FROM books WHERE name = 'Евгений Онегин'")
sql20.execute("SELECT opis, god FROM books WHERE name = 'Евгений Онегин'")

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
		.p11 {
		font-weight: bold;
		font-size: 24px;
		margin-left: 118px;
		}
		.p12 {
		font-style: italic;
		font-size: 20px;
		margin-left: 148px;
		}
		.p21 {
		font-weight: bold;
		font-size: 24px;
		margin-left: 64px;
		}
		.p22 {
		font-style: italic;
		font-size: 20px;
		margin-left: 134px;
		}
		.p31 {
		font-weight: bold;
		font-size: 24px;
		margin-left: 104px;
		}
		.p32 {
		font-style: italic;
		font-size: 20px;
		margin-left: 154px;
		}
		.p41 {
		font-weight: bold;
		font-size: 24px;
		margin-left: 142px;
		}
		.p42 {
		font-style: italic;
		font-size: 20px;
		margin-left: 150px;
		}
		.p51 {
		font-weight: bold;
		font-size: 24px;
		margin-left: 132px;
		}
		.p52 {
		font-style: italic;
		font-size: 20px;
		margin-left: 136px;
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
		.img1 {
		width: 400px;
		height: 600px;
		margin-top: 10px;
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
		button {
		color: white;
		font-weight: bold;
		width: 127px;
		height: 25px;
		margin-top: 10px;
		background-color: rgb(40, 167, 68);
		border-radius: 5px;
		font-size: 15px;
		margin-left: 5px;
		margin-right: 5px;
		}
		#d1 {display: none;}
		#d2 {display: none;}
		#d3 {display: none;}
		#d4 {display: none;}
		#d5 {display: none;}
		#ad1 {display: none;}
		#ad2 {display: none;}
		#ad3 {display: none;}
		#ad4 {display: none;}
		#ad5 {display: none;}
    </style>
</head>
<body>

	<button id="b1" onclick="Dyma()">Дюма</button>
	<button id="b2" onclick="Remark()">Ремарк</button>
	<button id="b3" onclick="Dikkens()">Диккенс</button>
	<button id="b4" onclick="Pyshkin()">Пушкин</button>
	<button id="b5" onclick="god2015()">Год издания: 2015</button>
	<button id="b6" onclick="god2018()">Год издания: 2018</button>
	<button id="b7" onclick="god2019()">Год издания: 2019</button>
	<button id="b8" onclick="all111()">Показать всё</button>
	<button id="b9" onclick="hall()">Сбросить</button>""")

print("""<div id="d1">""")
print("""<p class="p11">{}</p>""".format(sql.fetchone()[0]))
print("""<p class="p12">{}</p>""".format(sql.fetchone()[1]))
print("""<img class="img1" class src="https://s1.livelib.ru/boocover/1003012244/o/4d2a/Aleksandr_Dyuma__Graf_MonteKristo.jpeg">""")
print("""<p class="p3">{}</p>""".format(sql2.fetchone()[0]))
print("""<p class="p4">{}</p>""".format(sql2.fetchone()[1]))
print("""</div>""")

print("""<div id="d2">""")
print("""<p class="p21">{}</p>""".format(sql5.fetchone()[0]))
print("""<p class="p22">{}</p>""".format(sql5.fetchone()[1]))
print("""<img class="img1" class src="https://s1.livelib.ru/boocover/1003006627/o/325d/Erih_Mariya_Remark__Vremya_zhit_i_vremya_umirat.jpeg">""")
print("""<p class="p3">{}</p>""".format(sql6.fetchone()[0]))
print("""<p class="p4">{}</p>""".format(sql6.fetchone()[1]))
print("""</div>""")

print("""<div id="d3">""")
print("""<p class="p31">{}</p>""".format(sql7.fetchone()[0]))
print("""<p class="p32">{}</p>""".format(sql7.fetchone()[1]))
print("""<img class="img1" class src="https://s1.livelib.ru/boocover/1002722681/o/8da1/Charlz_Dikkens__Rozhdestvenskaya_pesn.jpeg">""")
print("""<p class="p3">{}</p>""".format(sql8.fetchone()[0]))
print("""<p class="p4">{}</p>""".format(sql8.fetchone()[1]))
print("""</div>""")

print("""<div id="d4">""")
print("""<p class="p41">{}</p>""".format(sql3.fetchone()[0]))
print("""<p class="p42">{}</p>""".format(sql3.fetchone()[1]))
print("""<img class="img1" class src="https://s1.livelib.ru/boocover/1003057151/o/d278/Aleksandr_Dyuma__Tri_mushketera.jpeg">""")
print("""<p class="p3">{}</p>""".format(sql4.fetchone()[0]))
print("""<p class="p4">{}</p>""".format(sql4.fetchone()[1]))
print("""</div>""")

print("""<div id="d5">""")
print("""<p class="p51">{}</p>""".format(sql9.fetchone()[0]))
print("""<p class="p52">{}</p>""".format(sql9.fetchone()[1]))
print("""<img class="img1" class src="https://s1.livelib.ru/boocover/1001448384/o/80cb/Aleksandr_Pushkin__Evgenij_Onegin_sbornik.jpeg">""")
print("""<p class="p3">{}</p>""".format(sql10.fetchone()[0]))
print("""<p class="p4">{}</p>""".format(sql10.fetchone()[1]))
print("""</div>""")

print("""<div id="ad1">""")
print("""<p class="p11">{}</p>""".format(sql11.fetchone()[0]))
print("""<p class="p12">{}</p>""".format(sql11.fetchone()[1]))
print("""<p class="p3">{}</p>""".format(sql12.fetchone()[0]))
print("""<p class="p4">{}</p>""".format(sql12.fetchone()[1]))
print("""</div>""")

print("""<div id="ad2">""")
print("""<p class="p21">{}</p>""".format(sql15.fetchone()[0]))
print("""<p class="p22">{}</p>""".format(sql15.fetchone()[1]))
print("""<p class="p3">{}</p>""".format(sql16.fetchone()[0]))
print("""<p class="p4">{}</p>""".format(sql16.fetchone()[1]))
print("""</div>""")

print("""<div id="ad3">""")
print("""<p class="p31">{}</p>""".format(sql17.fetchone()[0]))
print("""<p class="p32">{}</p>""".format(sql17.fetchone()[1]))
print("""<p class="p3">{}</p>""".format(sql18.fetchone()[0]))
print("""<p class="p4">{}</p>""".format(sql18.fetchone()[1]))
print("""</div>""")

print("""<div id="ad4">""")
print("""<p class="p41">{}</p>""".format(sql13.fetchone()[0]))
print("""<p class="p42">{}</p>""".format(sql13.fetchone()[1]))
print("""<p class="p3">{}</p>""".format(sql14.fetchone()[0]))
print("""<p class="p4">{}</p>""".format(sql14.fetchone()[1]))
print("""</div>""")

print("""<div id="ad5">""")
print("""<p class="p51">{}</p>""".format(sql19.fetchone()[0]))
print("""<p class="p52">{}</p>""".format(sql19.fetchone()[1]))
print("""<p class="p3">{}</p>""".format(sql20.fetchone()[0]))
print("""<p class="p4">{}</p>""".format(sql20.fetchone()[1]))
print("""</div>""")

print("""<script>
		var d1 = document.getElementById("d1");
		var d2 = document.getElementById("d2");
		var d3 = document.getElementById("d3");
		var d4 = document.getElementById("d4");
		var d5 = document.getElementById("d5");
		var ad1 = document.getElementById("ad1");
		var ad2 = document.getElementById("ad2");
		var ad3 = document.getElementById("ad3");
		var ad4 = document.getElementById("ad4");
		var ad5 = document.getElementById("ad5");
		let a = 0;
		let b = 0;
		let c = 0;
		let d = 0;

		function Dyma() {
			if(d1.style.display === "none") {
				d1.style.display = "inline";
				a = 2;
			}
			else {
				d1.style.display = "none";
				a = 0;
			}
			if(d4.style.display === "none") {
				d4.style.display = "inline";
				a = 2;
			}
			else {
				d4.style.display = "none";
				a = 0;
			}

			ad1.style.display = "none";
			ad2.style.display = "none";
			ad3.style.display = "none";
			ad4.style.display = "none";
			ad5.style.display = "none";
			pr()
		}

		function Remark() {
			if(d2.style.display === "none") {
				d2.style.display = "inline";
				b = 1;
			}
			else {
				d2.style.display = "none";
				b = 0;
			}

			ad1.style.display = "none";
			ad2.style.display = "none";
			ad3.style.display = "none";
			ad4.style.display = "none";
			ad5.style.display = "none";
			pr()
		}

		function Dikkens() {
			if(d3.style.display === "none") {
				d3.style.display = "inline";
				c = 1;
			}
			else {
				d3.style.display = "none";
				c = 0;
			}

			ad1.style.display = "none";
			ad2.style.display = "none";
			ad3.style.display = "none";
			ad4.style.display = "none";
			ad5.style.display = "none";
			pr()
		}

		function Pyshkin() {
			if(d5.style.display === "none") {
				d5.style.display = "inline";
				d = 1;
			}
			else {
				d5.style.display = "none";
				d = 0;
			}

			ad1.style.display = "none";
			ad2.style.display = "none";
			ad3.style.display = "none";
			ad4.style.display = "none";
			ad5.style.display = "none";
			pr()
		}

		function god2015() {
			if(d5.style.display === "none") {
				d5.style.display = "inline";
				d = 1;
			}
			else {
				d5.style.display = "none";
				d = 0;
			}

			ad1.style.display = "none";
			ad2.style.display = "none";
			ad3.style.display = "none";
			ad4.style.display = "none";
			ad5.style.display = "none";
			pr()
		}

		function god2018() {
			if(d2.style.display === "none") {
				d2.style.display = "inline";
				b = 1;
			}
			else {
				d2.style.display = "none";
				b = 0;
			}
			if(d3.style.display === "none") {
				d3.style.display = "inline";
				c = 1;
			}
			else {
				d3.style.display = "none";
				c = 0;
			}

			ad1.style.display = "none";
			ad2.style.display = "none";
			ad3.style.display = "none";
			ad4.style.display = "none";
			ad5.style.display = "none";
			pr()
		}

		function god2019() {
			if(d1.style.display === "none") {
				d1.style.display = "inline";
				a = 2;
			}
			else {
				d1.style.display = "none";
				a = 0;
			}
			if(d4.style.display === "none") {
				d4.style.display = "inline";
				a = 2;
			}
			else {
				d4.style.display = "none";
				a = 0;
			}

			ad1.style.display = "none";
			ad2.style.display = "none";
			ad3.style.display = "none";
			ad4.style.display = "none";
			ad5.style.display = "none";
			pr()
		}

		function all111() {
			d1.style.display = "none";
			d2.style.display = "none";
			d3.style.display = "none";
			d4.style.display = "none";
			d5.style.display = "none";
			ad1.style.display = "inline";
			ad2.style.display = "inline";
			ad3.style.display = "inline";
			ad4.style.display = "inline";
			ad5.style.display = "inline";

			a = 1;
			b = 1;
			c = 1;
			d = 1;
		}

		function hall() {
			d1.style.display = "none";
			d2.style.display = "none";
			d3.style.display = "none";
			d4.style.display = "none";
			d5.style.display = "none";
			ad1.style.display = "none";
			ad2.style.display = "none";
			ad3.style.display = "none";
			ad4.style.display = "none";
			ad5.style.display = "none";

			a = 0;
			b = 0;
			c = 0;
			d = 0;
		}
		function pr() {
			if (a == 2 && d == 1 && c == 1 && d == 1 ) {
			d1.style.display = "none";
			d2.style.display = "none";
			d3.style.display = "none";
			d4.style.display = "none";
			d5.style.display = "none";
			ad1.style.display = "inline";
			ad2.style.display = "inline";
			ad3.style.display = "inline";
			ad4.style.display = "inline";
			ad5.style.display = "inline";
			}
			else {
			ad1.style.display = "none";
			ad2.style.display = "none";
			ad3.style.display = "none";
			ad4.style.display = "none";
			ad5.style.display = "none";
			}
		}
	</script>

</body>
</html>""")