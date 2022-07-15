from selenium.webdriver.common.by import By


class BasePage:
    TITLE_PAGE = (By.XPATH, "//div[contains(@class,'k1zIA rSk4se')]//img[contains(@alt,'Google')]")
    SEARCH_FIELD = (By.XPATH, "//input[contains(@title,'Поиск')]")
