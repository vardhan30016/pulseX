# 🫀 PulseX — Circulatory System Learning & Simulation Platform

**PulseX** is a premium, high-fidelity interactive educational web platform built on Django. It connects anatomical and biological knowledge of the human circulatory system with real-time physiological simulations, interactive quizzes, dynamic profile dashboards, and custom certification generators.

---

## 🌟 Key Features

1. **🏠 Interactive Home Dashboard**
   - Sleek dark navy interface featuring a live, glowing vector ECG heartbeat animation.
   - Six interactive module gateways leading to distinct features.

2. **📚 Interactive Circulatory Lessons (`/learn/`)**
   - High-contrast structured lessons with custom medical illustrations detailing Systemic/Pulmonary pathways, heart anatomy, and the vascular network.

3. **🧪 Physiological Flow Simulator (`/simulation/`)**
   - Interactive SVG canvas tracing oxygenated (red) and deoxygenated (blue) blood paths.
   - Start, pause, and reset controls with animated flowing blood cells and dynamic speed adjustments.

4. **🩸 Hematology Explorer (`/blood/`)**
   - Visual cards detailing Red Blood Cells, White Blood Cells, Platelets, and Plasma.
   - Interactive blood composition pie chart analyzer.

5. **💔 Cardiovascular Pathologies Library (`/diseases/`)**
   - Detailed profiles on Heart Attacks, Hypertension, Strokes, and Anemia.
   - Auto-mapped warning illustrations and support for admin-uploaded custom files.

6. **📝 Interactive Quiz & Badges (`/quiz/`)**
   - Real-time graded questions with instant results and automatic database tracking.
   - Dynamic performance rewards: **Excellent** (Gold Star), **Good** (Silver Medal), or **Try Again** (Red Retry Badge) based on score.

7. **🎓 Completion Certificate (`/certificate/`)**
   - Generates an official, printable completion credential with gold borders, awarding stamps, and authorized signature lines.

8. **👤 User Profile & Bio (`/dashboard/`)**
   - User profile metrics dashboard.
   - Dynamic profile uploader allowing customizable bios and profile photos.

---

## 🛠️ Technology Stack
* **Backend:** Django 6.0.6 (Python)
* **Frontend:** HTML5, CSS3, Javascript, SVG Vector Animations
* **CSS Framework:** Bootstrap 5
* **Image Processing:** Pillow (Python Image Library)

---

## 🚀 How to Run the Project

Follow these simple steps to set up and run the application locally on any machine:

### Prerequisite: Python
Make sure you have **Python 3.10 or higher** installed on your system.

### Step 1: Extract the Zip File
Unzip the folder containing the project files. (Ensure you do **not** run commands inside the zip preview, extract it first).

### Step 2: Create a Virtual Environment
Open a terminal (Command Prompt, PowerShell, or bash) in the extracted folder root directory (where `requirements.txt` is located) and run:
```bash
# Windows
python -m venv .venv

# macOS / Linux
python3 -m venv .venv
```

### Step 3: Activate the Virtual Environment
Activate the virtual environment to isolate the project dependencies:
```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Command Prompt)
.venv\Scripts\activate.bat

# macOS / Linux (Terminal)
source .venv/bin/activate
```

### Step 4: Install Dependencies
Install all the required python packages:
```bash
pip install -r requirements.txt
```

### Step 5: Run Database Migrations
Set up the SQLite database schemas and seeds:
```bash
python pulsex/manage.py migrate
```

### Step 6: Start the Server
Launch the Django local development server:
```bash
python pulsex/manage.py runserver
```

### Step 7: Open the Application
Open your browser and navigate to:
```text
http://127.0.0.1:8000/
```

---

## 📦 How to create a ZIP to share with friends

When zipping the project, **exclude the `.venv` folder**! The `.venv` folder is very large (hundreds of megabytes) and contains environment-specific compiled binaries that will not work on your friends' systems. Your friends will create their own virtual environment using `requirements.txt`.

### Recommended files to include in the ZIP:
```text
Heart Sync/
├── pulsex/              # The Django project code
├── pyrightconfig.json   # IDE configurations
├── README.md            # This documentation
└── requirements.txt     # Dependencies list
```
*(Exclude `.venv/` and any `__pycache__/` folders if present to keep the size under 15MB).*
