### Configuration

This application uses plotly dash, which runs through a webserver. You will need to pick a port and hostname, or use the defaults in `config.json`.

If using the default settings:

1. Run the application with `python app.py`.
2. Visit `localhost:8030` in your browser.

### Usage

View the profit and loss for a portfolio of options. Define the portfolio using the text box. The syntax is:

```
<underlying>  <price>
<underlying>:<dte>:[PC]<strike>  <iv>,<qty>
```

For example, a call butterfly for ticker "AR":

```
AR            18.44
AR:36:C17     0.13,-1
AR:36:C18     0.14,+2
AR:36:C19     0.15,-1
time          20
rate          0.0050
```

![example output](https://github.com/toobrien/payoff/blob/master/example.png?raw=true)

In this example, the underlying ("AR") is priced at 18.44. The three options all have 36 days to expiration, at strikes 17, 18, and 19. Their implied volatilities are, respectively 13%, 14%, 15%. The 17 and 19 calls are short, the 18 call is long (2 contracts).

The `time` and `rate` are optional. After clicking `submit` to render the payoff graph, you can also set `time` using the slider. Known issue: dragging the slider too fast will break the graph.

You can plot as many underlyings and options as you would like. However, the strikes in the payoff graph only refer to the underlying for the option nearest expiration.

Note that the ticker is arbitrary; it is only used to identify the underlying for each option.

When changing any thing in the text box, click `submit` to show the changes.

The `mode` dropdown also refreshes the graph. When `value` is selected, the payoff graph does not include the option's initial price (which is determined from its IV). When `pnl` is selected, the payoff includes the option's price. 
