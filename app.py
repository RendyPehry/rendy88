from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    testimonials = [
        {"name": "Regina", "text": "Desainnya keren dan cepat selesai!"},
        {"name": "Rendy", "text": "Fast track sangat membantu deadline saya."},
        {"name": "Raymond", "text": "Rekomendasi banget, komunikatif dan hasilnya bagus."}
    ]
    portfolio = [
        {"img": "image.png", "desc": "Poster Event"},
        {"img": "image.png", "desc": "Feed Instagram"},
        {"img": "image.png", "desc": "Flyer Produk"}
    ]
    return render_template('index.html', testimonials=testimonials, portfolio=portfolio)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    service_type = request.form['service']
    description = request.form['description']
    print(f"Order dari {name} ({email}) - {service_type}: {description}")
    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
