import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Vizualizacija podatkov pacientov onkologije.</h1><p>Ta aplikacija se uporablja za vizualizacijo ter upravljanje podatkov baze pacientov onkologije. </p>"

app.run()