import json
import unittest
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Base.webdriver_setup import WebDriverSetup
from PageObject.Locators.qualiton_locators import QualitonLocators
from Utilities.maze_handler import MazeSolver
from websocket import create_connection


class ObstacleCourse(WebDriverSetup):
    __author__ = "Nitzan Bachar"
    __version__ = "1.0.0"

    def test_qualiton(self):
        self.main_page()
        self.first_page()
        self.second_page()
        self.third_page()
        self.fourth_page()
        self.fifth_page()
        self.sixth_page()
        self.page_seven()
        sleep(1)

    def main_page(self):
        """
        the first page describing what to do
        :return: nothing
        """
        self.enter_site('http://54.80.137.197:5000/')
        self.click(QualitonLocators.door, By.XPATH, True)
        print("Cleared main page")

    def first_page(self):
        """
        Ahoy page
        :return: nothing
        """
        self.click(QualitonLocators.start_button, By.XPATH, True)
        print("Cleared first page")

    def second_page(self):
        """
        5 buttons page
        :return: nothing
        """
        current_id = 1
        locator = QualitonLocators.general_proceed_btn.replace("$numb", str(current_id))
        print(self.driver.current_url)
        while self.driver.current_url == "http://54.80.137.197:5000/c/c1":
            self.click(locator, By.XPATH, True)
            current_id += 1
            locator = QualitonLocators.general_proceed_btn.replace("$numb", str(current_id))
        print("Cleared the second page")

    def third_page(self):
        """
        youtube page
        :return: nothing
        """
        self.press_play_on_youtube(QualitonLocators.video_player)
        sleep(10)
        self.click(QualitonLocators.mute_button, By.XPATH, False)
        self.switch_back()
        self.click(QualitonLocators.proceed_after_youtube, By.XPATH, True)
        print("Cleared norm youtube page ")

    def fourth_page(self):
        """
        Maze solver
        :return:nothing
        """
        maze_info = self.copy_table(QualitonLocators.maze_id, By.XPATH)
        maze_handler = MazeSolver(maze_info[0], maze_info[1], maze_info[2])
        maze_handler.solve_maze()
        self.click(QualitonLocators.right_btn, By.XPATH, True)
        self.maze_recursion(maze_handler.solution, (maze_info[1])[0], (maze_info[1])[1], maze_info[2],
                            [QualitonLocators.up_btn, QualitonLocators.left_btn, QualitonLocators.down_btn,
                             QualitonLocators.right_btn])
        self.click(QualitonLocators.right_btn, By.XPATH, True)
        self.click(QualitonLocators.right_btn, By.XPATH, True)
        self.click(QualitonLocators.submit_btn, By.XPATH, True)

    def fifth_page(self):
        """
        world map
        :return: nothing
        """
        elem = self.get_element(QualitonLocators.world_map_title, By.XPATH)
        self.send_key(elem, Keys.TAB)
        self.send_key(elem, 'i')
        for i in range(35):
            self.send_key(elem, Keys.ARROW_LEFT)
        for i in range(15):
            self.send_key(elem, Keys.ARROW_UP)
        self.click(QualitonLocators.proceed_after_map, By.XPATH, True)

    def sixth_page(self):
        """
        captcha page

        :return: nothing
        """
        with open('../Utilities/finished_data.json') as json_file:
            data = json.load(json_file)
            src = self.get_element(QualitonLocators.captcha_id, By.XPATH).get_attribute("src")
            input_box = self.get_element(QualitonLocators.captcha_input_box, By.XPATH)
            self.input_text(input_box, data[src])
            self.click(QualitonLocators.captcha_submit_btn, By.XPATH, True)

    def page_seven(self):
        """
        socket page
        :return: nothing
        """
        elem = self.get_element(QualitonLocators.access_token_box, By.XPATH)
        print(elem.text)
        ws = create_connection("ws://54.80.137.197:5001")
        ws.send(elem.text)
        result = ws.recv()
        ws.close()
        input_box = self.get_element(QualitonLocators.token_input_box, By.XPATH)
        self.input_text(input_box, result)
        self.click(QualitonLocators.token_submit_btn, By.XPATH, True)


if __name__ == "__main__":
    unittest.main()
