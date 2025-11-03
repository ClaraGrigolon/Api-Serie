# Importa o objeto `db` que representa a conexão com o banco de dados
from db import db

# Define a classe Funcionario como um modelo de dados do SQLAlchemy
class Serie(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'series'

    # Define a estrutura da tabela com suas colunas
    id = db.Column(db.Integer, primary_key=True)  # Coluna ID, chave primária
    titulo = db.Column(db.String(100), nullable=False)
    elenco = db.Column(db.String(200), nullable=False)
    lancamento = db.Column(db.String(8), nullable=False)
    genero = db.Column(db.String(100), nullable=False)

    # Método para converter o objeto em um formato JSON
    def json(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'elenco': self.elenco,
            'lancamento': self.lancamento,
            'genero': self.genero
        }
