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

class simpleFuture:
    def __init__(self, team, outcome, chance, winReturn):
        self.team = team
        self.outcome = outcome
        self.chance = chance
        self.winReturn = winReturn
        self.calculate_odds()
    def calculate_odds(self):
        self.dollarReturn = (self.chance * (self.winReturn - 1) - (1-self.chance))

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

    def add_bet_from_simpleFuture(self, simpleFuture):
        self.addBet(bet("{} to {}".format(simpleFuture.team, simpleFuture.outcome), simpleFuture.dollarReturn))

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

assembler.add_bets_from_simpleWinBet(simpleWinBet("Heat", "Bucks", .49, 2.85, 1.444))
assembler.add_bets_from_simpleWinBet(simpleWinBet("Thunder", "Rockets", .19, 2.95, 1.426))
assembler.add_bets_from_simpleWinBet(simpleWinBet("Raptors", "Celtics", .43, 1.909, 1.909))
assembler.add_bets_from_simpleWinBet(simpleWinBet("Nuggets", "Clippers", .33, 4, 1.286))


assembler.add_bet_from_simpleFuture(simpleFuture("Celtics", "Win the East", .68, 2.5))
assembler.add_bet_from_simpleFuture(simpleFuture("Celtics", "Win the Finals", .35, 6.5))

assembler.add_bet_from_simpleFuture(simpleFuture("Clippers", "Win the West", .51, 2.1))
assembler.add_bet_from_simpleFuture(simpleFuture("Clippers", "Win the Finals", .31, 3.5))

assembler.add_bet_from_simpleFuture(simpleFuture("Rockets", "Win the West", .25, 11))
assembler.add_bet_from_simpleFuture(simpleFuture("Rockets", "Win the Finals", .14, 17))

assembler.add_bet_from_simpleFuture(simpleFuture("Lakers", "Win the West", .19, 2.1))
assembler.add_bet_from_simpleFuture(simpleFuture("Lakers", "Win the Finals", .08, 3.5))

assembler.add_bet_from_simpleFuture(simpleFuture("Heat", "Win the East", .15, 4.75))
assembler.add_bet_from_simpleFuture(simpleFuture("Heat", "Win the Finals", .04, 13))

assembler.add_bet_from_simpleFuture(simpleFuture("Bucks", "Win the East", .10, 2.3))
assembler.add_bet_from_simpleFuture(simpleFuture("Bucks", "Win the Finals", .03, 5))

assembler.add_bet_from_simpleFuture(simpleFuture("Raptors", "Win the East", .07, 11))
assembler.add_bet_from_simpleFuture(simpleFuture("Raptors", "Win the Finals", .02, 25))

assembler.add_bet_from_simpleFuture(simpleFuture("Nuggets", "Win the West", .05, 16))
assembler.add_bet_from_simpleFuture(simpleFuture("Nuggets", "Win the Finals", .02, 31))

assembler.add_bet_from_simpleFuture(simpleFuture("Thunder", "Win the West", .00001, 34))
assembler.add_bet_from_simpleFuture(simpleFuture("Thunder", "Win the Finals", .0000001, 67))

assembler.sort_and_print()
