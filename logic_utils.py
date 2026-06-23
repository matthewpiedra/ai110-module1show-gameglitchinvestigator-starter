#FIX: Refactored logic into logic_utils.py using agent mode
# Hard should have a larger range like 1–500 to be genuinely harder
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 500
    return 1, 100

#FIX: Refactored logic into logic_utils.py using agent mode
# treat decimal input as invalid, just like non-numeric input:
def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if not raw:
        return False, None, "Enter a guess."

    if "." in raw:
        return False, None, "Enter a whole number."

    try:
        value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

#FIX: Refactored logic into logic_utils.py using agent mode
# swap the messages so "Go LOWER!" accompanies too-high guesses
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"

#FIX: Refactored logic into logic_utils.py using agent mode
# wrong guesses on even attempt_number award +5 instead of -5. The fix is to always deduct 5 for "Too High" on wrong guesses
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
