from mgc import db

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f'<Name {self.name}>' 

class Users(db.Model):
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(8), primary_key=True)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f'<Name {self.name}>' 