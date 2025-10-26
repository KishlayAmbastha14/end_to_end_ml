## learning phased

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
  - Modules inside `src` can now be imported anywhere in the project.

---

## 3. Project Structure
- inside **`src` folder** i added two new folder called as **`components`** and **`pipeline`** 
- **`components`** it means that here we make data_ingestion.py, data_transformation.py, model_trainin.py and also we have __init__.py as make our folder as a package
- **`pipeline`** here we have train_pipeline.py, predict_pipeline.py and also there is __init__.py  make its as a package 
