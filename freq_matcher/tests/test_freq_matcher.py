import pytest
from freq_matcher.freq_matcher import Matcher

@pytest.fixture
def example_abstracts():
    return {
        "oct_list": ["This study includes climate science and pollution."],
        "nov_list": ["This program is accessible.", "Gender ideology and race issues are addressed here."],
        "dec_list": ["Race and racism are systemic issues."],
        "jan_list": ["Nothing relevant here.", "This program is somewhat accessible and has an environment."],
        "feb_list": ["Let's talk about mental health.", "Socioeconomic is a keyword."],
        "mar_list": ["Nothing relevant here."]
    }

def test_match_ability(example_abstracts):
    matcher = Matcher(**example_abstracts)
    tally = matcher.match("ability")
    assert tally["oct"] == 0
    assert tally["nov"] == 1
    assert tally["dec"] == 0
    assert tally["jan"] == 1
    assert tally["feb"] == 1
    assert tally["mar"] == 0

def test_match_class(example_abstracts):
    matcher = Matcher(**example_abstracts)
    tally = matcher.match("class")
    assert tally["oct"] == 0
    assert tally["nov"] == 0
    assert tally["dec"] == 1
    assert tally["jan"] == 0
    assert tally["feb"] == 1
    assert tally["mar"] == 0

def test_match_climate(example_abstracts):
    matcher = Matcher(**example_abstracts)
    tally = matcher.match("climate")
    assert tally["oct"] == 2
    assert tally["nov"] == 0
    assert tally["dec"] == 0
    assert tally["jan"] == 1
    assert tally["feb"] == 0
    assert tally["mar"] == 0

def test_match_gs(example_abstracts):
    matcher = Matcher(**example_abstracts)
    tally = matcher.match("gs")
    assert tally["oct"] == 0
    assert tally["nov"] == 1
    assert tally["dec"] == 0
    assert tally["jan"] == 0
    assert tally["feb"] == 0
    assert tally["mar"] == 0

def test_match_re(example_abstracts):
    matcher = Matcher(**example_abstracts)
    tally = matcher.match("re")
    assert tally["oct"] == 0
    assert tally["nov"] == 1
    assert tally["dec"] == 2
    assert tally["jan"] == 0
    assert tally["feb"] == 0
    assert tally["mar"] == 0

def test_graph_shows_up(example_abstracts):
    matcher = Matcher(**example_abstracts)
    tally = matcher.match("gs", graph_true=True)
    assert isinstance(tally, dict)
