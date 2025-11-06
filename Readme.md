```

# My ML Project

## 1. Project Overview
This project is an **end-to-end modular ML application**.  
It demonstrates how to structure a Python project, manage dependencies, build reusable pipelines, and run ML workflows efficiently.

---

## 2. What I Learned
- Created **`requirements.txt`** and **`setup.py`**:
  - `setup.py` helps Python find all packages required for the ML application.
  - Defined:
    - `project_name`
    - `version`
    - `author` / `author_email`
    - `packages` (from `src`)
    - `install_requires` (automatically read from `requirements.txt`)

- Created **`src` folder** with **`__init__.py`**:
  - Makes `src` a **Python package**.
  - Modules inside `src` can now be imported anywhere in the project.```

---

## 3. Project Structure
- inside **`src` folder** i added two new folder called as **`components`** and **`pipeline`**









```
# 🌾 Crop Prediction — End-to-End ML Project

## 📘 1. Overview

This project is an end-to-end modular Machine Learning application built from scratch.
It demonstrates a production-ready structure with modularized code, reusable components, pipeline automation, and environment management — following real-world ML project architecture.

## 🧠 2. What I Learned

Through this project, I learned to build a complete ML pipeline systematically and professionally.

## 🔹 Project Setup

Created a requirements.txt file to list all dependencies.

Built a setup.py file for packaging the ML application.

Defined:

project_name

version

author and author_email

packages (automatically discovered from src)

install_requires (dependencies auto-loaded from requirements.txt)

## 🔹 Project Packaging

Created a src folder as the main source code directory.

Added an __init__.py file to make it a Python package, enabling imports across the project.
- **`components`** it means that here we make data_ingestion.py, data_transformation.py, model_trainin.py and also we have __init__.py as make our folder as a package
- **`pipeline`** here we have train_pipeline.py, predict_pipeline.py and also there is __init__.py  make its as a package 
