from dash import Dash, callback_context
from dash_core_components import Graph, Slider
from dash_html_components import Div, P
from dash.dependencies import Input, Output, State
from json import loads
from model import model
from payoff import get_payoff_graph
from typing import List, Tuple
from view import view


# GLOBALS

app = Dash(__name__, title = "payoff_2")
model_ = model()
view_ = view()

app.layout = view_.get_layout()

DEBUG = False


# FUNCTIONS

def debug(dash_decorator):

    def decorator(func):

        if DEBUG: return func
        else:     return dash_decorator(func)

    return decorator


@debug(
    app.callback(
        Output("payoff_chart_view", "children"),
        Output("time_label", "children"),
        Input("mode_dropdown", "value"),
        Input("time_slider", "value"),
        prevent_initial_call = True
    )
)
def set_time_and_payoff_graph(
    mode: str,
    time: float
) -> Tuple[List[Graph], str]:

    payoff_graph = [ 
        get_payoff_graph(
            "payoff_chart",
            model_.get_legs(),
            mode,
            model_.get_rate(),
            time,
            model_.get_underlyings(),
        )
    ]

    return payoff_graph, f"time: {time}"


@debug(
    app.callback(
        Output("time_view", "children"),
        Input("submit", "n_clicks"),
        State("variables_text", "value"),
        prevent_initial_call = True
    )
)
def submit(
    _,
    variables_text: str
) -> Tuple[str, List[Div]]:

    model_.set_variables(variables_text)
    
    time = model_.get_time()
    max_time = model_.get_max_time()
    
    time_view = Div(
        id = "time_view",
        children = [
            P(
                id = "time_label",
                children = [
                    f"time ({time})"
                ]
            ),
            Slider(
                    id = "time_slider",
                    min = 0,
                    max = max_time,
                    step = 1,
                    value = time,
                    updatemode = "drag"
                )
        ]
        )

    view_.set_time_view(time_view)

    return time_view


# MAIN

if __name__ == "__main__":

    with open("./config.json") as fd:

        config = loads(fd.read())

        if DEBUG:

            submit(
                None,
                "\n".join(
                    [
                        "SPX 4782.71",
                        "SPX:10:C4780 0.14,-1",
                        "SPX:10:P4780 0.14,-1"
                    ]
                )
            )

            set_time_and_payoff_graph(
                "value",
                0
            )

        else:

            app.run_server(
                host = config["dash_host"],
                port = config["dash_port"], 
                debug = False,
                dev_tools_hot_reload = False
            )