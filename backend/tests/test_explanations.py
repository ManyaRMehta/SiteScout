from app.scoring.explanations import generate_explanation


def test_generate_explanation_mentions_strengths():
    category_scores = {
        "demand": 85,
        "competition": 60,
        "affordability": 50,
        "transit": 90,
        "growth": 40,
    }

    explanation = generate_explanation(category_scores)

    assert "strong customer demand" in explanation
    assert "good transit and accessibility" in explanation


def test_generate_explanation_mentions_manageable_competition():
    category_scores = {
        "demand": 60,
        "competition": 70,
        "affordability": 60,
        "transit": 60,
        "growth": 60,
    }

    explanation = generate_explanation(category_scores)

    assert "Competition appears manageable" in explanation


def test_generate_explanation_mentions_high_competition_risk():
    category_scores = {
        "demand": 60,
        "competition": 40,
        "affordability": 60,
        "transit": 60,
        "growth": 60,
    }

    explanation = generate_explanation(category_scores)

    assert "differentiation is important" in explanation