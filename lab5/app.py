from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

# модель для работы с пользователем
class User(UserMixin):
    def __init__(self, id, email, password, name):
        self.id = id
        self.email = email
        self.password = password
        self.name = name

# менеджер для работы с авторизацией
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# база данных пользователей
users_db = {}

# функция для поиска пользователя по id
@login_manager.user_loader
def load_user(user_id):
    user_data = users_db.get(user_id)
    if user_data:
        return User(id=user_data['id'], 
                   email=user_data['email'], 
                   password=user_data['password'], 
                   name=user_data['name'])
    return None

# эндпоинт для главной страницы
@app.route('/')
def index():
    # пользователь не авторизован - открывается страница входа
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    
    # пользователь авторизован - открывается главная страница
    return render_template('index.html')

# эндпоинт для страницы входа
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

# эндпоинт для авторизации
@app.route('/login', methods=['POST'])
def login_post():
    # получаем данные из формы входа
    email = request.form.get('email')
    password = request.form.get('password')
    
    # ищем пользователя по email в базе данных
    user_found = None
    for user_id, user_data in users_db.items():
        if user_data['email'] == email:
            user_found = user_data
            break
    
    # проверяем существование пользователя
    if not user_found:
        flash('Пользователь с таким email не найден')
        return redirect(url_for('login'))
    
    # проверяем правильность ввода пароля
    if user_found['password'] != password:
        flash('Неверный пароль')
        return redirect(url_for('login'))
    
    # создаем объект пользователя и выполняем вход
    user_obj = User(id=user_found['id'], 
                   email=user_found['email'], 
                   password=user_found['password'], 
                   name=user_found['name'])
    login_user(user_obj)
    return redirect(url_for('index'))

# эндпоинт для страницы регистрации
@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

# эндпоинт для регистрации 
@app.route('/signup', methods=['POST'])
def signup_post():
    # получаем данные из формы регистрации
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    # проверяем, есть ли пользователь с таким email
    for user_id, user_data in users_db.items():
        if user_data['email'] == email:
            flash('Пользователь с таким email уже существует')
            return redirect(url_for('signup'))

    # создаем нового пользователя
    user_id = str(len(users_db) + 1)  # генерируем новый id
    new_user = {
        'id': user_id,
        'name': name,
        'email': email,
        'password': password
    }
    users_db[user_id] = new_user  # сохраняем пользователя в базу

    flash('Регистрация прошла успешно! Теперь вы можете войти')
    return redirect(url_for('login'))

# эндпоинт для выхода
@app.route('/logout')
@login_required  # доступно только авторизованным пользователям
def logout():
    # завершаем сеанс пользователя
    logout_user()
    return redirect(url_for('login'))