# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
 The game has a GUI with a prompt to guess a number between 1 and 100, an "Attempts left" counter showing 7, a "Developer Debug Info" dropdown section, a text box, and "Submit Guess" and "New Game" buttons and a "Show hint" checkbox. When I entered the secret number from the debug section, I got a "You Won" message onscreen.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - Backwards hints: high guess would suggest going higher; vice versa for low guesses
  - Enter key does not submit: there is a prompt in the guess text entry box that tells the user to press Enter to submit; it doesn't work
  - New Game does not fully reset: pressing "New Game" button doesn't allow the user to play a new game; it just resets some stats
  - Blank guesses allows unlimited attempts: Pressing Submit with nothing in the text entry box allows infinite attempts and the attempts counter goes negative


**Pre-fix run trace** (headless run of the original app.py using Streamlit's AppTest, secret forced to 50)

```
== Scenario 1: hints (secret forced to 50 via Debug Info) ==
guess 22 -> "Go LOWER!"   attempts=2 score=-5
guess 60 -> "Go HIGHER!"  attempts=3 score=-10
guess 9  -> "Go HIGHER!"  attempts=4 score=-5
guess 70 -> "Go HIGHER!"  attempts=5 score=-10

== Scenario 2: New Game after losing ==
after 7 wrong guesses   -> "Out of attempts! The secret was 50. Score: -35"  status=lost
after New Game          -> secret=33 attempts=0 score=-35 status=lost history=[1,1,1,1,1,1,1]
guess 50 after New Game -> "Game over. Start a new game to try again."

== Scenario 3: blank guesses ==
after 10 blank submits  -> "Enter a guess."  attempts=11 status=playing
info banner             -> "Attempts left: -2"
```

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location |
|-------|-------------------|-----------------|------------------------|-------------------------|
| Secret 50 (from debug info), guess 22 | "📈 Go HIGHER!" (Too Low) | "📉 Go LOWER!" shown | none | app.py `check_guess`, lines 39, 42, 49, 50 |
| Typed a guess and pressed Enter | Guess is submitted | Nothing happens until Submit is clicked | none | app.py line 124 (`st.text_input`) |
| Pressed New Game (after a win or loss) | Full reset and playable again | Only Attempts Left, Secret, and Attempts reset; buttons do nothing | none | app.py lines 137-144, 146-151 |
| Left the guess box empty and pressed Submit repeatedly | Rejected without exceeding the attempt limit | Attempts exceed the limit and the game never ends | "Enter a guess." | app.py lines 154-160, 189-195 |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Claude Code (in VS Code).
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  Claude explained the hint bug: `check_guess` returned "Go HIGHER" when the guess was above the secret, and on even attempts `app.py` also cast the secret to a string, so `check_guess` fell into a string-comparison branch (`"9" > "10"`). It suggested moving `check_guess` into `logic_utils.py`, swapping the messages, and deleting the string cast. This was correct because it fixed both causes of the wrong hints instead of only swapping the messages. I verified it with pytest (including `check_guess(9, 10)` returning "Too Low") and with a headless game run where guesses 22, 60, 9, and 70 against a secret of 50 all got the right hint on both odd and even attempts.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
  For the New Game fix, Claude first recommended leaving `attempts` reset at 0 to keep the change small. After we compared it against the grading criteria, Claude reversed that recommendation and I accepted the change to 1, because the first game starts at 1 and a reset to 0 would give a new game one extra attempt (a partial fix). I verified it with the headless run: after New Game, `attempts=1`, `status=playing`, `score=0`, and history was empty. I also did not accept Claude's earlier proposal to restructure my section 1 write-up, and kept my own wording.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I re-ran the same headless scenarios from my pre-fix trace and compared the output. After the fix, guesses 22, 60, 9, and 70 against a secret of 50 gave the correct hints, and New Game after a loss reset to `attempts=1 score=0 status=playing history=[]` and accepted a new guess.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  `pytest` ran 9 tests and all passed. The regression test `check_guess(9, 10)` returning "Too Low" showed the string-comparison bug is gone. The three starter tests initially failed because `check_guess` returns an `(outcome, message)` tuple, so I updated them to unpack it.
- Did AI help you design or understand any tests? How?
  Yes. Claude suggested the regression tests for the hint direction and the 9-vs-10 case, plus three `parse_guess` edge cases (non-numeric text, empty string, negative number). It also pointed out that the starter tests expected a plain string and would fail against the tuple return.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
