import time
from TestData import data


def test_letskodeit(helper_obj, practice_page, login_page):
    # Alert
    popup_text = practice_page.click_alert()
    # assert
    helper_obj.write_into_file(popup_text, mode="w")

    # Hide and Show text box
    practice_page.enter_text_box(data.text)
    practice_page.hide_text_box()

    hide_info = practice_page.get_text_box_style()
    helper_obj.write_into_file(hide_info)

    # Mouse hover -ից top
    practice_page.scroll_top()


    footer_text = practice_page.scroll_footer()
    # assert
    helper_obj.write_into_file(footer_text)

    # Sign In -ից Login -ից validation message
    login_page.click_sign_in_login(data.email, data.password)
    incorrect_text = login_page.get_incorrect_text()
    # assert 
    helper_obj.write_into_file(incorrect_text)

    # New tab -ից google.com
    helper_obj.browser.switch_to.new_window("tab")
    helper_obj.browser.get(data.google_url)
    time.sleep(2)

    assert "google" in helper_obj.browser.current_url