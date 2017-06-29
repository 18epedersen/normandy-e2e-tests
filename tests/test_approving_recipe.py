import pytest
from page.login import Login


# test to successfully approval a recipe
@pytest.mark.destructive
def test_approving_recipe(base_url, selenium, variables):
    """Test the approval flow of a recipe."""
    page = Login(selenium, base_url).open()
    duo = page.login(variables['username'], variables["password"])
    duo.switch_to_frame(
      duo.find_element(*duo._duoiframe_locator))
    home = duo.login_duo(variables['secret'])
    home.switch_to_default_content()
    recipe = home.add_recipe()
    approval = recipe.create_recipe(variables['additional filters'],
                                    variables['action'], variables['message'])
    home = approval.approve_recipe(variables['approve'])
    # fix assert statement
    assert home.heading == "shield"
