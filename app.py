import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, render_template, redirect, request, flash, url_for
from dotenv import load_dotenv
import os
from config import email, senha

load_dotenv()

app = Flask(__name__)
app.secret_key = 'marley'

# Configurações de e-mail
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USER = email
EMAIL_PASSWORD = senha  # Senha de aplicativo (não use a senha da conta!)

class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        mensagem = request.form.get("mensagem")

        if not all([nome, email, mensagem]):
            flash("Preencha todos os campos.", "danger")
            return redirect(url_for("index"))

        # Configura o e-mail a ser enviado
        msg = MIMEMultipart()
        msg["From"] = EMAIL_USER
        msg["To"] = EMAIL_USER  # Altere para destinatários diferentes, se necessário
        msg["Subject"] = f"Contato de {nome}"
        msg["Reply-To"] = email

        body = f"Nome: {nome}\nE-mail: {email}\n\nMensagem:\n{mensagem}"
        msg.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
                server.starttls()
                server.login(EMAIL_USER, EMAIL_PASSWORD)
                server.send_message(msg)
                flash("Mensagem enviada com sucesso!", "success")
        except Exception as e:
            print(f"Erro ao enviar o e-mail: {e}")
            flash("Erro ao enviar a mensagem. Tente novamente mais tarde.", "danger")
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
