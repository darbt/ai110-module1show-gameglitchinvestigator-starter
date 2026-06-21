# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  When I first ran the program, the hints didn't even work the first time at all. Once I reoloaded the program, that when the hints showed up but they proved to be very inaccurate. 

  The hints lie, answer was 1 but when inputting 5, the program said for me to guess higher. 

  New game seems to crash sometimes. After trying to input something after a new game it doesn't register anything

  Game difficulty seems to also not work properly. Description states that easy mode range is 1-20 but the instructions don't change and the secret is 95. Only thing that changes is the number of attempts

  The input says that we can press enter to apply, but that does not seems to work either

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|52     | "Go Lower"        | "Go Higher"     | None                   |
|100    | "Go Lower"        | "Go Higher"     | None                   |
|15     | "Go Higher"       | "Go Lower       | None                   |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  The AI suggested getting rid of the line where it does and int-string ceonversion on every even number attempt. I agreed because it didn't seem to serve a purpose other than to be a bug. When running the program after getting rid of the bug, the porgram still worked perfectly. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  When talking about the hint bug, the AI didn't even suggest the idea of the messages being switched. It pointed to a different line in the code which had to do with int-string conversion and while I agreed that line was unnecessary it wasn't the core issue and I had to point out the mismatched messages to the AI myself
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  Through two ways. A pytest case and testing it on the actual live game. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  Through a pytest case, I tested the Hint bug. Check guess takes two inputs. The first input is the user's guess and the second input is the actual secret number. If the guess is higher than the secret, the output should be "Go Lower", if the guess is smaller than the secret than the output should be "Go Higher". 
- Did AI help you design or understand any tests? How?
  Ai generated the pytest cases but since I have some experience in test cases like these, it didn't really add to my knowledge. It generated the test, I checked to make sure they were accurate and once I determined that, I ran the test cases. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
