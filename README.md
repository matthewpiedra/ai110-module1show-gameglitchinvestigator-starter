# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [Guess the secret number with the provided number of attempts until you guess the secret number] Describe the game's purpose.
- [Too high and too low swapped, decimal number parsing, even number increasing score even though its wrong] Detail which bugs you found.
- [decimal number treated as invalid input, swapped too high and too low, and every wrong guess should decrease score regardless if it is even or not] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess in the input box with a decimal number
2. Game treats the decimal input as invalid and prompts the user to enter a whole number

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
tests/test_game_logic.py .......                                                                                                                                 [100%]

========================================================================== 7 passed in 0.01s ===========================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
