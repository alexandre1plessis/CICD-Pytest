# test_push.py

import pytest

# Exemple de fonction
def push_to_stack(stack, item):
    stack.append(item)
    return stack

# Un test simple pour vérifier si l'item est bien ajouté au stack
def test_push_to_stack():
    stack = []
    push_to_stack(stack, "item")
    assert stack == ["item"], "L'item n'a pas été ajouté au stack"

# Peut également tester des cas d'erreurs attendus ou des exceptions
def test_push_to_stack_exception():
    stack = "pas un stack"
    with pytest.raises(AttributeError):
        push_to_stack(stack, "item")

# Si besoin de paramètres pour les tests, peut utiliser des fixtures
@pytest.fixture
def stack():
    return []

def test_push_to_stack_with_fixture(stack):
    push_to_stack(stack, "item")
    assert stack == ["item"], "L'item n'a pas été ajouté au stack avec fixture"
