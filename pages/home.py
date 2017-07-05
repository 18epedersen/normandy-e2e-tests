"""By method for selenium webdriver."""
from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from pages import locators


class Home(Base):
    """Class for Normandy Control UI Home."""

    LOCATORS = locators.Home
    # def __init__(self, conf):
    #     """Create home page."""
    #     self.addbutton_locator = conf.get('home', 'addbutton_locator')
    #     self.name_locator = conf.get('recipe', 'name_locator')
    #     self.filtertextbox_locator = conf.get('recipe',
    #                                           'filtertextbox_locator')
    #     self.action_locator = conf.get('recipe', 'action')
    #     self.actionmessage_locator = conf.get('recipe',
    #                                           'actionmessage_locator')
    #     self.save_locator = conf.get('recipe', 'save_locator')
    #     self.requestbutton_locator = conf.get('recipe',
    #                                           'requestbutton_locator')
    #     self.approvebutton_locator = conf.get('recipe',
    #                                           'approvebutton_locator')
    #     self.approvemessagetextbox_locator = conf.get('recipe',
    #                                                   'approvemessagetextbox_locator') # noqa
    #     self.approvemessagebutton_locator = conf.get('recipe',
    #                                                  'approvemessagebutton_locator') # noqa
    #     self.enablebutton_locator = conf.get('recipe', 'enablebutton_locator')
    #     self.confirmbutton_locator = conf.get('recipe',
    #                                           'confirmbutton_locator')
    #     self.recipesbreadcrumb_locator = conf.get('recipe',
    #                                               'recipesbreadcrumb_locator')
    #     # locator for recipe table

    def wait_for_page_to_load(self):
        """Wait for page to load."""
        self.wait.until(EC.visibility_of_element_located(
           self.addrecipe_locator))
        return self

    def add_recipe(self):
        """Click add button to create recipe."""
        from pages.recipe import Recipe
        self.find_element(*self.LOCATORS.addbutton).click()
        return Recipe(self.selenium, self.base_url).wait_for_page_to_load()
