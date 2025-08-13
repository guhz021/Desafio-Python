<h1 align="center">Desafio Python</h1>

## <div align="center">PASSOS DE SETUP</div>

 
|📄 **Descrição**|
|-|
 |1- Instalar python na máquina
2- Criar o ambiente virtual com o comando: python -m venv venv
3- Instalar bibliotecas com comando: pip install supabase python-dotenv requests
4-Crie a tabela "contatos" no Supabase na seguinte ordem: 
CREATE TABLE contatos (
  id SERIAL PRIMARY KEY,
  nome TEXT,
  telefone TEXT NOT NULL
);
INSERT INTO contatos (nome, telefone) VALUES
  ('João Silva', '5511999999999'),
  ('Maria Souza', '5511888888888');
4-Execute o projeto com o comando: python main.py|


