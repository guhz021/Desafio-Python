<h1 align="center">Desafio Python</h1>

## <div align="center">PASSOS DE SETUP</div>

 

|📄 **Descrição**|
|-|
 |1- Instalar python na máquina 
2- Criar o ambiente virtual com o comando: python -m venv venv 
3- Instalar bibliotecas com comando: pip install supabase python-dotenv requests 
4- Crie a tabela "contatos" no Supabase na seguinte ordem:
CREATE TABLE contatos (id SERIAL PRIMARY KEY, nome TEXT, telefone TEXT NOT NULL);
INSERT INTO contatos (nome, telefone) VALUES ('João Silva', '5511999999999'), ('Maria Souza', '5511888888888')
5- Crie uma nova instância no Z-API, obtendo assim o ID da instância, token da instância e o Client Token(Este você encontra na aba de "Segurança" e ativando a opção 3. Token de segurança da conta)
6- Coloque os tokens no arquivo .env
*SUPABASE_URL= URL do projeto no Supabase
*SUPABASE_KEY= API KEY do projeto no Supabase
*ZAPI_INSTANCE= ID da instância
*ZAPI_TOKEN= token da instância
*ZAPI_CLIENT_TOKEN= Client Token
7-Execute o projeto com o comando: python main.py|

