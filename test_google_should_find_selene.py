from selene import browser, be, have


def test_google_should_search_selen():
    browser.open('https://google.com/')
    browser.element('[name=q]').should(be.blank).type('yashaka/selen').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User oriented Web UI browser tests in Python'))

def test_google_should_search_nothing():
    browser.open('https://google.com/')
    browser.element('[name=q]').should(be.blank).type('!@#$%^&*(0asDfsdfdsvjwq').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))

