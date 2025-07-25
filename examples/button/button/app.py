import random

import toga
from toga.constants import BLUE, COLUMN, RED, ROW


class ButtonApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(
            size=(800, 500), resizable=False, minimizable=False
        )

        # Button class
        #   Simple button with text and callback function called when
        #   hit the button
        button1 = toga.Button(
            "Change Text",
            on_press=self.callback_text,
            flex=1,
        )

        # Button with text and enable option
        # Keep a reference to it so it can be enabled by another button.
        self.button2 = toga.Button(
            "Button is disabled!",
            enabled=False,
            flex=1,
            on_press=self.callback_disable,
        )

        # Button with text and style option
        button3 = toga.Button("Bigger", width=200)

        # Button with text and callback function called
        button4a = toga.Button("Make window larger", on_press=self.callback_larger)
        button4b = toga.Button("Make window smaller", on_press=self.callback_smaller)

        # Box class
        # Container of components
        #   Add components for the first row of the outer box
        inner_box1 = toga.Box(
            direction=COLUMN,
            children=[
                button1,
                self.button2,
                button3,
                button4a,
                button4b,
            ],
        )

        # Button with text and margin style
        button5 = toga.Button("Far from home", margin=50, color=BLUE)

        # Button with text and RGB color
        button6 = toga.Button("RGB : Fashion", background_color=RED)

        # Button with text and string color
        button7 = toga.Button("String : Fashion", background_color=BLUE)

        # Button with text and string color
        button8 = toga.Button(
            "Big Font",
            font_family="serif",
            font_size=20,
            font_weight="bold",
        )

        # Button with icon
        button9 = toga.Button(
            icon=toga.Icon("resources/star"),
        )

        # Add components for the second row of the outer box
        inner_box2 = toga.Box(
            direction=COLUMN,
            children=[button5, button6, button7, button8, button9],
        )

        #  Create the outer box with 2 rows
        outer_box = toga.Box(direction=ROW, children=[inner_box1, inner_box2])

        # Add the content on the main window
        self.main_window.content = outer_box

        # Show the main window
        self.main_window.show()

    def callback_text(self, button):
        # Some action when you hit the button
        #   In this case the text will change
        button.text = f"Magic {random.randint(0, 100)}!!"

        # If the disabled button isn't enabled, enable it.
        if not self.button2.enabled:
            self.button2.enabled = True
            self.button2.text = "Disable button"

    def callback_disable(self, button):
        button.enabled = False
        button.text = "Button is disabled!"

    def callback_larger(self, button):
        # Some action when you hit the button
        #   In this case the window size will change
        self.main_window.size = (1000, 600)

    def callback_smaller(self, button):
        # Some action when you hit the button
        #   In this case the window size will change
        self.main_window.size = (200, 200)


def main():
    return ButtonApp("Button", "org.beeware.toga.examples.buttons")


if __name__ == "__main__":
    main().main_loop()
