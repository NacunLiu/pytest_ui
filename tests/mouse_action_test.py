import pytest
from pages.mouse_action_page import MouseActionPage

mouse_loc = (By.CSS_SELECTOR, '')

@pytest.mark.usefixtures('main_page')
def test_change_color(main_page):
    