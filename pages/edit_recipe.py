from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from pages import locators
import time


class EditRecipe(Base):
    """Edit Recipe."""

    LOCATORS = locators.EditRecipe

    # def get_recipe_name(self):
    #     """Get the recipe name."""
    #     recipe_name_field = self.wait.until(EC.element_to_be_clickable(
    #       self.LOCATORS.recipe_name_field))
    #     name = recipe_name_field.get_attribute('value')
    #     print("name", name)
    #     return name
    #
    # def get_selected_action(self):
    #     """Get current recipe action."""
    #     selected_action_name = self.find_element(
    #      *self.LOCATORS.selected_action_name)
    #     selected_recipe_action_text = selected_action_name.text
    #     print("selected recipe action ", selected_recipe_action_text)
    #     return selected_recipe_action_text

    def pick_new_random_action(self, selected_recipe_action):
        """Return a random recipe action."""
        from random import choice
        actions = ['console-log', 'show-heartbeat', 'preference-experiment']
        new_recipe_action = selected_recipe_action
        while new_recipe_action == selected_recipe_action:
            new_recipe_action = choice(actions)
        print("new action is ", new_recipe_action)
        return new_recipe_action

    def edit_recipe(self, conf):
        """Save recipe with a unique UUID."""
        """Return a recipe page, recipe name, and notification's texts."""
        # from pages.new_recipe import configure_action
        recipe_name = self.get_recipe_name()
        current_recipe_action = self.get_selected_action()
        new_recipe_action = self.pick_new_random_action(current_recipe_action)
        self.configure_action(conf, new_recipe_action)
        save_button = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.save_button))
        save_button.click()
        print("recipename ", recipe_name)
        print("newrecipeacton", new_recipe_action)
        return new_recipe_action, self
        # time.sleep(500)

    def select_random_branch_preference(self):
        """Select a random branch preference."""
        from random import choice
        print("entered random branch preference")
        preferences = [True, False]
        random_preference = choice(preferences)
        if random_preference:
            self.find_element(*self.LOCATORS.true_preference).click()
        else:
            self.find_element(*self.LOCATORS.false_preference).click()

    def configure_action(self, conf, recipe_action):
        """Configure action for recipe."""
        action_dropdown = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.action_dropdown))
        action_dropdown.click()
        time.sleep(5)
        if recipe_action == 'console-log':
            console_log = self.wait.until(EC.element_to_be_clickable(
              self.LOCATORS.console_log))
            console_log.click()
            message = conf.get('console_log', 'message')
            self.find_element(*self.LOCATORS.action_message).clear()
            self.find_element(*self.LOCATORS.action_message).send_keys(message)
        if recipe_action == 'show-heartbeat':
            heart_beat = self.wait.until(EC.element_to_be_clickable(
              self.LOCATORS.show_heartbeat))
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
            preference_experiment = self.wait.until(EC.element_to_be_clickable(
              self.LOCATORS.preference_experiment))
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
            self.find_element(*self.LOCATORS.experiment_doc_url).send_keys(
             experiment_doc_url)
            self.find_element(*self.LOCATORS.preference_name).clear()
            self.find_element(*self.LOCATORS.preference_name).send_keys(
             preference_name)
            self.find_element(*self.LOCATORS.add_branch_button).click()
            self.find_element(*self.LOCATORS.branch_name).clear()
            self.find_element(*self.LOCATORS.branch_name).send_keys(
             branch_name)
            self.select_random_branch_preference()

    def click_view_recipe_breadcrumb(self):
        """Click on the view recipe breadcrumb."""
        time.sleep(5)
        from pages.view_recipe import ViewRecipe
        self.find_element(*self.LOCATORS.view_recipe_breadcrumb).click()
        return ViewRecipe(self.selenium, self.base_url).wait_for_page_to_load()
