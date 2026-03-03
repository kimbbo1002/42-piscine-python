from GameStrategy import GameStrategy
from ex0 import CreatureCard
from typing import List


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: List, battlefield: list) -> dict:
        target = AggressiveStrategy.prioritize_targets(self, battlefield)
        return {
            
        }
        
    def get_strategy_name(self) -> str:
        return "Agressive"
    
    def prioritize_targets(self, available_targets: List[CreatureCard]) -> list:
        if not available_targets:
            return 
        prior_target = available_targets[0]
        for target in available_targets:
            if target.health < prior_target.health:
                prior_target = target
        return [prior_target]
