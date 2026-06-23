from logic_utils import check_guess, get_range_for_difficulty, update_score, parse_guess

def test_hard_range_is_harder_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high, (
        f"Hard upper bound ({hard_high}) should be greater than Normal ({normal_high})"
    )

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ('Win', '🎉 Correct!')

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ('Too High', '📉 Go LOWER!')

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ('Too Low', '📈 Go HIGHER!')

def test_hint_direction_not_swapped():
    # Regression: original bug returned "Go HIGHER!" when guess was too high
    # and "Go LOWER!" when guess was too low — exactly backwards.
    _, message_high = check_guess(99, 1)
    assert "LOWER" in message_high, (
        f"Guess too high should say Go LOWER, got: {message_high!r}"
    )

    _, message_low = check_guess(1, 99)
    assert "HIGHER" in message_low, (
        f"Guess too low should say Go HIGHER, got: {message_low!r}"
    )

def test_decimal_input_is_rejected():
    # Regression: "3.7" was previously accepted and silently truncated to 3
    # instead of returning an error. Decimals must be rejected outright.
    ok, value, err = parse_guess("3.7")
    assert not ok, "Decimal input should be rejected"
    assert value is None
    assert err is not None, "Should return an error message for decimal input"

def test_even_numbered_wrong_guess_deducts_points():
    # Regression: even attempt numbers for "Too High" guesses were awarding +5
    # instead of deducting 5. All wrong guesses should always lose 5 points.
    score_before = 50
    for attempt in [2, 4, 6]:
        score_after = update_score(score_before, "Too High", attempt)
        assert score_after == score_before - 5, (
            f"Attempt {attempt} (even): expected {score_before - 5}, got {score_after}"
        )
