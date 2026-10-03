import re

from playwright.sync_api import Page, expect

# pytest-playwright gives each test a fresh browser tab via the `page` fixture.
# books.toscrape.com is a fake bookshop built for practising automation.

BOOKSHOP = "https://books.toscrape.com/"


def test_homepage_has_title(page: Page):
    page.goto(BOOKSHOP)
    expect(page).to_have_title(re.compile("All products"))


def test_homepage_shows_20_books(page: Page):
    page.goto(BOOKSHOP)
    expect(page.locator("article.product_pod")).to_have_count(20)


def test_open_category(page: Page):
    page.goto(BOOKSHOP)
    page.get_by_role("link", name="Travel").click()
    expect(page.get_by_role("heading", level=1)).to_have_text("Travel")
    expect(page).to_have_url(re.compile("travel"))


def test_open_book_details(page: Page):
    page.goto(BOOKSHOP)
    page.get_by_role("link", name="A Light in the Attic").click()
    expect(page.get_by_role("heading", level=1)).to_have_text("A Light in the Attic")
    expect(page.locator(".product_main .price_color")).to_have_text("£51.77")


def test_next_page(page: Page):
    page.goto(BOOKSHOP)
    page.get_by_role("link", name="next").click()
    expect(page.locator("li.current")).to_contain_text("Page 2 of 50")
