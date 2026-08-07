from extensions import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    mot_de_passe = db.Column(db.String(100))
    role = db.Column(db.String(20), default='user')

class Produit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    description = db.Column(db.Text)
    prix = db.Column(db.Float) 
    stock = db.Column(db.Integer)

class Panier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class PanierProduit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    panier_id = db.Column(db.Integer, db.ForeignKey('panier.id'))
    produit_id = db.Column(db.Integer, db.ForeignKey('produit.id'))
    quantite = db.Column(db.Integer, default=1)

class Commande(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_commande = db.Column(db.DateTime, default=datetime.utcnow)
    statut = db.Column(db.String(20), default='en attente')
    total = db.Column(db.Float)

class CommandeProduit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    commande_id = db.Column(db.Integer, db.ForeignKey('commande.id'))
    produit_id = db.Column(db.Integer, db.ForeignKey('produit.id'))
    quantite = db.Column(db.Integer)
    prix_unitaire = db.Column(db.Float)  # le prix au moment de l'achat

