from datetime import datetime

from flask import Flask, request, render_template, session, redirect, url_for, jsonify
from flask_session import Session

from secret import SECRET, ADMIN_PASSWORD, FLAG

app = Flask(__name__)

# Configure the secret key for session management. Change it to your own secret key.
app.config['SECRET_KEY'] = SECRET

# Configure the session type as 'filesystem'
app.config['SESSION_TYPE'] = 'filesystem'

# Initialize the Flask-Session extension
Session(app)

# In-memory database (dictionary) to store user data
class Database(dict):
    def __init__(self, *args, **kwargs):
        super(Database, self).__init__(*args, **kwargs)

database = Database({
    'users': [
        {
            'username': 'admin',
            'password': ADMIN_PASSWORD,
            'is_admin': True
        }
    ],
    'mergelogs': [

    ]
})

def log_merge_time(*args, donext=None):
    database['mergelogs'].append({
        'time': str(datetime.now()),
        'log': " - ".join(args)
    })
    if donext != None:
        exec(donext)

def merge(new_data, old_data):
    t = type(new_data)
   
    if t in [list, tuple]:
        if len(new_data) != len(old_data):
            raise Exception("lists aren't the same size!")

        for i, val in enumerate(new_data):
            if type(new_data[i]) in [list, dict, tuple]:
                merge(val, old_data[i])
            else:
                old_data[i] = val
    elif t == dict:
        for i in new_data:
            val = new_data[i]
            if type(val) in [list, dict]:
                if hasattr(old_data, i):
                    merge(val, getattr(old_data, i))
                else:
                    merge(val, old_data[i])
            else:
                old_data[i] = val
    else:
        raise Exception("can't merge this type!")



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/v0.1', methods=['POST'])
def api_v01():
    if request.is_json:
        try:
            data = request.get_json()

            merge(data, database)

            log_merge_time()

            return jsonify({"message": "Data merged successfully."})
        except Exception as e:
            return jsonify({"error": "Error merging data: {}".format(str(e))}), 400
    else:
        return jsonify({"error": "Request must contain JSON data"}), 400

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users = database['users']
        if username in [i['username'] for i in users]:
            return "Username already exists"
        users.append({
            'username': username,
            'password': password,
            'is_admin': False
        })
        return "User registered successfully"
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users = database['users']
        users_found = list(filter(lambda x: x['username'] == username, users))
        if len(users_found) == 1 and users_found[0]['password'] == password:
            session['username'] = username
            return redirect(url_for('profile'))
        else:
            return "Invalid username or password"
    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/profile', methods=['GET'])
def profile():
    username = session.get('username')
    return render_template('profile.html', username=username)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
