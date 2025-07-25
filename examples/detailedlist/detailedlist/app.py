import asyncio

import toga
from toga.constants import COLUMN, ROW

from .translations import bee_translations


class DetailedListApp(toga.App):
    # Detailed list callback functions
    def on_select_handler(self, widget, **kwargs):
        row = widget.selection
        self.label.text = (
            f"Bee is {getattr(row, 'title', '')} in {getattr(row, 'subtitle', '')}"
            if row is not None
            else "No row selected"
        )

    def on_refresh_switch(self, switch):
        self.dl.on_refresh = self.on_refresh_handler if switch.value else None

    def on_delete_switch(self, switch):
        self.dl.on_primary_action = self.on_delete_handler if switch.value else None

    def on_visit_switch(self, switch):
        self.dl.on_secondary_action = self.on_visit_handler if switch.value else None

    async def on_refresh_handler(self, widget, **kwargs):
        self.label.text = "Refreshing list..."
        # We are using a local data source, so there's literally no reason
        # to use refresh. However, for demonstration purposes, lets pretend
        # that we're getting the data from an API, which takes 1s to respond.
        await asyncio.sleep(1)
        self.label.text = "List was refreshed."

    def on_delete_handler(self, widget, row, **kwargs):
        self.dl.data.remove(row)

    def on_visit_handler(self, widget, row, **kwargs):
        self.label.text = "We're not a travel agent."

    # Button callback functions
    def insert_handler(self, widget, **kwargs):
        item = {"icon": None, "subtitle": "The Hive", "title": "Bzzz!"}
        if self.dl.selection:
            index = self.dl.data.index(self.dl.selection) + 1
            self.dl.data.insert(index, item)
        else:
            index = len(self.dl.data)
            self.dl.data.append(item)
        self.dl.scroll_to_row(index)

    def remove_handler(self, widget, **kwargs):
        if self.dl.selection:
            self.dl.data.remove(self.dl.selection)

    def startup(self):
        # Set up main window
        self.main_window = toga.MainWindow()

        # Buttons
        btn_style = {"flex": 1, "margin": 10}
        self.btn_insert = toga.Button(
            "Insert Row", on_press=self.insert_handler, **btn_style
        )
        self.btn_remove = toga.Button(
            "Remove Row", on_press=self.remove_handler, **btn_style
        )
        self.btn_box = toga.Box(
            children=[self.btn_insert, self.btn_remove], direction=ROW
        )

        # Switches to enable/disable actions
        self.switch_box = toga.Box(
            direction=ROW,
            children=[
                toga.Box(flex=1),  # Spacer
                toga.Switch(
                    "Delete",
                    value=True,
                    on_change=self.on_delete_switch,
                    margin=10,
                ),
                toga.Switch(
                    "Visit",
                    value=True,
                    on_change=self.on_visit_switch,
                    margin=10,
                ),
                toga.Switch(
                    "Refresh",
                    value=True,
                    on_change=self.on_refresh_switch,
                    margin=10,
                ),
                toga.Box(flex=1),  # Spacer
            ],
        )

        # Label to show responses.
        self.label = toga.Label("Ready.")

        self.dl = toga.DetailedList(
            data=[
                {},  # Missing values
                {"icon": None, "title": None, "subtitle": None},  # None values
            ]
            + [
                {
                    "icon": toga.Icon("resources/brutus.png"),
                    "title": translation["string"],
                    "subtitle": translation["country"],
                }
                for translation in bee_translations
            ],
            missing_value="MISSING",
            on_select=self.on_select_handler,
            on_primary_action=self.on_delete_handler,
            secondary_action="Visit",
            on_secondary_action=self.on_visit_handler,
            on_refresh=self.on_refresh_handler,
            flex=1,
        )

        # Outermost box
        outer_box = toga.Box(
            children=[self.btn_box, self.switch_box, self.dl, self.label],
            flex=1,
            direction=COLUMN,
            margin=10,
        )

        # Add the content on the main window
        self.main_window.content = outer_box

        # Show the main window
        self.main_window.show()


def main():
    return DetailedListApp("Detailed List", "org.beeware.toga.examples.detailedlist")


if __name__ == "__main__":
    main().main_loop()
