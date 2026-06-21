from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Regression tests for the swapped-hint bug ---
# The bug: when the guess was too HIGH, the message told the player to
# "Go HIGHER!" (and vice versa). The outcome label was correct, so these
# tests assert on the MESSAGE direction, which is where the bug lived.

def test_too_high_message_says_go_lower():
    # Guess (60) is above secret (50) -> player must go LOWER
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()
    assert "HIGHER" not in message.upper()


def test_too_low_message_says_go_higher():
    # Guess (40) is below secret (50) -> player must go HIGHER
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()
    assert "LOWER" not in message.upper()


# --- Regression tests for the swapped difficulty-range bug ---
# The bug: get_range_for_difficulty had Normal and Hard ranges swapped, so
# Hard returned (1, 50) and Normal returned (1, 100). That made "Hard"
# easier than "Normal". These tests pin the correct ranges and the ordering.

def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_normal_range():
    assert get_range_for_difficulty("Normal") == (1, 50)


def test_hard_range():
    # This is the exact case that was broken: Hard must be (1, 100), not (1, 50).
    assert get_range_for_difficulty("Hard") == (1, 100)


def test_difficulty_increases_range_size():
    # Harder difficulty must mean a wider (not narrower) guessing range.
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high < hard_high


def test_unknown_difficulty_defaults_to_full_range():
    assert get_range_for_difficulty("Whatever") == (1, 100)
