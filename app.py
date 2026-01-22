from flask import Flask, render_template_string, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'virtual-career-2026-super-secret'

users = {'virtual career': 'counselor'}
user_data = {}

def is_logged_in():
    return 'username' in session

# 1. INDEX PAGE
@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html><head><title>Neural Career Matrix</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:Arial;background:linear-gradient(135deg,#0a0a1e,#1a1a3e);color:white;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:20px}.container{background:rgba(255,255,255,0.1);padding:60px;border-radius:25px;backdrop-filter:blur(20px);max-width:500px;width:100%;text-align:center;border:1px solid rgba(0,255,204,0.3)}h1{font-size:3rem;background:linear-gradient(45deg,#00ffcc,#ff6bcb);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:20px}p{font-size:1.3rem;margin:30px 0}.btn{display:inline-block;background:linear-gradient(45deg,#00ffcc,#ff6bcb);color:#000;padding:18px 40px;text-decoration:none;border-radius:15px;font-weight:bold;margin:15px;font-size:1.2rem;transition:all .3s}.btn:hover{transform:translateY(-5px);box-shadow:0 15px 30px rgba(0,255,204,.5)}</style></head>
<body><div class="container">
<h1>🤖 Neural Career Matrix</h1>
<p>2026 AI Career Revolution</p>
<a href="/login" class="btn">🔐 Neural Login</a>
<a href="/aws_register" class="btn">☁️ AWS Register</a>
</div></body></html>
    ''')

# 2. LOGIN PAGE
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        if username == 'virtual career' and password == 'counselor':
            session['username'] = username
            return redirect(url_for('dashboard'))
        return render_template_string(LOGIN_TEMPLATE, error=True)
    return render_template_string(LOGIN_TEMPLATE, error=False)

LOGIN_TEMPLATE = '''
<!DOCTYPE html>
<html><head><title>Login</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:Arial;background:linear-gradient(135deg,#0a0a1e,#1a1a3e);color:white;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:20px}.container{background:rgba(255,255,255,0.1);padding:50px 40px;border-radius:25px;backdrop-filter:blur(20px);max-width:400px;width:100%;text-align:center;border:1px solid rgba(0,255,204,0.3)}.h1{font-size:2.5rem;background:linear-gradient(45deg,#00ffcc,#ff6bcb);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:20px}.credentials{background:rgba(0,255,204,0.2);padding:20px;border-radius:15px;margin:25px 0;border-left:4px solid #00ffcc}.credentials strong{color:#00ffcc}input{width:100%;padding:18px;margin:12px 0;border:none;border-radius:12px;background:rgba(255,255,255,0.2);color:white;font-size:16px}input::placeholder{color:rgba(255,255,255,0.7)}button{width:100%;background:linear-gradient(45deg,#00ffcc,#ff6bcb);color:#000;padding:20px;border:none;border-radius:15px;font-size:18px;font-weight:bold;cursor:pointer;margin-top:20px}.button:hover{transform:translateY(-2px);box-shadow:0 10px 25px rgba(0,255,204,0.4)}.error{background:rgba(255,0,0,0.2);color:#ff6b6b;padding:15px;border-radius:10px;margin:15px 0}a{color:#00ffcc;text-decoration:none;font-weight:bold}a:hover{color:#ff6bcb}</style></head>
<body><div class="container">
<h1 class="h1">🔐 Neural Login</h1>
{% if error %}
<div class="error">❌ Wrong credentials!<br><small>Username: virtual career<br>Password: counselor</small></div>
{% endif %}
<div class="credentials">
<strong>Username:</strong> virtual career<br>
<strong>Password:</strong> counselor
</div>
<form method="POST">
<input name="username" placeholder="Username" required>
<input name="password" type="password" placeholder="Password" required>
<button>🚀 Access Dashboard</button>
</form>
<p style="margin-top:25px"><a href="/">← Home</a></p>
</div></body></html>
'''

# 3. DASHBOARD WITH ALL LINKS!
@app.route('/dashboard')
def dashboard():
    if not is_logged_in():
        return redirect(url_for('login'))
    return render_template_string(DASHBOARD_TEMPLATE, username=session['username'])

DASHBOARD_TEMPLATE = '''
<!DOCTYPE html>
<html><head><title>Dashboard</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:Arial;background:linear-gradient(135deg,#0a0a1e,#1a1a3e);color:white;min-height:100vh;padding:50px 20px}.container{max-width:1200px;margin:0 auto;background:rgba(255,255,255,0.1);padding:50px;border-radius:25px;backdrop-filter:blur(20px);text-align:center}h1{font-size:3rem;background:linear-gradient(45deg,#00ffcc,#ff6bcb);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:20px}h2{font-size:1.8rem;margin:40px 0 20px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:25px;margin:40px 0}.card{background:rgba(255,255,255,0.15);padding:30px;border-radius:20px;border-left:5px solid #00ffcc;transition:all .3s;cursor:pointer}.card:hover{transform:translateY(-10px);box-shadow:0 20px 40px rgba(0,255,204,.3)}.card.purple{border-left-color:#ff6bcb}.card.blue{border-left-color:#00d4ff}.card h3{font-size:1.4rem;color:#00ffcc;margin-bottom:15px}.btn-group{display:flex;flex-wrap:wrap;gap:15px;justify-content:center;margin-top:40px}.btn{background:linear-gradient(45deg,#00ffcc,#ff6bcb);color:#000;padding:15px 30px;text-decoration:none;border-radius:15px;font-weight:bold;font-size:1.1rem;transition:all .3s}.btn:hover{transform:translateY(-3px);box-shadow:0 15px 30px rgba(0,255,204,.5)}.logout{background:linear-gradient(45deg,#ff6bcb,#ff0080)}@media(max-width:768px){.container{padding:30px 20px}}</style></head>
<body>
<div class="container">
<h1>🧠 Neural Dashboard</h1>
<h2>Welcome, {{ username }}!</h2>
<div class="grid">
<div class="card">
<h3>☁️ AWS Registration</h3>
<p>Complete your AWS certification profile</p>
<a href="/aws_register" class="btn" style="margin-top:15px;display:inline-block">Register Now</a>
</div>
<div class="card purple">
<h3>🧠 Career Counseling</h3>
<p>Get personalized career guidance</p>
<a href="/counsel" class="btn" style="margin-top:15px;display:inline-block">Start Counseling</a>
</div>
<div class="card blue">
<h3>📈 Career Paths</h3>
<p>View your top career matches</p>
<a href="/career_path" class="btn" style="margin-top:15px;display:inline-block">View Paths</a>
</div>
</div>
<div class="grid">
<div class="card">
<h3>📊 Job Market</h3>
<p>2026 job market trends analysis</p>
<a href="/job_market" class="btn" style="margin-top:15px;display:inline-block">View Trends</a>
</div>
<div class="card purple">
<h3>🎯 Recommendations</h3>
<p>Personalized learning paths</p>
<a href="/recommendations" class="btn" style="margin-top:15px;display:inline-block">Get Recs</a>
</div>
<div class="card blue">
<h3>🚪 Logout</h3>
<p>End session</p>
<a href="/logout" class="btn logout" style="margin-top:15px;display:inline-block">Logout</a>
</div>
</div>
</div>
</body></html>
'''

# 4. AWS REGISTER
@app.route('/aws_register', methods=['GET', 'POST'])
def aws_register():
    if not is_logged_in():
        return redirect(url_for('login'))
    if request.method == 'POST':
        session['aws_data'] = {
            'name': request.form['name'],
            'email': request.form['email'],
            'cert': request.form['cert'],
            'experience': request.form['experience']
        }
        flash('AWS Profile Saved!')
        return redirect(url_for('counsel'))
    return render_template_string(AWS_REGISTER_TEMPLATE)

AWS_REGISTER_TEMPLATE = '''
<!DOCTYPE html>
<html><head><title>AWS Register</title>
<style>*{margin:0;padding:0}body{font-family:Arial;background:linear-gradient(135deg,#0a0a1e,#1a1a3e);color:white;min-height:100vh;padding:50px 20px;display:flex;align-items:center;justify-content:center}.container{background:rgba(255,255,255,0.1);padding:50px;border-radius:25px;backdrop-filter:blur(20px);max-width:500px;width:100%;text-align:center;border:1px solid rgba(0,255,204,0.3)}h1{font-size:2.5rem;background:linear-gradient(45deg,#00ffcc,#ff6bcb);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:30px}input,select,textarea{width:100%;padding:15px;margin:10px 0;border:none;border-radius:10px;background:rgba(255,255,255,0.2);color:white;font-size:16px}textarea{resize:vertical;height:100px}button{width:100%;background:linear-gradient(45deg,#00ffcc,#ff6bcb);color:#000;padding:20px;border:none;border-radius:15px;font-size:18px;font-weight:bold;cursor:pointer;margin-top:20px}.btn-group{display:flex;gap:15px;justify-content:center;margin-top:20px}.btn{background:linear-gradient(45deg,#00ffcc,#ff6bcb);color:#000;padding:12px 24px;text-decoration:none;border-radius:10px;font-weight:bold;flex:1}a.btn:hover,button:hover{transform:translateY(-2px)}</style></head>
<body><div class="container">
<h1>☁️ AWS Profile Registration</h1>
<form method="POST">
<input name="name" placeholder="Full Name" required>
<input name="email" type="email" placeholder="Email" required>
<select name="cert" required><option value="">AWS Certification</option><option>AWS Solutions Architect</option><option>AWS Developer</option><option>AWS SysOps</option><option>AWS DevOps</option><option>None</option></select>
<textarea name="experience" placeholder="AWS Experience/Projects" required></textarea>
<button type="submit">🚀 Save AWS Profile</button>
</form>
<div class="btn-group">
<a href="/counsel" class="btn">➡️ Continue to Counsel</a>
<a href="/dashboard" class="btn">🏠 Dashboard</a>
</div>
</div></body></html>
'''

# 5. COUNSEL PAGE
@app.route('/counsel')
def counsel():
    if not is_logged_in():
        return redirect(url_for('login'))
    aws_data = session.get('aws_data', {})
    return render_template_string(COUNSEL_TEMPLATE, aws_data=aws_data)

COUNSEL_TEMPLATE = '''
<!DOCTYPE html>
<html><head><title>Counsel</title>
<style>*{margin:0;padding:0}body{font-family:Arial;background:linear-gradient(135deg,#0a0a1e,#1a1a3e);color:white;padding:50px 20px}.container{max-width:900px;margin:0 auto;background:rgba(255,255,255,0.1);padding:40px;border-radius:25px;backdrop-filter:blur(20px)}h1{font-size:2.8rem;background:linear-gradient(45deg,#00ffcc,#ff6bcb);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-align:center;margin-bottom:30px}.profile-card{background:rgba(0,255,204,0.2);padding:25px;border-radius:15px;margin:20px 0;border-left:5px solid #00ffcc}.btn-group{display:flex;gap:15px;justify-content:center;flex-wrap:wrap;margin-top:30px}.btn{background:linear-gradient(45deg,#00ffcc,#ff6bcb);color:#000;padding:15px 30px;text-decoration:none;border-radius:12px;font-weight:bold}.btn:hover{transform:translateY(-2px)}</style></head>
<body><div class="container">
<h1>🧠 Career Counseling</h1>
<div class="profile-card">
<h3>📊 Your AWS Profile</h3>
{% if aws_data %}
<p><strong>Name:</strong> {{ aws_data.name }}</p>
<p><strong>Certification:</strong> {{ aws_data.cert }}</p>
<p><strong>Experience:</strong> {{ aws_data.experience }}</p>
{% else %}
<p>No AWS profile. <a href="/aws_register" style="color:#00ffcc">Complete registration</a></p>
{% endif %}
</div>
<div class="btn-group">
<a href="/career_path" class="btn">📈 Career Paths</a>
<a href="/job_market" class="btn">📊 Job Market</a>
<a href="/recommendations" class="btn">🎯 Recommendations</a>
<a href="/dashboard" class="btn">🏠 Dashboard</a>
</div>
</div></body></html>
'''

# 6. CAREER PATH
@app.route('/career_path')
def career_path():
    if not is_logged_in():
        return redirect(url_for('login'))
    paths = [
        {'role': 'Cloud Architect', 'match': '94%', 'salary': '₹45LPA'},
        {'role': 'DevOps Engineer', 'match': '88%', 'salary': '₹32LPA'},
        {'role': 'Solutions Architect', 'match': '91%', 'salary': '₹52LPA'}
    ]
    return render_template_string(CAREER_PATH_TEMPLATE, paths=paths)

CAREER_PATH_TEMPLATE = '''
<!DOCTYPE html>
<html><head><title>Career Path</title>
<style>*{margin:0;padding:0}body{font-family:Arial;background:linear-gradient(135deg,#0a0a1e,#1a1a3e);color:white;padding:50px 20px}.container{max-width:1200px;margin:0 auto}h1{font-size:3rem;background:linear-gradient(45deg,#00ffcc,#ff6bcb);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-align:center;margin-bottom:40px}.paths{display:grid;grid-template-columns:repeat(auto-fit,minmax(350px,1fr));gap:25px}.path-card{background:rgba(255,255,255,0.1);padding:30px;border-radius:20px;backdrop-filter:blur(15px);border-top:4px solid #00ffcc;transition:transform 0.3s}.path-card:hover{transform:translateY(-10px)}.match{font-size:2.5rem;font-weight:bold;background:linear-gradient(45deg,#00ffcc,#ff6bcb);-webkit-background-clip:text;-webkit-text-fill-color:transparent}.btn-group{text-align:center;margin-top:40px}.btn{background:linear-gradient(45deg,#00ffcc,#ff6bcb);color:#000;padding:15px 40px;text-decoration:none;border-radius:15px;font-weight:bold;font-size:18px;display:inline-block}</style></head>
<body><div class="container">
<h1>📈 Career Pathways ({{ paths|length }} Matches)</h1>
<div class="paths">
{% for path in paths %}
<div class="path-card">
<div class="match">{{ path.match }}</div>
<h3>{{ path.role }}</h3>
<p><strong>Expected Salary:</strong> {{ path.salary }}</p>
</div>
{% endfor %}
</div>
<div class="btn-group"><a href="/counsel" class="btn">← Back to Counsel</a></div>
</div></body></html>
'''

# 7. JOB MARKET
@app.route('/job_market')
def job_market():
    if not is_logged_in():
        return redirect(url_for('login'))
    return render_template_string(JOB_MARKET_TEMPLATE)

JOB_MARKET_TEMPLATE = '''
<!DOCTYPE html>
<html><head><title>Job Market</title>
<style>*{margin:0;padding:0}body{font-family:Arial;background:linear-gradient(135deg,#0a0a1e,#1a1a3e);color:white;padding:50px 20px}.container{max-width:1200px;margin:0 auto}h1{font-size:3rem;background:linear-gradient(45deg,#00ffcc,#ff6bcb);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-align:center;margin-bottom:40px}.trends{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:25px}.trend-card{background:rgba(255,255,255,0.1);padding:30px;border-radius:20px;backdrop-filter:blur(15px);text-align:center}.demand{font-size:3rem;color:#00ffcc;font-weight:bold}.btn-group{text-align:center;margin-top:40px}.btn{background:linear-gradient(45deg,#00ffcc,#ff6bcb);color:#000;padding:15px 40px;text-decoration:none;border-radius:15px;font-weight:bold;font-size:18px;display:inline-block}</style></head>
<body><div class="container">
<h1>📊 2026 Job Market Trends</h1>
<div class="trends">
<div class="trend-card"><div class="demand">120%</div><h3>AWS Certified</h3><p>15K+ Jobs | Bangalore</p></div>
<div class="trend-card"><div class="demand">110%</div><h3>DevOps</h3><p>22K+ Jobs | Chennai</p></div>
<div class="trend-card"><div class="demand">95%</div><h3>Kubernetes</h3><p>8K+ Jobs | Hyderabad</p></div>
</div>
<div class="btn-group"><a href="/counsel" class="btn">← Back to Counsel</a></div>
</div></body></html>
'''

# 8. RECOMMENDATIONS
@app.route('/recommendations')
def recommendations():
    if not is_logged_in():
        return redirect(url_for('login'))
    return render_template_string(RECOMMENDATIONS_TEMPLATE)

RECOMMENDATIONS_TEMPLATE = '''
<!DOCTYPE html>
<html><head><title>Recommendations</title>
<style>*{margin:0;padding:0}body{font-family:Arial;background:linear-gradient(135deg,#0a0a1e,#1a1a3e);color:white;padding:50px 20px}.container{max-width:1200px;margin:0 auto}h1{font-size:3rem;background:linear-gradient(45deg,#00ffcc,#ff6bcb);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-align:center;margin-bottom:40px}.recs{display:grid;grid-template-columns:repeat(auto-fit,minmax(350px,1fr));gap:25px}.rec-card{background:rgba(255,255,255,0.1);padding:30px;border-radius:20px;backdrop-filter:blur(15px);border-left:5px solid #00ffcc}.cost{font-size:2rem;color:#00ffcc;font-weight:bold}.btn-group{text-align:center;margin-top:40px}.btn{background:linear-gradient(45deg,#00ffcc,#ff6bcb);color:#000;padding:15px 40px;text-decoration:none;border-radius:15px;font-weight:bold;font-size:18px;display:inline-block}</style></head>
<body><div class="container">
<h1>🎯 Top Recommendations</h1>
<div class="recs">
<div class="rec-card"><h3>AWS Solutions Architect</h3><p><strong>Duration:</strong> 3 months</p><div class="cost">₹12,000</div><p>Udemy</p></div>
<div class="rec-card"><h3>Docker & Kubernetes</h3><p><strong>Duration:</strong> 2 months</p><div class="cost">₹8,500</div><p>Coursera</p></div>
<div class="rec-card"><h3>Terraform IaC</h3><p><strong>Duration:</strong> 1 month</p><div class="cost">₹5,000</div><p>ACloudGuru</p></div>
</div>
<div class="btn-group"><a href="/counsel" class="btn">← Back to Counsel</a></div>
</div></body></html>
'''

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

