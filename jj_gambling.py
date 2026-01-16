import random, time, colourTheory as cT

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = '23456789TJQKA'
RANK_TO_VALUE = {r: i for i, r in enumerate(RANKS, start=2)}

def card_to_str(card):
    """Return a readable string for cards"""
    r, s = card
    return f"{r}{s}"

def make_deck():
    """Create a standard 52-card deck with ranks and suits."""
    return [(r, s) for r in RANKS for s in SUITS]

def card_value(card):
    """Return the numeric value of a card's rank."""
    r, _ = card
    return RANK_TO_VALUE[r]

class PokerGame:
    def __init__(self):
        self.balances = [1000, 1000, 1000, 1000]

        while True:
            for a in range(50):
                print()
                time.sleep(0.01)
            cT.print_colour(self.balances, "black")
            self.deck = []
            self.hands = []
            self.need_to_pay = [0, 0, 0, 0]
            self.prize_pot = 0
            self.deck = make_deck()
            random.shuffle(self.deck)

            for a in self.balances:
                if a < 0:
                    cT.print_colour("\nTable Over: Come Back Soon", "blue")
                    time.sleep(5)
                    print(5/0)
            self.balances = self.deal_to_players()
            time.sleep(2)


    def _deal_one(self):
        return self.deck.pop()

    def _format_hand(self, hand):
        """Return a short, readable representation of a hand (list of cards)."""
        return ", ".join(card_to_str(c) for c in hand)

    def _output_preflop(self):
        player_hand = self.hands[0]
        robot_hand = self.hands[1]
        robot_hand2 = self.hands[2]
        robot_hand3 = self.hands[3]

        player_hand_str = f"{player_hand[0]}{player_hand[1]}" if False else self._format_hand(player_hand)

        player_hand_str = self._format_hand(player_hand)
        robot_hand_str = self._format_hand(robot_hand)
        robot_hand2_str = self._format_hand(robot_hand2)
        robot_hand3_str = self._format_hand(robot_hand3)

        cT.print_colour(f"You: {player_hand_str}", "magenta")
        return player_hand_str, robot_hand_str, robot_hand2_str, robot_hand3_str


    def deal_to_players(self, num_players: int = 4, cards_each: int = 2):
        """Deal initial hands and run the first betting round (simplified)."""

        self.hands = [[] for _ in range(num_players)]
        total_cards = num_players * cards_each

        for i in range(total_cards):
            player_index = i % num_players
            self.hands[player_index].append(self.deck.pop())

        player, dealer, small_bind, big_bind = self._output_preflop()

        self.balances[2] -= 2
        self.balances[3] -= 5
        self.prize_pot = 7
        self.need_to_pay = [5, 5, 3, 0]

########################################################### PREFLOP ##############################################################
        
        # Player action
        cT.print_colour(f"To Call: {self.need_to_pay[0]} | Your balance: {self.balances[0]}", "white")
        action = input("What action do you want to do: call/fold/raise: ").strip().lower()
        if action == "raise":
            try: amount = int(input("What amount are you raising by: "))
            except: amount = -1
            if 0 < amount < self.balances[0]:
                self._apply_raise(amount)
            else:
                self._apply_call_or_fold_zero()
        elif action == "fold":
            self.need_to_pay[0] = -1
        else:
            self._apply_call_or_fold_zero()

        print()

        # Dealer
        time.sleep(random.randint(1, 3))
        self._simulate_opponents_round(1, self.need_to_pay[1])

        # Small Bind
        time.sleep(random.random())
        self._simulate_opponents_round(2,  self.need_to_pay[2])

        # Big Blind
        if self.need_to_pay[3] > 0:
            time.sleep(random.randint(1, 3))
            self._simulate_opponents_round(3,  self.need_to_pay[3])
        
        while not (self.need_to_pay[0] < 0.1 and
               self.need_to_pay[1] < 0.1 and
               self.need_to_pay[2] < 0.1 and
               self.need_to_pay[3] < 0.1):
            for idx in range(0, 4):
                if self.need_to_pay[idx] > 0:
                    if idx == 0:
                        cT.print_colour(f"To Call: {self.need_to_pay[0]} | Your balance: {self.balances[0]}", "white")
                        action = input("What action do you want to do: call/fold/raise: ").strip().lower()
                        if action == "raise":
                            amount = int(input("What amount are you raising by: "))
                            if 0 < amount < self.balances[0]:
                                self._apply_raise(amount)
                            else:
                                self._apply_call_or_fold_zero()
                        elif action == "fold":
                            self.need_to_pay[0] = -1
                        else:
                            self._apply_call_or_fold_zero()
                    else:
                        time.sleep(random.randint(1, 3))
                        self._simulate_opponents_round(idx,  self.need_to_pay[idx])


        print()
        cT.print_colour(f"Left in Game: {", ".join(self.return_in_game())}", "black")
        cT.print_colour(f"Prizepot: {self.prize_pot}", "black")
        cT.print_colour(f"Money: {self.balances}", "black")
        print()

        self._deal_community_cards(num_players=1, cards_each=3, label="Flop", color="yellow")

########################################################### FLOP ##############################################################
        
        print()

        # Small Bind
        if self.need_to_pay[2] > -1:
            time.sleep(2*random.random())
            self._simulate_opponents_round(2,  self.need_to_pay[2])

        # Big Blind
        if self.need_to_pay[3] > -1:
            time.sleep(random.randint(0, 3))
            self._simulate_opponents_round(3,  self.need_to_pay[3])

        # Player action
        if self.need_to_pay[0] > -1:
            cT.print_colour(f"To Call: {self.need_to_pay[0]} | Your balance: {self.balances[0]}", "white")
            action = input("What action do you want to do: call/fold/raise: ").strip().lower()
            if action == "raise":
                amount = int(input("What amount are you raising by: "))
                if 0 < amount < self.balances[0]:
                    self._apply_raise(amount)
                else:
                    self._apply_call_or_fold_zero()
            elif action == "fold":
                self.need_to_pay[0] = -1
            else:
                self._apply_call_or_fold_zero()


        # Dealer
        if self.need_to_pay[1] > -1:
            time.sleep(random.randint(2, 6))
            self._simulate_opponents_round(1, self.need_to_pay[1])

        # Small Bind
        if self.need_to_pay[2] > 0:
            time.sleep(random.randint(1, 3))
            self._simulate_opponents_round(2,  self.need_to_pay[2])

        # Big Blind
        if self.need_to_pay[3] > 0:
            time.sleep(2*random.random())
            self._simulate_opponents_round(3,  self.need_to_pay[3])
        
        while (not (self.need_to_pay[0] < 0.1 and
               self.need_to_pay[1] < 0.1 and
               self.need_to_pay[2] < 0.1 and
               self.need_to_pay[3] < 0.1)):
            for idx in range(0, 4):
                if self.need_to_pay[idx] > 0:
                    if idx == 0:
                        cT.print_colour(f"To Call: {self.need_to_pay[0]} | Your balance: {self.balances[0]}", "white")
                        action = input("What action do you want to do: call/fold/raise: ").strip().lower()
                        if action == "raise":
                            amount = int(input("What amount are you raising by: "))
                            if 0 < amount < self.balances[0]:
                                self._apply_raise(amount)
                            else:
                                self._apply_call_or_fold_zero()
                        elif action == "fold":
                            self.need_to_pay[0] = -1
                        else:
                            self._apply_call_or_fold_zero()
                    else:
                        time.sleep(random.randint(1, 3))
                        self._simulate_opponents_round(idx,  self.need_to_pay[idx])


        print()
        cT.print_colour(f"Left in Game: {", ".join(self.return_in_game())}", "black")
        cT.print_colour(f"Prizepot: {self.prize_pot}", "black")
        cT.print_colour(f"Money: {self.balances}", "black")
        print()

        # Turn
        self._deal_community_cards(num_players=1, cards_each=1, label="Turn", color="red")
        print()

########################################################### TURN ##############################################################

        # Small Bind
        if self.need_to_pay[2] > -1:
            time.sleep(random.randint(1, 3))
            self._simulate_opponents_round(2,  self.need_to_pay[2])

        # Big Blind
        if self.need_to_pay[3] > -1:
            time.sleep(random.randint(1, 3))
            self._simulate_opponents_round(3,  self.need_to_pay[3])

        # Player action
        if self.need_to_pay[0] > -1:
            cT.print_colour(f"To Call: {self.need_to_pay[0]} | Your balance: {self.balances[0]}", "white")
            action = input("What action do you want to do: call/fold/raise: ").strip().lower()
            if action == "raise":
                amount = int(input("What amount are you raising by: "))
                if 0 < amount < self.balances[0]:
                    self._apply_raise(amount)
                else:
                    self._apply_call_or_fold_zero()
            elif action == "fold":
                self.need_to_pay[0] = -1
            else:
                self._apply_call_or_fold_zero()

        time.sleep(random.randint(1, 3))

        # Dealer
        if self.need_to_pay[1] > -1:
            self._simulate_opponents_round(1, self.need_to_pay[1])

        # Small Bind
        if self.need_to_pay[2] > 0:
            time.sleep(random.randint(1, 3))
            self._simulate_opponents_round(2,  self.need_to_pay[2])

        # Big Blind
        if self.need_to_pay[3] > 0:
            time.sleep(random.randint(1, 3))
            self._simulate_opponents_round(3,  self.need_to_pay[3])
        
        while (not (self.need_to_pay[0] < 0.1 and
               self.need_to_pay[1] < 0.1 and
               self.need_to_pay[2] < 0.1 and
               self.need_to_pay[3] < 0.1)):
            for idx in range(0, 4):
                if self.need_to_pay[idx] > 0:
                    if idx == 0:
                        cT.print_colour(f"To Call: {self.need_to_pay[0]} | Your balance: {self.balances[0]}", "white")
                        action = input("What action do you want to do: call/fold/raise: ").strip().lower()
                        if action == "raise":
                            amount = int(input("What amount are you raising by: "))
                            if 0 < amount < self.balances[0]:
                                self._apply_raise(amount)
                            else:
                                self._apply_call_or_fold_zero()
                        elif action == "fold":
                            self.need_to_pay[0] = -1
                        else:
                            self._apply_call_or_fold_zero()
                    else:
                        time.sleep(random.randint(1, 3))
                        self._simulate_opponents_round(idx,  self.need_to_pay[idx])

        print()
        cT.print_colour(f"Left in Game: {", ".join(self.return_in_game())}", "black")
        cT.print_colour(f"Prizepot: {self.prize_pot}", "black")
        cT.print_colour(f"Money: {self.balances}", "black")
        print()

        # River
        self._deal_community_cards(num_players=1, cards_each=1, label="River", color="cyan")
        print()

########################################################### RIVER ##############################################################

        # Small Bind
        if self.need_to_pay[2] > -1:
            time.sleep(random.randint(1, 3))
            self._simulate_opponents_round(2,  self.need_to_pay[2])

        # Big Blind
        if self.need_to_pay[3] > -1:
            time.sleep(2*random.random())
            self._simulate_opponents_round(3,  self.need_to_pay[3])

        # Player action
        if self.need_to_pay[0] > -1:
            cT.print_colour(f"To Call: {self.need_to_pay[0]} | Your balance: {self.balances[0]}", "white")
            action = input("What action do you want to do: call/fold/raise: ").strip().lower()
            if action == "raise":
                amount = int(input("What amount are you raising by: "))
                if 0 < amount < self.balances[0]:
                    self._apply_raise(amount)
                else:
                    self._apply_call_or_fold_zero()
            elif action == "fold":
                self.need_to_pay[0] = -1
            else:
                self._apply_call_or_fold_zero()

        # Dealer
        if self.need_to_pay[1] > -1:
            time.sleep(3*random.random())
            self._simulate_opponents_round(1, self.need_to_pay[1])

        # Small Bind
        if self.need_to_pay[2] > 0:
            time.sleep(random.randint(1, 2))
            self._simulate_opponents_round(2,  self.need_to_pay[2])

        # Big Blind
        if self.need_to_pay[3] > 0:
            time.sleep(random.randint(0, 4))
            self._simulate_opponents_round(3,  self.need_to_pay[3])
        
        while (not (self.need_to_pay[0] < 0.1 and
               self.need_to_pay[1] < 0.1 and
               self.need_to_pay[2] < 0.1 and
               self.need_to_pay[3] < 0.1)):
            for idx in range(0, 4):
                if self.need_to_pay[idx] > 0:
                    if idx == 0:
                        cT.print_colour(f"To Call: {self.need_to_pay[0]} | Your balance: {self.balances[0]}", "white")
                        action = input("What action do you want to do: call/fold/raise: ").strip().lower()
                        if action == "raise":
                            amount = int(input("What amount are you raising by: "))
                            if 0 < amount < self.balances[0]:
                                self._apply_raise(amount)
                            else:
                                self._apply_call_or_fold_zero()
                        elif action == "fold":
                            self.need_to_pay[0] = -1
                        else:
                            self._apply_call_or_fold_zero()
                    else:
                        time.sleep(random.randint(1, 3))
                        self._simulate_opponents_round(idx,  self.need_to_pay[idx])

        print()
        cT.print_colour(f"Left in Game: {", ".join(self.return_in_game())}", "black")
        cT.print_colour(f"Prizepot: {self.prize_pot}", "black")
        cT.print_colour(f"Money: {self.balances}", "black")
        print()

########################################################### END ##############################################################
        time.sleep(0.1)

        if self.return_in_game() == ["Dealer"]: winner = "dealer"
        elif self.return_in_game() == ["Small Bind"]: winner = "small"
        elif self.return_in_game() == ["Big Bind"]: winner = "big"
        elif self.return_in_game() == ["Player"]: winner = "player"
        else:
            if self.need_to_pay[0] > -1: cT.print_colour(f"\nYour Hand: {player}", "green")
            if self.need_to_pay[1] > -1: cT.print_colour(f"Dealer: {dealer}", "green")
            if self.need_to_pay[2] > -1: cT.print_colour(f"Small Bind: {small_bind}", "green")
            if self.need_to_pay[3] > -1: cT.print_colour(f"Big Blind: {big_bind}", "green")

            winner = cT.input_colour("Winner: player/dealer/small/big: ", "blue").lower()
        if winner == "player": self.balances[0] += self.prize_pot
        elif winner == "dealer": self.balances[1] += self.prize_pot
        elif winner == "small": self.balances[2] += self.prize_pot
        elif winner == "big": self.balances[3] += self.prize_pot

        cT.print_colour(f"\nWell Done for Winning {winner}", "green")
        return self.balances
    
    def return_in_game(self):
        left = []
        if self.need_to_pay[0] > -1: left.append("Player")
        if self.need_to_pay[1] > -1: left.append("Dealer")
        if self.need_to_pay[2] > -1: left.append("Small Bind")
        if self.need_to_pay[3] > -1: left.append("Big Bind")
        return left

    def _apply_raise(self, amount):
        """Handle a raise by the user on the preflop round."""
        self.balances[0] -= self.need_to_pay[0]
        self.balances[0] -= amount
        self.prize_pot += self.need_to_pay[0] + amount
        for idx in range(4):
            if self.need_to_pay[idx] > -1:
                self.need_to_pay[idx] += amount
        self.need_to_pay[0] = 0

    def _apply_call_or_fold_zero(self):
        """Default action when user calls or folds (simplified)."""
        self.balances[0] -= self.need_to_pay[0]
        self.prize_pot += self.need_to_pay[0]
        self.need_to_pay[0] = 0

######################################################### ROBOT LOGIC ##############################################################

    def _simulate_opponents_round(self, player_index, pay):
        """Simulate a single opponent round action (randomized as in original)."""
        random_action = random.randint(0, 9)

        # Stops folding when little money bet
        if random_action == 2:
            if self.need_to_pay[player_index] < 5:
                random_action = 10

        # Stops folding when no money bet
        if random_action <= 2:
            if self.need_to_pay[player_index] == 0:
                random_action = random.randint(3,9)

        # Stops too much re-raising
        elif 3 <= random_action <= 4:
            if self.need_to_pay[player_index] > 9:
                random_action = 10

        # Stops blindly calling
        if 4 <= random_action <= 7:
            if self.need_to_pay[player_index] > 80:
                random_action = 1

        # Stops folding when only left
        counter = 0
        for a in self.need_to_pay:
            if a == -1: counter += 1
        if counter == 3: random_action = 7

        if random_action <= 2:
            self.need_to_pay[player_index] = -1
            actions = ["Dealer Folds", "Small Bind Folds", "Big Bind Folds"]

        elif random_action <= 5:
            amount = random.randint(1,12)
            amount *= amount
            if amount > 8: amount = round(amount, -1)

            all_in = random.randint(1,40) 
            if (all_in == 1) and (self.need_to_pay[player_index] != 0):
                amount = self.balances[player_index] - 1
                actions = [f"Dealer Goes All In for {amount}", f"Small Bind Goes All In for {amount}", f"Big Bind Goes All In for {amount}"]
            else:
                actions = [f"Dealer Raises by {amount}", f"Small Bind Raises by {amount}", f"Big Bind Raises by {amount}"]

            self.balances[player_index] -= amount
            self.balances[player_index] -= self.need_to_pay[player_index]
            self.prize_pot += self.need_to_pay[player_index] + amount
            for idx in range(4):
                if self.need_to_pay[idx] > -1:
                    self.need_to_pay[idx] += amount
            self.need_to_pay[player_index] = 0
        
        else:
            if self.need_to_pay[player_index] != 0:
                actions = ["Dealer Calls", "Small Bind Calls", "Big Bind Calls"]
            else:
                actions = ["Dealer Checks", "Small Bind Checks", "Big Bind Checks"]
            self.balances[player_index] -= self.need_to_pay[player_index]
            self.prize_pot += self.need_to_pay[player_index]
            self.need_to_pay[player_index] = 0
        cT.print_colour(actions[player_index - 1], "black")

        time.sleep(random.random())


    def _deal_community_cards(self, num_players: int, cards_each: int, label: str, color: str):
        """Deal community cards by recreating a single-hand surface (as in original)."""
        self.hands = [[] for _ in range(num_players)]
        total_cards = num_players * cards_each
        for i in range(total_cards):
            player_index = i % num_players
            self.hands[player_index].append(self.deck.pop())

        hand_str = self._format_hand(self.hands[0])

        self_box = ", ".join(card_to_str(c) for c in self.hands[0])
        self.flop = self_box
        cT.print_colour(f"{label}: {self_box}", color)



if __name__ == "__main__":
    while True:
        try: game = PokerGame()
        except ZeroDivisionError: pass
