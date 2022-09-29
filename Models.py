from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class medios(db.Model):
    rowid= db.Column(db.Integer, primary_key=True)
    TV= db.Column(db.Integer)
    radio= db.Column(db.Integer)
    newspaper= db.Column(db.Integer)
    sales=db.Column(db.Integer)

    def __init__(self, TV, radio, newspaper, sales):
        super().__init__()
        self.TV=TV
        self.radio=radio
        self.newspaper=newspaper
        self.sales=sales

        
    def __str__(self):
        return "\nTV:{}. radio:{}. newspaper:{}. sales:{}.\n".format(
            self.TV,
            self.radio,
            self.newspaper,
            self.sales
    )

    def serialize(self):
        return{
            "rowid":self.rowid,
            "TV":self.TV,
            "radio":self.radio,
            "newspaper":self.newspaper,
            "sales":self.sales,
        }
