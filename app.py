from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Base de datos de citas (podría moverse a un archivo JSON o base de datos real)
QUOTES = {
    "es": [
        {
            "text": "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor.",
            "author": "Miguel de Cervantes"
        },
        {
            "text": "La vida no es la que uno vivió, sino la que uno recuerda y cómo la recuerda para contarla.",
            "author": "Gabriel García Márquez"
        },
        {
            "text": "El amor es una amistad con momentos eróticos.",
            "author": "Antonio Gala"
        },
        {
            "text": "La música es el arte más directo, entra por el oído y va al corazón.",
            "author": "Magdalena Martínez"
        },
        {
            "text": "La creatividad es la inteligencia divirtiéndose.",
            "author": "Albert Einstein"
        }
    ],
    "en": [
        {
            "text": "To be or not to be, that is the question.",
            "author": "William Shakespeare"
        },
        {
            "text": "It was the best of times, it was the worst of times.",
            "author": "Charles Dickens"
        },
        {
            "text": "The only way to do great work is to love what you do.",
            "author": "Steve Jobs"
        },
        {
            "text": "Life is what happens when you're busy making other plans.",
            "author": "John Lennon"
        },
        {
            "text": "Success is not final, failure is not fatal: it is the courage to continue that counts.",
            "author": "Winston Churchill"
        }
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/quote/<lang>')
def get_quote(lang):
    import random
    
    # Si el idioma no existe, usar inglés por defecto
    if lang not in QUOTES:
        lang = "en"
    
    # Seleccionar una cita aleatoria
    quote = random.choice(QUOTES[lang])
    return jsonify(quote)

@app.route('/api/verify', methods=['POST'])
def verify_text():
    data = request.json
    typed_text = data.get('typed', '')
    original_text = data.get('original', '')
    
    # Verificar la precisión
    min_length = min(len(typed_text), len(original_text))
    correct_chars = sum(1 for i in range(min_length) if typed_text[i] == original_text[i])
    accuracy = (correct_chars / len(original_text)) * 100 if len(original_text) > 0 else 0
    
    return jsonify({
        'accuracy': accuracy,
        'isCorrect': typed_text == original_text
    })

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)