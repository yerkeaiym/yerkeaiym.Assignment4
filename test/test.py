from src import *
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:erkeaiym2408@localhost/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'

db = SQLAlchemy(app)

class Coin(db.Model):
    tablename = "coins"
    coin_name = db.Column(db.String, primary_key = True)
    coin_price= db.Column(db.Integer(20))
    coin_marketcap= db.Column(db.Integer(20))
    coin_circulating_supply = db.Column(db.Integer(20))
    coin_valume = db.Column(db.Integer(20))
    def init(self, decentraland):
        self.decentraland = decentraland
        
           
@app.route('/', methods = ['GET', 'POST'])
def index():
    coin_name = ['bitcoin', 'Binance Coin', 'Tether']
    checking = ['', '', '']
    for i in range(3):
        if db.session.query(Coin).filter(Coin.login == coin_name[i]).count() == 0:
            data = Coin(coin_name[i],checking[i])
            db.session.add(data)
    db.session.commit()
    return render_template('Coin.html')
    
    

@app.route('/check', methods = ['POST'])
def submit():
    checkLog = request.form['Decentraland']
    

 
if __name__ == '__main':
    app.run()
