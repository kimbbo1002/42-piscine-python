from abc import ABC, abstractmethod


class Player:
    def __init__(self, name: str, deck: Deck)