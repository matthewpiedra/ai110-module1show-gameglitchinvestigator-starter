# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- new game doesn’t work at all, the developer debug info refreshes the secret and attempts, but not history and game session
		- I get stuck on game won! If I win
- It seems the settings range does match the “make a guess” dialog box number range, nor does the secret number
		- Settings should sync, and the attempts left are off by 1 to the settings attempts allowed
- When clicking submit guess, I expect the history field to autofill, not anytime I enter a new number
		- Almost like developer debug info only updates if I click enter or enter new number, it should auto update when I guess a 		number

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guess of 10 | Go higher hint | Go lower hint | |
| guess of 200 | Go lower hint | Go higher hint | |
| Click on new game | history resets | history does not reset | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- I used Claude 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- When I asked Claude to help me refactor the logic into a separate file, it suggested creating a `logic_utils.py` file and moving the functions there. I followed its suggestion, and after refactoring, I ran the game and verified that the functionality remained intact by testing various guesses and ensuring the outcomes were as expected. For example, get_range_for_difficulty function
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
- AI was incorrect when I gave a vague request for fixing the update_score function. By having it first analyze the function, it gained a better understanding of the logic and then suggested a fix that was more accurate. I verified the result by running tests and checking the score updates for various scenarios, confirming that the function now behaves as intended.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- I decided by having claude generate a pytest for the function, and then I ran the test to see if it passed. If the test passed, I considered the bug fixed. Additionally, I manually tested the game by playing through various scenarios to ensure that the expected behavior was consistent with the actual behavior.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - I ran a pytest for the `check_guess` function, which tested various scenarios such as guesses being too high, too low, or correct. The test confirmed that the function returned the expected outcomes and messages for each scenario.
- Did AI help you design or understand any tests? How?
- Yes, I used AI to generate a test for each specific bug it fixed. I provided the AI with the function and asked it to create a pytest that would cover different cases. The AI generated tests that I could run to verify that the function behaved as expected, which helped me understand how to structure my own tests in the future.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - Validate AI generated code, check for errors, and run tests to ensure functionality is correct. I want to continue using AI as a tool to assist in coding, but I will always verify its suggestions and test the code thoroughly before considering it complete.
- What is one thing you would do differently next time you work with AI on a coding task?
  - Be patient, and provide clear, specific instructions to the AI. I would also take the time to understand the code it generates, rather than blindly accepting its suggestions, to ensure that I can effectively debug and maintain the code in the future.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - AI code is not perfect and requires human oversight. While it can be a powerful tool for generating code quickly, it is essential to validate its output, understand the logic, and test thoroughly to ensure that the final product meets the desired functionality and quality standards.
