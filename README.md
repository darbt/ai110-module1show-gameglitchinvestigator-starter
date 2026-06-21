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

- [ ] Describe the game's purpose.
   The purpose of the game is a fun and quick game of guess the number. The game generates a random number in a range based on the difficulty. That number becomes the game's "secret" and the user has to guess the secret within a certain number of attempts. With hints enabled, the game will inform if a guess is too big or too small. The game will end either when the user guesses the number correctly or when all the number of attempts have been used up. 
- [ ] Detail which bugs you found.
   1. The hints were broken. If if a guess was too high, then the hint would tell the user to go higher. If a guess was too lowm then the hint would tell the user to go lower
   2. The difficulty also didn't actually change the range. It only changed the range in the difficulty instructuons section but the number would still be in the range of 1-100. 
- [ ] Explain what fixes you applied.
   1. For the hints issue. It was a simple fix of just swithcing the messages based on the return. Too high needs the message "Go lower", and vice versa for Too low.
   2. For the difficulty bug, 1-100 was hardcoded when a new game was generated so no matter what difficulty was chosen the range will always be 1-100. To fix this, I used the variables low and high that we recieve from the get_range_for_difficulty function. 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Input a guess within the range described. (Range and attempt number varies depending on game difficulty) (e.g. Range = 1-50, secret = 32, User guesses: 45)
2. (If hints are enabled), If your guess is too big, hint will inform you to guess lower (Game Returns Too High, displays "Go Lower", User guesses: 24)
3. (If hints are enabled), If your guess is too small, hint will inform you to guess higher (Game returns Too Low, displays "Go Higher", User guesses: 32)
4. If you can guess the secret within the number of attempts, you win and get a  congratulatory message along with your score, Otherwise You will get a message saying that you ran out of attempts and that is Game Over!
5. Click new game, to start a brand new game and refresh everything 

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
