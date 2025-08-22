import numpy as np

class SecondPriceAuction:
    # Starts a new round
    def __init__(self):
        self.reset()

    # Resets the auction for a new round
    def reset(self):
        self.agent_value = np.random.uniform(0, 1)
        self.opponent_value = np.random.uniform(0, 1)
        return self.agent_value
    
    def step(self, agent_bid):
        opponent_bid = self.opponent_value
        if agent_bid > opponent_bid:
            price_paid = opponent_bid
            reward = self.agent_value - price_paid
        else:
            reward = 0
        done = True  # In a single round auction, the episode ends after one step
        return self.agent_value, reward, done, {}