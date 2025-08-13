import os
import requests
from supabase import create_client
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

def get_supabase_contacts(limit=3):
    """Pega os contatos do Supabase e cria o cliente """
    try:
        client = create_client(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_KEY'))
        return client.table('contatos').select('*').limit(limit).execute().data
    except Exception as e:
        logging.error(f"Ocorreu um erro no Supabase: {e}")
        return []

def send_zapi_message(phone, message):
    """Envia a mensagem com o Z-API"""
    phone = f"55{''.join(filter(str.isdigit, phone))}" if not str(phone).startswith('55') else phone
    
    try:
        response = requests.post(
            f"https://api.z-api.io/instances/{os.getenv('ZAPI_INSTANCE')}/token/{os.getenv('ZAPI_TOKEN')}/send-text",
            json={"phone": phone, "message": message},
            headers={
                'Content-Type': 'application/json',
                'Client-Token': os.getenv('ZAPI_CLIENT_TOKEN'),
                'Authorization': f'Bearer {os.getenv('ZAPI_TOKEN')}'
            },
            timeout=30
        )
        if response.status_code == 200:
            logging.info(f"Mensagem para o telefone: {phone} enviada!")
            return True
        logging.error(f"Erro ao enviar mensagem: {response.json().get('error', 'Erro desconhecido')}")
    except Exception as e:
        logging.error(f"Falha no envio da mensagem: {e}")
    return False

def main():
    logging.info("Iniciando envio de mensagens aos telefones do Supabase...")
    contacts = get_supabase_contacts(int(os.getenv('MAX_SEND', 3))) or []
    
    if not contacts:
        logging.error("Nenhum contato foi encontrado!")
        return
    
    success = sum(
        send_zapi_message(c['telefone'], f"Olá {c.get('nome', '')}, tudo bem?")
        for c in contacts if c.get('telefone')
    )
    logging.info(f"Concluído! {success}/{len(contacts)} mensagens enviadas com sucesso.")

if __name__ == "__main__":
    main()