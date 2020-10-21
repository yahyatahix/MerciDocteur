#!/usr/bin/python3
# coding:utf-8

##
#  Ecriture dans fichier "guestbook.html"
#  Paramètres reçus par méthode POST
#  NE génère pas page HTML, mais une réponse 
#  en retour (AJAX)
#
 
import cgi, cgitb , datetime, os, re

# Lecture des données formulaire
form = cgi.FieldStorage() 
xnom = form.getvalue('nom')
xprenom  = form.getvalue('prenom')
xville = form.getvalue('ville')
xcomment = form.getvalue('comment')

xemail = form.getvalue('email')

xdate=datetime.datetime.now()
year=xdate.year
jour=xdate.strftime("%B")
mois=xdate.strftime("%d")


numpost=0
with open("../livreDor/guestbook.html", 'r') as file:
    numpost =len(re.findall('Post',file.read().replace('\n', '')) )+1

# Création du fichier si n'existe pas et ouverture en mode append 
gb = open("../livreDor/guestbook.html", "a")

# Ecriture des informations dans le fichier avec balisage HTML
gb.write('<div> <hr />')
gb.write('<div style="margin-left: 50px">')
gb.write ("<strong><p><em>Post</em></strong>: "+str(numpost)+"<br />\n")

gb.write ("<strong><p><em>Date</em></strong>: le "+ xdate.strftime("%d")+" "+xdate.strftime("%B")+" "+xdate.strftime("%Y") +" <br />\n")
gb.write ("<strong><em>Nom</em></strong>: "+str(xnom)+", ")
gb.write(str(xprenom)+"<br />")
gb.write ("<strong><em>Adresse</em></strong>: "+str(xville)+"</p>\n")
gb.write("<strong><em>Email</em>: </strong>"+str(xemail)+"<br />")
#gb.write("<blockquote>")
gb.write ("<strong><em>Message</em>: </strong> <blockquote>"+str(xcomment)+"</blockquote>")

navigateur="Inconnue"
ip_address="Inconnue"
for key in os.environ.keys():
	if key == "REMOTE_ADDR":
		ip_address =os.environ[key]
	if key == "HTTP_USER_AGENT":
		navigateur=os.environ[key]

gb.write("<strong> Vous utiliser le navigateur </strong>: \" "+navigateur+" \"<br/>")
gb.write("<strong>Connecté à partir de </strong>: "+ip_address+" \"</p>")
gb.write("</div>")
gb.write("</div>")

gb.close()

# Sortie sur UA de l'accusé de réception
print ("Content-type: text/html; charset=UTF-8\n")
print ("Merci %s %s <br/>" % (xnom, xprenom));
print ("Votre message a été transmis...")

