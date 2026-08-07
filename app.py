from flask import Flask
from extensions import db
from models import User, Produit, Panier, PanierProduit, Commande, CommandeProduit

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)