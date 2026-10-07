from logic_utils import check_guess, parse_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_too_high_tells_player_to_go_lower():
    # Regression: the hint direction was inverted
    _, message = check_guess(60, 50)
    assert "LOWER" in message


def test_too_low_tells_player_to_go_higher():
    # Regression: the hint direction was inverted
    _, message = check_guess(40, 50)
    assert "HIGHER" in message


def test_numeric_not_string_comparison():
    # Regression: a string secret made "9" > "10" compare lexicographically
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"


def test_parse_guess_non_numeric_text():
    ok, value, err = parse_guess("abc")
    assert (ok, value) == (False, None)
    assert err == "That is not a number."


def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert (ok, value) == (False, None)
    assert err == "Enter a guess."


def test_parse_guess_negative_number():
    ok, value, err = parse_guess("-5")
    assert (ok, value, err) == (True, -5, None)
