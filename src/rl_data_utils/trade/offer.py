from rl_data_utils.exceptions import InvalidItemAttribute
from rl_data_utils.rocket_league.rocket_league import RocketLeagueObject, Validable


class Offer(RocketLeagueObject, Validable):
    def __init__(self, credits_=None, items=None, author=None):
        self.credits = credits_
        self.items = items
        self.author = author

    def is_only_items(self):
        return not self.credits and self.items

    def is_only_credits(self):
        return self.credits and not self.items

    def is_items_and_credits(self):
        return self.credits and self.items

    def validate(self):
        self.credits.validate()
        self.items.validate()

    def is_valid(self):
        return self._is_valid_by_validate(InvalidItemAttribute)
