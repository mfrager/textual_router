"""Run tests"""

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Static

from textual_router import Router, RouterLink


class Home(Static):
    """Basic view"""

    def compose(self):
        """Return view"""

        yield RouterLink(page="about", label="About", id="about_link")


class About(Static):
    """Basic view"""

    def compose(self):
        """Return view"""

        yield RouterLink(page="home", label="Home", id="home_link")


class BasicApp(App):
    """A Textual app to test Router."""

    TITLE = "Basic test app"
    SUB_TITLE = "by imajacket"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Router(
            {
                "home": Home(),
                "about": About(),
            }
        )
        yield Footer()


async def test_links():
    """Test that view updates on link navigation"""

    app = BasicApp()

    async with app.run_test() as pilot:
        await pilot.click("#about_link")
        assert app.query_one("RouterLink").id == "home_link"

        await pilot.click("#home_link")
        assert app.query_one("RouterLink").id == "about_link"
