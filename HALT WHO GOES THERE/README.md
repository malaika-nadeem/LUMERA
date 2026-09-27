#💀HALT! WHO GOES THERE?

A small neural-network security experiment that classifies login attempts as **legitimate user, impersonator, or bot**.

HALT uses login behavior such as login time, country match, device familiarity, and email-account consistency to learn patterns associated with different types of login attempts.

## Overview

The project uses a **Keras/TensorFlow softmax classifier** with a single hidden layer.

The model takes five input features:

* `hour_sin` — cyclical representation of login hour
* `hour_cos` — cyclical representation of login hour
* `country_match` — whether the country matches the expected country
* `device_known` — whether the device is recognized
* `email_matches_account` — whether the email matches the account

The output contains three classes:

* `legitimate user`
* `impersonator`
* `bot`

## Model

```text
Input: 5 features
        ↓
Dense: 16 neurons + ReLU
        ↓
Dense: 3 neurons + Softmax
        ↓
Login classification
```

The model is trained using:

* **Optimizer:** Adam
* **Loss:** Sparse Categorical Crossentropy
* **Training:** 100 epochs
* **Train/Test Split:** 70/30
* **Stratification:** Enabled

## Feature Engineering

Login hour is represented using sine and cosine rather than linear scaling:

```python
hour_sin = np.sin(2 * np.pi * login_hour / 24)
hour_cos = np.cos(2 * np.pi * login_hour / 24)
```

This preserves the cyclical nature of time, where `23:00` and `00:00` are close to each other.

## Prediction

The `check_login()` function accepts a login attempt and returns:

* Predicted class
* Prediction confidence
* Probability for each class

Example input:

```text
login_hour = 23
country_match = 0
device_known = 0
email_matches_account = 1
```

The model then evaluates the attempt and classifies it based on the patterns learned from the dataset.

## Dataset

The dataset contains simulated login attempts with four input attributes and a target label:

```text
login_hour
country_match
device_known
email_matches_account
label
```

The dataset is intended for experimentation and model-learning purposes rather than real-world authentication.

## Technologies

* Python
* TensorFlow / Keras
* NumPy
* Pandas
* Scikit-learn
* Matplotlib

## Project Structure

```text
HALT WHO GOES THERE/
├── HALTWHOGOESTHERE.py
├── halt_who_goes_there_logins.csv
└── README.md
```

## Running

Install dependencies:

```bash
pip install tensorflow numpy pandas scikit-learn matplotlib
```

Run the program:

```bash
python HALTWHOGOESTHERE.py
```

## Purpose

HALT is an experimental project exploring how a small neural network can learn behavioral patterns from login data and use those patterns for multi-class classification.

> **HALT! WHO GOES THERE?**
>
> A small experiment in machine learning, behavioral signals, and security.
