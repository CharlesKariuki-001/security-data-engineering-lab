# Security Data Engineering Lab

A place where I learn to build software that spots danger hidden inside data.


## What is this project?

Every day, people send money from their phones, use apps, and connect computers to the internet. All of this creates a huge amount of data.

Most of that data is normal. But some of it is not:

* A thief sends many fake payments in a few minutes.
* A computer starts talking to a dangerous server it never contacted before.
* A chatbot is tricked into sharing secrets it should keep private.

This lab is where I build the software that finds these problems, explains them clearly, and raises an alert for a person to check.

## Who is this for?

If you are a manager, a recruiter, a business owner or just curious, this README explains what I am building and why it matters. If you are a developer, the sections further down show the tools, the structure and the plan.

## The big idea in one picture

```text
Data comes in  →  It is checked and cleaned  →  It is stored safely
                                                      ↓
A person reviews the alert  ←  An alert is created  ←  Detection rules look for danger
```

Think of it like a security guard at a busy building. The guard watches who comes in, remembers what normal looks like, notices when something is odd, and calls for help with a clear reason.

## The four parts of the lab

### 1. Data Engineering
This is the foundation. Before anything can be detected, data must be collected, cleaned, stored and kept reliable. Bad data leads to bad decisions, so I learn how to receive records, remove duplicates, catch errors and organise everything properly.

### 2. Mobile Money Fraud Detection
Mobile money moves fast, so fraud moves fast too. Here I build rules that notice strange patterns, such as many transfers in a short time, sudden changes in behaviour, or several accounts acting in a linked way.

### 3. Network Detection and Response
Computers talk to each other all day. Here I learn what normal conversation looks like, then build tools that notice when a computer starts behaving differently.

### 4. AI Security
More apps now use AI chatbots, and they can be tricked. I learn how attackers fool them, how private information leaks out, and how to build protection around AI so it is safer to use.

## An important promise

An alert is a warning sign, not proof.

A strange pattern does not always mean a crime. Many alerts will turn out to be normal behaviour. That is why this lab always keeps a human in charge of the final decision, and why I measure how often my detection is wrong, not only how often it is right.

## How I learn: Build, Break, Fix

I do not just follow tutorials. For every feature I follow the same loop:

1. Understand: what problem am I solving?
2. Build: make a working version.
3. Break: attack my own work, and see how it fails.
4. Investigate: find out exactly why it failed.
5. Fix: rebuild it properly.
6. Test: write a check that proves the fix works.
7. Document: write down what I learned.

Breaking my own software is the fastest way to learn how real systems fail. Questions I ask myself often:

* What happens if the database goes offline?
* What happens if the same record arrives twice?
* What happens if 500 requests arrive at once?
* What happens if someone sends broken or harmful input?
* What happens if my detection gives a wrong answer?

## Tools I use

Everything here is free and open source.

* Python: the main language
* FastAPI: builds the backend that receives data
* PostgreSQL: stores the data safely
* Redis: tracks activity over short periods of time
* Pandas and DuckDB: study and summarise large amounts of data
* Scikit learn: simple machine learning
* Docker: packages the project so it runs the same everywhere
* Pytest: automatic checks that prove the code works
* GitHub Actions: runs those checks every time I save my work
* Bandit: scans my code for security mistakes

## How the project is organised

```text
src/        The main code of the lab
tests/      Automatic checks that prove the code works
docs/       Architecture notes, diagrams and lessons learned
scripts/    Small helper tools
examples/   Sample data and demos
```

A key design rule: the detection logic is kept separate from the web layer and the database. This means I can test the thinking of the system on its own, without starting the whole application.

Folders are only created when they are truly needed, so the structure grows with my understanding.

## Roadmap

The order matters. Each stage gives me the foundation for the next one.

Stage 1: Python and backend basics
Build an API that receives data and checks that it is valid.

Stage 2: Databases
Store records reliably, and learn how to keep data correct even when many things happen at once.

Stage 3: Data pipelines
Clean, organise and process large files of transactions and network records.

Stage 4: Detection rules
Build the engine that finds suspicious money activity and unusual network behaviour.

Stage 5: Machine learning and AI security
Measure how good detection really is, and protect AI chatbots from attacks.

Stage 6: Going live safely
Package, monitor, secure and document the whole system.

Progress is tracked in `PROGRESS.md` as I complete each stage.

## What you will find here over time

* Working software
* Architecture diagrams
* Automatic tests
* Notes on what broke and how I fixed it
* Speed and load measurements
* Security test results
* Honest limits of what each part can and cannot do

## Getting started

These steps will work once the first stage of code is saved in the repository.

```bash
git clone https://github.com/CharlesKariuki-001/security-data-engineering-lab.git
cd security-data-engineering-lab
python -m venv venv
python -m pip install fastapi uvicorn
uvicorn src.security_lab.main:app
```

Then open `http://localhost:8000/docs` in your browser to see the app.

## Safety and honesty

* All data in this lab is fake and created by me.
* I only test on my own computers and systems.
* No real personal or financial information is ever used.
* This is a learning project, so it is not ready to protect a real business yet.

## Why this matters

Banks, phone companies, online shops and fast growing apps all depend on data, and they all need people who can protect it. Few people can build the full path from raw data to a trustworthy alert. This lab is how I am training to become one of them.

## Follow along

Watch or star this repository to see the project grow, one stage at a time.

Repository: https://github.com/CharlesKariuki-001/security-data-engineering-lab
