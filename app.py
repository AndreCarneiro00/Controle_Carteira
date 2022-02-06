from flask import Flask, Blueprint, redirect, url_for, render_template, request, session, flash
from datetime import timedelta, datetime
from flask_sqlalchemy import SQLAlchemy
from models import db, Operacoes,EventosAcionarios, Proventos,HistoricoCotacao, Carteira

def create_app():
    app = Flask(__name__)
    app.secret_key = "hello"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///controle_carteira.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.permanent_session_lifetime = timedelta(minutes=5)
    db.init_app(app)
    return app


app = create_app()

@app.route("/views")
@app.route("/")
def resumo():
    return render_template("resumo.html")

@app.route("/form_cadastro_rv", methods=["GET", "POST"])
def form_cadastro_rv():
    if request.method == "POST":
        categoria_ativo = request.form["categoria_ativo"]
        ticker = request.form["ticker"]
        data = datetime.strptime(request.form["data"], "%Y-%m-%d")
        quantidade = int(request.form["quantidade"])
        preco = float(request.form["preco"])
        emolumento = float(request.form["emolumento"])
        corretagem = float(request.form["corretagem"])
        corretora = request.form["corretora"]
        modalidade = request.form["modalidade"]
        setor = request.form["setor"]

        session['categoria_ativo'] = categoria_ativo
        session['ticker'] = ticker
        session['data'] = data
        session['quantidade'] = quantidade
        session['preco'] = preco
        session['emolumento'] = emolumento
        session['corretagem'] = corretagem
        session['corretora'] = corretora
        session['modalidade'] = modalidade
        session['setor'] = setor

        db_op_rv = Operacoes(ticker=ticker, quantidade=quantidade, preco=preco, data_operacao=data, taxa_emolumento=emolumento,
                             taxa_corretagem=corretagem, categoria_ativo=categoria_ativo, corretora=corretora, modalidade=modalidade, setor=setor)
        db.session.add(db_op_rv)
        db.session.commit()

        return redirect(url_for("form_cadastro_rv"))

    else:
        return render_template("cadastro_rv.html")

@app.route("/form_cadastro_rf", methods=["GET", "POST"])
def form_cadastro_rf():
    if request.method == "POST":
        categoria_ativo = request.form["rf_options"]
        data = datetime.strptime(request.form["data"], "%Y-%m-%d")
        preco = float(request.form["valor"])
        corretora = request.form["corretora"]
        modalidade = request.form["modalidade"]
        indexador = request.form['indexador']

        session['categoria_ativo'] = categoria_ativo
        session['data'] = data
        session['preco'] = preco
        session['corretora'] = corretora
        session['modalidade'] = modalidade
        session['indexador'] = indexador

        db_op_rv = Operacoes(preco=preco, data_operacao=data, indexador=indexador, corretora=corretora, modalidade=modalidade)
        db.session.add(db_op_rv)
        db.session.commit()

        return redirect(url_for("form_cadastro_rf"))

    else:
        return render_template("cadastro_rf.html")

@app.route("/carteira_ideal_cadastro")
def carteira_ideal_cadastro():
    return render_template("resumo.html")

@app.route("/carteira_ideal")
def carteira_ideal():
    return render_template("resumo.html")


@app.route("/tabelas")
def tabelas():
    return render_template("resumo.html")

# db_ops = Operacoes()
# db_prov = Proventos()
# db_cotacao = HistoricoCotacao()
# db_carteira = Carteira()
# db_eventos = EventosAcionarios()


if __name__ == "__main__":
    app.app_context().push()
    db.create_all(app=create_app())  # Creates the database if it not exist
    app.run(debug=True)  # debug True update the appsite for us
