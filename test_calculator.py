"""
Демо-тесты для проверки bi-directional GitHub интеграции с Allure TestOps.
Каждый тест снабжён allure-меткой epic/feature/story, чтобы результаты
были удобно сгруппированы в TestOps.
"""

import allure
import pytest


def add(a: int, b: int) -> int:
    return a + b


def divide(a: int, b: int) -> float:
    return a / b


@allure.epic("Calculator")
@allure.feature("Addition")
class TestAddition:

    @allure.story("Positive numbers")
    @pytest.mark.parametrize("a,b,expected", [(1, 2, 3), (10, 20, 30), (0, 0, 0)])
    def test_add_positive(self, a, b, expected):
        with allure.step(f"Add {a} + {b}"):
            result = add(a, b)
        assert result == expected

    @allure.story("Negative numbers")
    def test_add_negative(self):
        with allure.step("Add -5 + -7"):
            result = add(-5, -7)
        assert result == -12


@allure.epic("Calculator")
@allure.feature("Division")
class TestDivision:

    @allure.story("Normal division")
    def test_divide_normal(self):
        with allure.step("Divide 10 by 2"):
            result = divide(10, 2)
        assert result == 5

    @allure.story("Division by zero")
    def test_divide_by_zero(self):
        with allure.step("Divide 1 by 0, expect ZeroDivisionError"):
            with pytest.raises(ZeroDivisionError):
                divide(1, 0)

    @allure.story("Flaky example")
    def test_intentionally_failing(self):
        """
        Специально падающий тест — удобно, чтобы проверить,
        как выглядит rerun отдельного упавшего теста из TestOps.
        Когда тест перестанет быть нужен для проверки rerun,
        просто удали или почини его.
        """
        with allure.step("This assertion is intentionally wrong"):
            assert add(2, 2) == 5
