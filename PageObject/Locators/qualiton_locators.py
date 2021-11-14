class QualitonLocators:
    """
    Contain all the ids and Xpaths for all the objects required for this test

    """
    __author__ = "Nitzan Bachar"
    __version__ = "1.0.0"

    # Starter Page
    door = "//a[@href ='/intro']"
    # Ahoy Mateys - page 1
    start_button = "//button[@id='start']"
    # Proceed Button - page 2
    general_proceed_btn = "//button[@id='c1submitbutton$numb']"

    # A video Player
    video_player = "//iframe[@id='aVideoPlayer']"
    mute_button = "//button[@aria-label='Mute (m)']"
    proceed_after_youtube = "//button[@id='aVideoSubmit']"
    # Maze page - third page
    maze_id = "//table[@id='maze']"
    up_btn = "//a[@onclick='up();']"
    left_btn = "//a[@onclick='left();']"
    down_btn = "//a[@onclick='down();']"
    right_btn = "//a[@onclick='right();']"
    submit_btn = "//button[@id='crystalMazeFormSubmit']"
    # world map page - fourth page
    world_map_title = "//div[@class='card maincard']"
    proceed_after_map = "//button[@id='mapsChallengeSubmit']"
    # captcha
    captcha_id = "//img[@id='notABotCaptchaImg']"
    captcha_input_box = "//input[@id='notABotCaptchaResponse']"
    captcha_submit_btn = "//button[@id='notABotCaptchaSubmit']"
    # Token
    access_token_box = "//div[@class='yellow lighten-3']"
    token_input_box = "//input[@id='socketGateMessage']"
    token_submit_btn = "//button[@class='btn deep-orange darken-4']"
