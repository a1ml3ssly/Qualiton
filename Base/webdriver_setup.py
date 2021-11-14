import unittest
from selenium.webdriver import ActionChains
from Utilities.general_utils import Utilities
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class WebDriverSetup(unittest.TestCase):
    __author__ = "Nitzan Bachar"
    __version__ = "1.0.0"

    def setUp(self):
        ser = Service(Utilities.get_project_root() + "\\Drivers\\Chromedriver.exe")
        self.driver = webdriver.Chrome(service=ser)

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def enter_site(self, site_address):
        self.driver.get(site_address)

    def tearDown(self):
        if self.driver is not None:
            print("Cleccanup of test environment")
            self.driver.close()
            self.driver.quit()

    def click(self, elem_locator, by_what, visible):
        if visible:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by_what, elem_locator)))
        else:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by_what, elem_locator)))
        element.click()

    def send_key(self, element, key):
        ActionChains(self.driver).move_to_element(element).send_keys(key).perform()

    def input_text(self, element, txt):
        element.send_keys(txt)

    def get_element(self, elem_locator, by_what):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by_what, elem_locator)))
        return element

    def press_play_on_youtube(self, iframe_locator):
        required_frame = self.driver.find_element(By.XPATH, iframe_locator)
        self.driver.switch_to.frame(required_frame)
        element = self.driver.find_element(By.XPATH, "//button[@aria-label='Play']")
        element.click()
        print("Successfully pressed play on youtube")

    def is_it_there(self, elem_locator, by_what):
        try:
            self.driver.find_element(by_what, elem_locator)
        except NoSuchElementException:
            return False
        return True

    def switch_back(self):
        self.driver.switch_to.default_content()
        print("Switched back")

    def copy_table(self, elem_locator, by_what):
        new_maze = []
        table = self.driver.find_element(by_what, elem_locator)
        rows = table.find_elements(By.TAG_NAME, "tr")
        current_row = 0
        start_position = []
        finishing_position = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            current_maze_row = []
            for col in cols:
                for attribute in col.get_property('attributes'):
                    if attribute['name'] == 'class':
                        if 'black' in attribute['value']:
                            current_maze_row.append(0)
                        elif 'blue-grey' in attribute['value']:
                            current_maze_row.append(1)
            if current_maze_row != []:
                new_maze.append(current_maze_row)
            current_row += 1

        for i in range(len(new_maze)):
            for j in range(len(new_maze[i])):
                if j == 0 and new_maze[i][j] == 1:
                    start_position = [i, j]
                if j == 9 and new_maze[i][j] == 1:
                    finishing_position = [i, j]

        return [new_maze, start_position, finishing_position]

    def walk_the_walk(self, solved_maze, starting_pos, finishing_position, pos_arr):
        # up = 0
        # left = 1
        # down = 2
        # right = 3
        self.click(pos_arr[3], By.XPATH, True)
        self.maze_recursion(solved_maze, starting_pos[0], starting_pos[1], finishing_position, pos_arr)
        self.click(pos_arr[3], By.XPATH, True)
        self.click(pos_arr[3], By.XPATH, True)

    def maze_recursion(self, maze, x, y, finishing_position, pos_arr):
        if 0 <= x <= 9 and 0 <= y <= 9:
            if x != finishing_position[0] or y != finishing_position[1]:
                maze[x][y] = 0
                if x + 1 <= 9:
                    if maze[x + 1][y] == 1:
                        self.click(pos_arr[2], By.XPATH, True)
                        self.maze_recursion(maze, x + 1, y, finishing_position, pos_arr)
                if x - 1 >= 0:
                    if maze[x - 1][y] == 1:
                        self.click(pos_arr[0], By.XPATH, True)
                        self.maze_recursion(maze, x - 1, y, finishing_position, pos_arr)
                if y + 1 <= 9:
                    if maze[x][y + 1] == 1:
                        self.click(pos_arr[3], By.XPATH, True)
                        self.maze_recursion(maze, x, y + 1, finishing_position, pos_arr)
                if y - 1 >= 0:
                    if maze[x][y - 1] == 1:
                        self.click(pos_arr[1], By.XPATH, True)
                        self.maze_recursion(maze, x, y - 1, finishing_position, pos_arr)
            else:
                self.click(pos_arr[3], By.XPATH, True)
