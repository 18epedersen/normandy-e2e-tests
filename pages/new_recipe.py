"""Expected conditions."""
from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from pages import locators
# import time


class NewRecipe(Base):
    """Recipe class."""

    LOCATORS = locators.NewRecipe

    def wait_for_page_to_load(self):
        """Wait for recipe page's submit button."""
        self.wait.until(EC.visibility_of_element_located(
         self.LOCATORS.primary))
        return self

    def pick_random_action(self):
        """Return a random recipe action."""
        from random import choice
        actions = ['console-log', 'show-heartbeat', 'preference-experiment']
        action = choice(actions)
        print("action is ", action)
        return action

    def create_new_recipe(self, conf):
        """Save recipe with a unique UUID."""
        """Return a recipe page, recipe name, and notification's texts."""
        import uuid
        from pages.view_recipe import ViewRecipe
        recipe_name = str(uuid.uuid1().hex)
        filter_expression = conf.get('recipe', 'filter_expression')
        recipe_action = self.pick_random_action()
        recipe_name_field = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.recipe_name_field))
        recipe_name_field.clear()
        recipe_name_field.send_keys(recipe_name)
        self.find_element(
         *self.LOCATORS.recipe_filter_expression).send_keys(
          filter_expression)
        self.configure_action(conf, recipe_action)
        save_button = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.save_button))
        save_button.click()
        return ViewRecipe(self.selenium, self.base_url).wait_for_page_to_load()

    def configure_action(self, conf, recipe_action):
        """Configure action for recipe."""
        select_action_dropdown = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.select_action_dropdown))
        select_action_dropdown.click()
        if recipe_action == 'console-log':
            console_log = self.find_element(*self.LOCATORS.console_log)
            console_log.click()
            message = conf.get('console_log', 'message')
            self.find_element(*self.LOCATORS.action_message).clear()
            self.find_element(*self.LOCATORS.action_message).send_keys(message)
        if recipe_action == 'show-heartbeat':
            heart_beat = self.find_element(*self.LOCATORS.show_heartbeat)
            heart_beat.click()
            survey_id = conf.get('heart_beat', 'survey_id')
            message = conf.get('heart_beat', 'message')
            thanks_message = conf.get('heart_beat', 'thanks_message')
            post_url = conf.get('heart_beat', 'post_url')
            learn_more = conf.get('heart_beat', 'learn_more')
            learn_more_url = conf.get('heart_beat', 'learn_more_url')
            self.find_element(*self.LOCATORS.survey_id).clear()
            self.find_element(*self.LOCATORS.survey_id).send_keys(survey_id)
            self.find_element(*self.LOCATORS.action_message).clear()
            self.find_element(*self.LOCATORS.action_message).send_keys(message)
            self.find_element(*self.LOCATORS.thanks_message).clear()
            self.find_element(*self.LOCATORS.thanks_message).send_keys(
             thanks_message)
            self.find_element(*self.LOCATORS.post_answer_url).clear()
            self.find_element(*self.LOCATORS.post_answer_url).send_keys(
             post_url)
            self.find_element(*self.LOCATORS.learn_more).clear()
            self.find_element(*self.LOCATORS.learn_more).send_keys(learn_more)
            self.find_element(*self.LOCATORS.learn_more_url).clear()
            self.find_element(*self.LOCATORS.learn_more_url).send_keys(
             learn_more_url)
        if recipe_action == 'preference-experiment':
            preference_experiment = self.find_element(
             *self.LOCATORS.preference_experiment)
            preference_experiment.click()
            experiment_name = conf.get('preference_experiment',
                                       'experiment_name')
            experiment_doc_url = conf.get('preference_experiment',
                                          'experiment_doc_url')
            preference_name = conf.get('preference_experiment',
                                       'preference_name')
            branch_name = conf.get('preference_experiment', 'branch_name')
            self.find_element(*self.LOCATORS.experiment_name).clear()
            self.find_element(*self.LOCATORS.experiment_name).send_keys(
             experiment_name)
            self.find_element(*self.LOCATORS.experiment_doc_url).clear()
            self.find_element(*self.LOCATORS.action_message).send_keys(
             experiment_doc_url)
            self.find_element(*self.LOCATORS.preference_name).clear()
            self.find_element(*self.LOCATORS.preference_name).send_keys(
             preference_name)
            self.find_element(*self.LOCATORS.branch_name).clear()
            self.find_element(*self.LOCATORS.branch_name).send_keys(
             branch_name)
