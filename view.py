from dash_core_components import Dropdown, Slider, Textarea
from dash_html_components import Br, Button, Div, P, Table, Td, Tr

class view():

    
    def __init__(self):

        ROWS = 10
        VARS_COLS = 50

        # variables

        variables_cell = Td(
            id = "variables_control_cell",
            children = [
                Textarea(
                    id = "variables_text",
                    rows = ROWS,
                    cols = VARS_COLS
                ),
                Br(),
                Button(
                    id = "submit",
                    children = "submit"
                )
            ]
        )

        variables_row = Tr(
            id = "variables_row",
            children = [
                variables_cell
            ]
        )

        # time

        self.time_slider = Slider(
            id = "time_slider",
            min = 0,
            max = 252,
            step = 1,
            value = 0,
            updatemode = "drag"
        )

        time_cell = Td(
            id = "time_slider_cell",
            children = [
                Div(
                    id = "time_view",
                    children = [
                        P(
                            id = "time_label",
                            children = [
                                f"time: 0"
                            ]
                        ),
                        self.time_slider
                    ]
                )
            ]
        )

        time_row = Tr(
            id = "time_slider_row",
            children = [ time_cell ]
        )

        # mode

        mode_cell = Td(
            id = "mode_cell",
            children = [
                P(
                    id = "mode_label",
                    children = [
                        "mode"
                    ]
                ),
                Dropdown(
                    id = "mode_dropdown",
                    options = [
                        {
                            "label": "pnl", "value": "pnl"
                        },
                        {
                            "label": "value", "value": "value"
                        }
                    ],
                    value = "value"
                )
            ]
        )

        mode_row = Tr(
            id = "mode_row",
            children = [ mode_cell ]
        )

        # payoff

        payoff_cell = Td(
            id = "chart_cell",
            colSpan = 2,
            children = [
                Div(
                    id = "payoff_chart_view",
                    children = []
                )
            ]
        )

        # table

        controls = Table(
            id = "controls_table",
            children = [
                mode_row,
                time_row,
                variables_row
            ]
        )

        self.layout = Table(
            id = "app_view",
            children = [
                Tr(
                    children = [
                        Td(
                            children = [ controls ]
                        ),
                        payoff_cell
                    ]
                )
            ]
        )


    def get_layout(self):                           return self.layout
    def get_time_view(self):                        return self.time_view
    
    def set_time_view(self, time_view: Div):        self.time_view = time_view