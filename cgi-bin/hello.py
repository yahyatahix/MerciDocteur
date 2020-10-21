#!/usr/bin/python3.7
# coding:utf-8       # Pour le source avec des caractères Unicode

# Produire l'entête nécessaire, avec le saut de ligne
print ("Content-type:text/html; charset=UTF-8")    # ce qui suit est du HTML
print   ()                                         # ligne vide

# Sortir le HTML
a = """
<!DOCTYPE html>
 <html>
 <head><title>Bonjour Python</title></head>
 <body>
   <p>Bonjour...</p>
   <p>Contenu <b>HTML</b> produit par Python</p>
  </body>
</html>
"""
print(a)
