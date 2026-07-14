from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# 1. YE NAYA FUNCTION SABSE UPAR RAKHO
def get_answer(question):
    question = question.lower()
    
    if 'fees' in question:
        return "Fees ki last date 30 April 2026 hai."
    elif 'attendance' in question:
        return "Aapki attendance 86% hai."
    elif 'exam' in question:
        return "Exam 15 May se hai."
    elif 'hello' in question:
        return "Hello! Mai aapka Student AI Chatbot hu."
    elif 'result' in question:
        return "Result 20 June 2026 ko aayega."
    else:
        return "Sorry, mujhe is sawal ka jawab nahi pata."


# 2. YE SAB ROUTE NEECHE RAHE
@app.route('/')
def home():
    return redirect(url_for('register'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template('chat.html', question="", answer="")
    return render_template('login.html')


# 3. CHAT WALA ROUTE - YAHI PE FUNCTION CALL HOGA
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        question = request.form['question']
        answer = get_answer(question) # yaha function call ho raha hai
    else:
        question = ""
        answer = ""
    
    return render_template('chat.html', question=question, answer=answer)


if __name__ == '__main__':
    app.run(debug=True)