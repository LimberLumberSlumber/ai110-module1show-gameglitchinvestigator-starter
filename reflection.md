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


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location |
|-------|-------------------|-----------------|------------------------|-------------------------|
| Secret 50 (from debug info), guess 22 | "📈 Go HIGHER!" (Too Low) | "📉 Go LOWER!" shown | none | app.py `check_guess`, lines 38, 40, 46, 47 |
| Typed a guess and pressed Enter | Guess is submitted | Nothing happens until Submit is clicked | none | app.py line 121 (`st.text_input`) |
| Pressed New Game (after a win or loss) | Full reset and playable again | Only Attempts Left, Secret, and Attempts reset; buttons do nothing | none | app.py lines 134-138, 140-145 |
| Left the guess box empty and pressed Submit repeatedly | Rejected without exceeding the attempt limit | Attempts exceed the limit and the game never ends | "Enter a guess." | app.py lines 148-154, 182-188 |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
