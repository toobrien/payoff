from black_scholes import price
from sys import maxsize
from typing import List

DEFAULT_RATE = 0.0060
DAYS_PER_YEAR = 365

class leg():


    def __init__(
        self,
        call: bool,
        cost: float,
        time: float,
        iv: float,
        long: bool,
        quantity: int,
        strike: float,
        underlying: str,
    ):

        self.call = call
        self.cost = cost
        self.time = time
        self.iv = iv
        self.long = long
        self.quantity = quantity
        self.strike = strike
        self.underlying = underlying


class model():


    def __init__(self):

        self.legs = None
        self.mode = None
        self.underlyings = None
        self.time = None
        self.rate = DEFAULT_RATE


    '''
    format:

        rate                        <discount rate>
        time                        <days>
        <underlying>                <price>
        <underlying>:<dte>:[PC]<strike>   <iv>,[+-]<qty>

    '''
    def set_variables(
        self,
        variables: str
    ):

        self.legs = {}
        self.underlyings = {}

        time_set = False

        variables = variables.split("\n")
        
        legs = []

        for var in variables:

            parts = var.split()

            if parts[0] == "rate":

                self.rate = float(parts[1])

            elif parts[0] == "time":

                time_set = True
                self.time = float(parts[1])

            elif ":" not in var:

                # underlying

                self.underlyings[parts[0]] = float(parts[1])

            else:

                # leg, save for later
                # all underlyings should be defined first

                legs.append((parts[0], parts[1]))

        # finish legs
        # ("<symbol>:[PC]<strike>", "<iv>,<time>,<qty>")

        min_time = maxsize

        for leg_ in legs:

            id, vars = leg_
        
            parts = id.split(":")

            underlying = parts[0]
            time = float(parts[1])
            call = parts[2][0] == "C"
            strike = float(parts[2][1:])

            parts = vars.split(",")

            iv = float(parts[0])
            quantity = float(parts[1])
            long = parts[1][0] != "-"

            cost = price(
                call,
                self.underlyings[underlying],
                strike,
                time / DAYS_PER_YEAR,
                iv,
                self.rate
            )

            self.legs[id] = leg(
                call,
                cost * quantity,
                time,
                iv,
                long,
                quantity,
                strike,
                underlying
            )

            if time < min_time: min_time = time

        if not time_set: self.time = time
        self.max_time = min_time




    def get_legs(self):                             return self.legs
    def get_max_time(self):                         return self.max_time
    def get_rate(self):                             return self.rate
    def get_time(self):                             return self.time
    def get_underlyings(self):                      return self.underlyings

    def set_legs(self, legs: List[leg]):            self.legs = legs
    def set_max_time(self, time: float):            self.max_time = time
    def set_rate(self, rate: float):                self.rate = rate
    def set_time(self, time: float):                self.time = time
    def set_underlyings(self, underlyings: dict):   self.underlyings = underlyings