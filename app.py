from flask import Flask, render_template, request, session, send_file
import os
import re
from werkzeug.utils import secure_filename
from openai import OpenAI
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import io
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Inicializando Flask
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.secret_key = "super_secret_key"

# Criando diretório de uploads
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

import os
from dotenv import load_dotenv

# carrega o arquivo .env
load_dotenv()

# pega a chave de ambiente
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print("Minha chave está funcionando?", bool(OPENAI_API_KEY))


# --- Funções ---
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-ZÀ-ÿ0-9\s]", "", text)
    return text

def classify_email(content):
    prompt = f"""
    Você é um classificador de emails. Categorize o seguinte email em uma das opções:
    - Produtivo: Requer ação ou resposta específica.
    - Improdutivo: Não requer ação imediata.

    Email: {content}
    Responda apenas com 'Produtivo' ou 'Improdutivo'.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=10,
    )
    return response.choices[0].message.content.strip()

def suggest_response(category, content):
    if category == "Produtivo":
        prompt = f"O seguinte email requer ação: '{content[:400]}'. Sugira uma resposta formal e curta para esse email."
    else:
        prompt = f"O seguinte email é apenas cordialidade: '{content[:400]}'. Sugira uma resposta educada e curta para esse email."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=120,
    )
    return response.choices[0].message.content.strip()

# --- Rotas ---
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        content = ""
        if "email_text" in request.form and request.form["email_text"].strip():
            content = request.form["email_text"]
        elif "email_file" in request.files:
            file = request.files["email_file"]
            if file and file.filename != "":
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                file.save(filepath)
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

        if content:
            category = classify_email(content)
            response = suggest_response(category, content)
            result = {"content": content[:200] + "...", "category": category, "response": response}

            # Histórico
            if "history" not in session:
                session["history"] = []
            session["history"].insert(0, result)
            session["history"] = session["history"][:5]

    history = session.get("history", [])
    return render_template("index.html", result=result, history=history)

@app.route("/export_pdf")
def export_pdf():
    history = session.get("history", [])
    if not history:
        return "Nenhum histórico para exportar."

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("📧 Histórico de Emails Classificados", styles["Title"]))
    story.append(Spacer(1, 20))

    for i, item in enumerate(history, 1):
        story.append(Paragraph(f"<b>Email {i}:</b> {item['content']}", styles["Normal"]))
        story.append(Paragraph(f"<b>Categoria:</b> {item['category']}", styles["Normal"]))
        story.append(Paragraph(f"<b>Resposta sugerida:</b> {item['response']}", styles["Normal"]))
        story.append(Spacer(1, 15))

    doc.build(story)
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="historico_emails.pdf", mimetype="application/pdf")

@app.route("/clear_history")
def clear_history():
    session.pop("history", None)
    return "<script>window.location.href='/'</script>"

# --- Rodar aplicação ---
if __name__ == "__main__":
    app.run(debug=True)
