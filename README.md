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

- [x] Describe the game's purpose.

  Game Glitch Investigator is a Streamlit number-guessing game: guess the secret number within a limited number of attempts, with Higher/Lower hints and a score. The starter code shipped with bugs, and the goal was to find, document, and fix them.

- [x] Detail which bugs you found.

  Full reproduction table and run trace are in `reflection.md`.
  - Hints were backwards: a guess above the secret said "Go HIGHER" and vice versa. On even attempts the secret was also cast to a string, forcing a text comparison (`"9" > "10"`).
  - New Game only reset some stats, so `status` stayed "won"/"lost" and the game stayed blocked; score and history were not cleared.
  - The Enter key does not submit the guess; the Submit button is required.
  - Blank guesses use up attempts without ever ending the game ("Attempts left" goes negative).

- [x] Explain what fixes you applied.

  - Moved `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` into `logic_utils.py`; fixed the hint direction in `check_guess`; removed the string cast of the secret in `app.py`.
  - New Game now resets `status`, `score`, and `history`, uses the selected difficulty's range, and starts `attempts` at 1 like the first game.
  - The Enter-key and blank-guess bugs are documented but not fixed.

## 📸 Demo Walkthrough

A headless run of the fixed app (Streamlit `AppTest`, secret forced to 50):

1. Start a game on Normal difficulty (1-100); attempts left starts at 7.
2. Guess 22: the hint says "📈 Go HIGHER!" (22 is below 50).
3. Guess 60: the hint says "📉 Go LOWER!".
4. Guess 9 says "📈 Go HIGHER!" and guess 70 says "📉 Go LOWER!", on both odd and even attempts.
5. Make 7 wrong guesses to lose: "Out of attempts! The secret was 50."
6. Press New Game: score returns to 0, history is empty, status is "playing", attempts is 1.
7. Guess again: the game accepts it and shows a hint.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
tests/test_game_logic.py::test_winning_guess PASSED                      [ 11%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 22%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 33%]
tests/test_game_logic.py::test_too_high_tells_player_to_go_lower PASSED  [ 44%]
tests/test_game_logic.py::test_too_low_tells_player_to_go_higher PASSED  [ 55%]
tests/test_game_logic.py::test_numeric_not_string_comparison PASSED      [ 66%]
tests/test_game_logic.py::test_parse_guess_non_numeric_text PASSED       [ 77%]
tests/test_game_logic.py::test_parse_guess_empty_string PASSED           [ 88%]
tests/test_game_logic.py::test_parse_guess_negative_number PASSED        [100%]

============================== 9 passed in 0.05s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
- [x] Advanced edge-case testing: `parse_guess` tests for non-numeric text, an empty string, and a negative number (see `tests/test_game_logic.py` and `ai_interactions.md`).
