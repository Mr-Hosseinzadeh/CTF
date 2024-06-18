from flask import Flask, request, render_template,render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    template = request.args.get('template')
    if template:
        return render_template_string(template)
    return render_template('index.html', name="Visitor")

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
