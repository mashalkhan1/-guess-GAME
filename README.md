# Number Guessing Game

A beginner-friendly number guessing game built with Python and Streamlit.

## Project files

- `guess_game.py` — command-line version of the game.
- `guess_game.ipynb` — Jupyter Notebook version.
- `app.py` — interactive Streamlit web app.
- `requirements.txt` — Python package requirements.

## How the game works

The computer chooses a random number between 1 and 100. The player enters guesses until the correct number is found. After each guess, the game gives a hint:

- **Too low** — try a higher number.
- **Too high** — try a lower number.
- **Correct** — the game ends and displays the number of attempts.

## Run the Python version

Make sure Python is installed. Open a terminal in this folder and run:

```bash
python guess_game.py
```

## Run the Jupyter Notebook

1. Open `guess_game.ipynb` in Jupyter Notebook or VS Code.
2. Run the cells from top to bottom.
3. Play the game in the notebook's input area.

## Run the Streamlit app

1. Open a terminal in this project folder.
2. (Optional but recommended) Create and activate a virtual environment.
3. Install the required package:

```bash
pip install -r requirements.txt
```

4. Start the app:

```bash
streamlit run app.py
```

5. Streamlit will open the game in your web browser. If it does not open automatically, use the local URL shown in the terminal.

## Concepts used

- Variables
- `input()` and `print()`
- `if`, `elif`, and `else`
- `while` loop
- Functions
- `random.randint()`
- Exception handling with `try` and `except`
- Streamlit widgets and `st.session_state`
