from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import boto3
import uuid
from werkzeug.utils import secure_filename
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

app = Flask(__name__)
app.secret_key = 'virtual-career-2026-super-secret'

# AWS Configuration 
REGION = 'us-east-1' 

dynamodb = boto3.resource('dynamodb', region_name=REGION)
sns = boto3.client('sns', region_name=REGION)

# DynamoDB Tables (Create these tables in DynamoDB manually)
users_table = dynamodb.Table('Users')
admin_users_table = dynamodb.Table('AdminUsers')
career_profiles_table = dynamodb.Table('CareerProfiles')  # For AWS data

# SNS Topic ARN (Replace with your actual SNS Topic ARN)
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:604665149129:aws_capstone_topic' 

# Configuration for File Uploads
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def send_notification(subject, message):
    try:
        sns.publish(TopicArn=SNS_TOPIC_ARN, Subject=subject, Message=message)
    except ClientError as e:
        print(f"Error sending notification: {e}")

def is_logged_in():
    return 'username' in session

@app.route('/')
def index():
    if is_logged_in():
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        
        response = users_table.get_item(Key={'username': username})
        
        if 'Item' in response and response['Item']['password'] == password:
            session['username'] = username
            send_notification("User Login", f"User {username} has logged into Neural Career Matrix.")
            return redirect(url_for('dashboard'))
        
        flash('Invalid credentials! Username: virtual career, Password: counselor')
        return render_template('login.html', error=True)
    
    return render_template('login.html', error=False)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        response = users_table.get_item(Key={'username': username})
        if 'Item' in response:
            flash('User already exists!')
            return render_template('signup.html')
        
        users_table.put_item(Item={'username': username, 'password': password})
        send_notification("New User Signup", f"User {username} has signed up for Neural Career Matrix.")
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    if not is_logged_in():
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])

@app.route('/aws_register', methods=['GET', 'POST'])
def aws_register():
    if not is_logged_in():
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        username = session['username']
        aws_data = {
            'username': username,
            'name': request.form['name'],
            'email': request.form['email'],
            'cert': request.form['cert'],
            'experience': request.form['experience']
        }
        
        career_profiles_table.put_item(Item=aws_data)
        send_notification("AWS Profile Created", f"User {username} completed AWS profile: {request.form['cert']}")
        flash('AWS Profile Saved Successfully!')
        return redirect(url_for('counsel'))
    
    return render_template('aws_register.html')

@app.route('/counsel')
def counsel():
    if not is_logged_in():
        return redirect(url_for('login'))
    
    username = session['username']
    response = career_profiles_table.get_item(Key={'username': username})
    aws_data = response.get('Item', {}) if 'Item' in response else {}
    
    return render_template('counsel.html', aws_data=aws_data)

@app.route('/career_path')
def career_path():
    if not is_logged_in():
        return redirect(url_for('login'))
    
    paths = [
        {'role': 'Cloud Architect', 'match': '94%', 'salary': '₹45LPA'},
        {'role': 'DevOps Engineer', 'match': '88%', 'salary': '₹32LPA'},
        {'role': 'Solutions Architect', 'match': '91%', 'salary': '₹52LPA'}
    ]
    return render_template('career_path.html', paths=paths)

@app.route('/job_market')
def job_market():
    if not is_logged_in():
        return redirect(url_for('login'))
    return render_template('job_market.html')

@app.route('/recommendations')
def recommendations():
    if not is_logged_in():
        return redirect(url_for('login'))
    return render_template('recommendations.html')

@app.route('/logout')
def logout():
    username = session.pop('username', None)
    if username:
        send_notification("User Logout", f"User {username} logged out from Neural Career Matrix.")
    return redirect(url_for('index'))

# Admin Routes (keeping your AWS integration)
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        response = admin_users_table.get_item(Key={'username': username})
        if 'Item' in response and response['Item']['password'] == password:
            session['admin'] = username
            return redirect(url_for('admin_dashboard'))
        flash('Invalid admin credentials!')
    
    return render_template('admin_login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    if 'admin' not in session:
        return redirect(url_for('admin_login'))
    
    users = users_table.scan().get('Items', [])
    profiles = career_profiles_table.scan().get('Items', [])
    
    return render_template('admin_dashboard.html', 
                         admin_username=session['admin'], 
                         users=users, 
                         profiles=profiles)

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
