                                                The Virtual Career Counselor: Harnessing Generative AI and AWS for Personalized Pathways
1.🏠 Home / Index Page

Dark AI-themed neon gradient background

Title: 🤖 Neural Career Matrix

Main buttons:
🔐 Neural Login
☁️ AWS Register
👉 Gives a futuristic AI application feel at first glance.

2.🔐 Login Page

Glassmorphism-style login card
Neon gradient heading
Demo login credentials:
Username: virtual career
Password: counselor
On successful login → Dashboard page

3.📊 Dashboard

Welcome message for the user

Information cards:
🎯 Top Career Match: Cloud Architect
📈 Career Progress: 72%
🎓 Next Skill: AWS Certification

Navigation buttons:
ℹ️ About Us
🚪 Logout

4.ℹ️ About Page

Full-screen animated hero section
Glowing text and smooth transitions

Content sections:
🌌 Innovation
⚡ Technology Stack
🚀 Platform Features
🎯 Future Vision

5.☁️ AWS Registration Page

User input form fields:
Name
Email
AWS Certification
Years of Experience
After submitting → Redirects to Counsel Page

6.🧠 Counsel Page

Displays the registered AWS profile details

Action buttons:
📈 Career Paths
📊 Job Market Trends
🎯 Skill & Course Recommendations

7.📊 Job Market Trends Page

Card-based layout

Shows:
Skills
Industry demand percentage
“Apply Now” buttons

8.🎯 Recommendations Page

Suggested courses and certifications

Information displayed:
Course name
Duration
Cost
Learning platform
“Enroll Now” button for each course

9.Neural Career Matrix(app.py)
🏠 HOME (/)
 ├── 🔐 Login
 └── ☁️ AWS Register
🔐 LOGIN
 └── ✅ Success
       ↓
📊 DASHBOARD
 ├── ☁️ AWS Registration
 ├── 🧠 Career Counseling
 ├── 📈 Career Paths
 ├── 📊 Job Market
 ├── 🎯 Recommendations
 └── 🚪 Logout
 ☁️ AWS REGISTER
 └── Save Profile
       ↓
🧠 COUNSEL PAGE
 ├── 📈 Career Paths
 ├── 📊 Job Market
 ├── 🎯 Recommendations
 └── 🏠 Dashboard
📈 Career Paths   📊 Job Market   🎯 Recommendations
   (Roles)           (Trends)         (Courses)
🚪 LOGOUT → 🏠 HOME

10.Project Flow
🏠 HOME
   |
   v
🔐 LOGIN / SIGNUP
   |
   v
📊 DASHBOARD
   |
   +--> ☁️ AWS REGISTER
   |        |
   |        v
   |     🧠 COUNSEL
   |
   +--> 📈 CAREER PATH
   |
   +--> 📊 JOB MARKET
   |
   +--> 🎯 RECOMMENDATIONS
   |
   v
🚪 LOGOUT

Data Flow

USER DATA
   |
   v
🗄️ DynamoDB
 (Users / CareerProfiles)
   |
   v
📄 Display in Pages

LOGIN / SIGNUP / LOGOUT
   |
   v
📢 SNS NOTIFICATION


Admin login Flow
🔐 ADMIN LOGIN
      |
      v
📊 ADMIN DASHBOARD
 ├── View Users
 └── View AWS Profiles

