from GameStrategy import GameStrategy
from ex0 import CreatureCard
from typing import List


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: List[CreatureCard], battlefield: list):

        
    def get_strategy_name(self) -> str:
        return "Agressive"
    
    def prioritize_targets(self, available_targets: List[CreatureCard]) -> list:
        if not available_targets:
            return 
        prior_target = 
        for target in available_targets:
