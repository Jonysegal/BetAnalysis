class simpleWinBet:
    def __init__(
        self, teamOne, teamTwo, teamOneChance, teamOneWinReturn, teamTwoWinReturn
    ):
        self.teamOne = teamOne
        self.teamTwo = teamTwo
        self.teamOneChance = teamOneChance
        self.teamTwoChance = 1 - teamOneChance
        self.teamOneWinReturn = teamOneWinReturn
        self.teamTwoWinReturn = teamTwoWinReturn
        self.calculate_odds()

    def calculate_odds(self):
        self.teamOneDollarReturn = (
            self.teamOneChance * (self.teamOneWinReturn - 1)
        ) - (1 - self.teamOneChance)
        self.teamTwoDollarReturn = (
            (1 - self.teamOneChance) * (self.teamTwoWinReturn - 1)
        ) - (self.teamOneChance)

    def print_odds(self):
        print(
            "Every dollar put on {} beating {} generates ${} of return".format(
                self.teamOne, self.teamTwo, self.teamOneDollarReturn
            )
        )
        print(
            "Every dollar put on {} beating {} generates ${} of return".format(
                self.teamTwo, self.teamOne, self.teamTwoDollarReturn
            )
        )


class bet:
    def __init__(self, description, dollarReturn):
        self.description = description
        self.dollarReturn = dollarReturn


class betAssembler:
    def __init__(self):
        self.bets = []

    def addBet(self, bet):
        self.bets.append(bet)

    def add_bets_from_simpleWinBet(self, simpleWinBet):
        x = bet(
            "{} to beat {}".format(simpleWinBet.teamOne, simpleWinBet.teamTwo),
            simpleWinBet.teamOneDollarReturn,
        )
        self.addBet(x)
        y = bet(
            "{} to beat {}".format(simpleWinBet.teamTwo, simpleWinBet.teamOne),
            simpleWinBet.teamTwoDollarReturn,
        )
        self.addBet(y)

    def sort_and_print(self):
        self.sort_bets()
        self.print_bets()

    def sort_bets(self):
        self.bets.sort(key=lambda bet: bet.dollarReturn)

    def print_bets(self):
        for bet in self.bets:
            print(
                "Will get ${} per dollar bet by betting {}".format(
                    bet.dollarReturn, bet.description
                )
            )


assembler = betAssembler()

assembler.add_bets_from_simpleWinBet(simpleWinBet("Heat", "Bucks", .45, 2.7, 1.5))
assembler.add_bets_from_simpleWinBet(simpleWinBet("Celtics", "Raptors", .59, 1.952, 1.87))
assembler.add_bets_from_simpleWinBet(simpleWinBet("Jazz", "Nuggets", .44, 2, 1.833))


assembler.sort_and_print()
