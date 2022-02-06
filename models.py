from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Operacoes(db.Model):
    __tablename__ = "operacoes"

    _id = db.Column("id", db.Integer(), primary_key=True)
    ticker = db.Column("ticker", db.String(10))
    quantidade = db.Column("quantidade", db.Integer())
    preco = db.Column('preco', db.Float())
    data_operacao = db.Column('data_operacao', db.Date())
    taxa_emolumento = db.Column('taxa_emolumento', db.Float())
    taxa_corretagem = db.Column('taxa_corretagem', db.Float())
    categoria_ativo = db.Column("categoria_ativo", db.String())
    indexador = db.Column("indexador", db.String())
    modalidade = db.Column('modalidade', db.String(10)) # Compra ou venda
    corretora = db.Column('corretora', db.String())
    setor = db.Column('setor', db.String())

    def __init__(self, ticker: str = None, quantidade: int = None, preco: float = None, data_operacao = None,
                 taxa_emolumento = None, taxa_corretagem = None, modalidade = None, indexador=None, corretora=None,
                 categoria_ativo=None, setor=None):
        self.ticker = ticker
        self.quantidade = quantidade
        self.preco = preco
        self.data_operacao = data_operacao
        self.taxa_emolumento = taxa_emolumento
        self.taxa_corretagem = taxa_corretagem
        self.modalidade = modalidade
        self.indexador = indexador
        self.corretora = corretora
        self.categoria_ativo = categoria_ativo
        self.setor = setor


class HistoricoCotacao(db.Model):
    __tablename__ = "historico_cotacao"
    _id = db.Column("id", db.Integer(), primary_key=True)
    ticker = db.Column("ticker", db.String(10))
    date = db.Column("date", db.Date())
    high = db.Column("high", db.Float())
    low = db.Column("low", db.Float())
    open = db.Column("open", db.Float())
    close = db.Column("close", db.Float())
    volume = db.Column("volume", db.Float())
    adj_close = db.Column("adj_close", db.Float())

    def __init__(self, ticker = None, date=None, high=None, low=None, open=None, close=None, volume=None, adj_close=None):
        self.ticker = ticker
        self.date = date
        self.high = high
        self.low = low
        self.open = open
        self.close = close
        self.volume = volume
        self.adj_close = adj_close


class Carteira(db.Model):
    __tablename__ = "carteira"

    _id = db.Column("id", db.Integer(), primary_key=True)
    ticker = db.Column("ticker", db.String(10))
    data = db.Column("data", db.Date())
    quantidade = db.Column('quantidade', db.Float())
    preco_medio = db.Column('preco_medio', db.Float())
    categoria_ativo = db.Column('categoria_ativo', db.String())

    def __init__(self, ticker=None, data=None, quantidade=None, preco_medio=None, categoria_ativo=None):
        self.ticker = ticker
        self.quantidade = quantidade
        self.preco_medio = preco_medio
        self.data = data
        self.categoria_ativo = categoria_ativo


class Proventos(db.Model):
    __tablename__ = "proventos"

    _id = db.Column("id", db.Integer, primary_key=True)
    ticker = db.Column("ticker", db.String(10))
    valor = db.Column("valor", db.Float())
    data = db.Column('data', db.Date())
    modalidade = db.Column('modalidade', db.String(10))

    def __init__(self, ticker=None, quantidade=None, preco_medio=None, data=None, modalidade=None):
        self.ticker = ticker
        self.quantidade = quantidade
        self.preco_medio = preco_medio
        self.data_operacao = data
        self.modalidade = modalidade


class EventosAcionarios(db.Model):
    __tablename__ = "eventos_acionarios"

    _id = db.Column("id", db.Integer, primary_key=True)
    ticker = db.Column("ticker", db.String(10))
    fator = db.Column("quantidade", db.String())
    data = db.Column('data', db.Date())
    modalidade = db.Column('modalidade', db.String())

    def __init__(self, ticker=None, fator=None, data=None, modalidade=None):
        self.ticker = ticker
        self.fator = fator
        self.data = data
        self.modalidade = modalidade

class CarteiraIdealPesos(db.Model):
    __tablename__ = "carteira_ideal_pesos"

    _id = db.Column("id", db.Integer, primary_key=True)
    ticker = db.Column("ticker", db.String(10))
    categoria_ativo = db.Column('categoria_ativo', db.String())
    porcentagem = db.Column('porcentagem', db.Float)
    modalidade = db.Column('modalidade', db.String())

    def __init__(self, ticker=None, fator=None, data=None, modalidade=None):
        self.ticker = ticker
        self.fator = fator
        self.data = data
        self.modalidade = modalidade