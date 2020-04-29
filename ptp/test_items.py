
def test_add_to_basket_button_visible(browser):
    assert browser.find_element_by_class_name("btn-add-to-basket"), "Add to basket button not found"
