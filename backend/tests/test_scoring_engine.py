import pytest

from app.scoring.engine import calculate_weighted_score


def test_calculate_weighted_score_with_equal_weights():
    category_scores = {
        "demand": 80,
        "competition": 60,
        "affordability": 70,
        "transit": 90,
        "growth": 50,
    }

    weights = {
        "demand": 0.20,
        "competition": 0.20,
        "affordability": 0.20,
        "transit": 0.20,
        "growth": 0.20,
    }

    result = calculate_weighted_score(category_scores, weights)

    assert result == 70.0


def test_calculate_weighted_score_with_custom_weights():
    category_scores = {
        "demand": 90,
        "competition": 40,
        "affordability": 80,
        "transit": 70,
        "growth": 60,
    }

    weights = {
        "demand": 0.30,
        "competition": 0.10,
        "affordability": 0.30,
        "transit": 0.20,
        "growth": 0.10,
    }

    result = calculate_weighted_score(category_scores, weights)

    assert result == 75.0


def test_calculate_weighted_score_rejects_missing_score_category():
    category_scores = {
        "demand": 80,
        "competition": 60,
        "affordability": 70,
        "transit": 90,
    }

    weights = {
        "demand": 0.20,
        "competition": 0.20,
        "affordability": 0.20,
        "transit": 0.20,
        "growth": 0.20,
    }

    with pytest.raises(ValueError):
        calculate_weighted_score(category_scores, weights)


def test_calculate_weighted_score_rejects_score_above_100():
    category_scores = {
        "demand": 120,
        "competition": 60,
        "affordability": 70,
        "transit": 90,
        "growth": 50,
    }

    weights = {
        "demand": 0.20,
        "competition": 0.20,
        "affordability": 0.20,
        "transit": 0.20,
        "growth": 0.20,
    }

    with pytest.raises(ValueError):
        calculate_weighted_score(category_scores, weights)