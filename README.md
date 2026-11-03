# 🛡️ Security Data Engineering Lab

> A place where I learn to build software that spots danger in data.

## 🤔 What is this?

Every day, people send money, use apps and connect computers to the internet.
All of this creates a huge amount of data.

Hidden inside that data, some things are not normal. A thief may be sending
fake payments. A computer may be talking to a dangerous server. A chatbot may
be tricked into leaking secrets.

This project is my lab for building the software that **finds these problems
quickly**.

## 🧩 The four parts

📥 **Data Engineering**
Collect data, clean it, store it and keep it reliable.

💸 **Mobile Money Fraud Detection**
Spot strange money movements, like many transfers in a few minutes.

🌐 **Network Detection**
Notice when a computer starts acting differently from normal.

🤖 **AI Security**
Protect AI chatbots from tricks, attacks and data leaks.

## 🔄 How it works

1. Data comes in (payments, network logs, chat messages)
2. The system checks and cleans it
3. Detection rules look for strange behaviour
4. An alert is created with a clear reason
5. A person reviews the alert and decides what to do

> ⚠️ An alert is a warning sign, not proof. A human always makes the final call.

## 🧪 How I learn

I follow one simple loop for every feature:

**Build it → Break it → Fix it → Test it → Write it down**

Breaking my own work is the best way to learn how real systems fail.

## 🧰 Tools I use

All free and open source.

* Python (the main language)
* FastAPI (to build the backend)
* PostgreSQL (to store data)
* Redis (to track activity over time)
* Pandas and DuckDB (to study data)
* Docker (to package the project)
* Pytest (to test everything)
* GitHub Actions (to run checks automatically)

## 🗂️ Project layout

```text
src/        the main code
tests/      checks that prove the code works
docs/       my notes, diagrams and lessons
scripts/    small helper tools
examples/   sample data and demos
```

## 🚀 Quick start

```bash
git clone <your repository link>
cd security_data_engineering_lab
python -m venv venv
pip install -r requirements.txt
uvicorn src.security_lab.main:app --reload
```

Then open `http://localhost:8000/docs` to see the app.

## 🗺️ Roadmap

1. ✅ Python and backend basics
2. ⬜ Databases
3. ⬜ Data pipelines
4. ⬜ Detection rules
5. ⬜ Machine learning and AI security
6. ⬜ Going live safely



## 👋 Why this matters

Banks, phone companies and online apps all need people who can protect data.
This lab is how I am training to become one of them.

⭐ Follow along as I build, break and learn in public.
