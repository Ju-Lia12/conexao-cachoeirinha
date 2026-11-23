
from google.cloud import firestore
from google.oauth2 import service_account

cred = service_account.Credentials.from_service_account_file("conexao-cachoeirinha-1f599-f0ff91f7e49b.json")


# Cria cliente Firestore
db = firestore.Client(project="conexao-cachoeirinha-1f599", credentials=cred)  # usa autenticação nativa automaticamente

usuarios_ref = db.collection("formularios")
docs = usuarios_ref.stream()

resultado = []
for doc in docs:    
    resultado.append(doc.to_dict())

# print(resultado)

from email_template import gerar_email_template
from enviar_email import enviar_email

html = gerar_email_template(resultado)
enviar_email(html)



