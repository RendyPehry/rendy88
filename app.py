from flask import Flask, render_template  # Import modul Flask dan render_template

app = Flask(__name__)  # Membuat instance Flask

# Route untuk halaman utama
@app.route('/')
def home():
    return render_template('index.html')  # Render template index.html

# Route untuk halaman about
@app.route('/about')
def about():
    return render_template('about.html')  # Render template about.html

# Route untuk halaman projects
@app.route('/projects')
def projects():
    return render_template('projects.html')  # Render template projects.html

# Route untuk halaman contact
@app.route('/contact')
def contact():
    return render_template('contact.html')  # Render template contact.html

# Menjalankan aplikasi jika file di-execute langsung
if __name__ == '__main__':
    app.run(debug=True)  # Mode debug untuk development