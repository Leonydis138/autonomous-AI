import numpy as np

class ReinforcementLearningAgent:
    def __init__(self, actions, learning_rate=0.1, discount_factor=0.9):
        self.actions = actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.q_table = {}  # Initialize Q-table

    def choose_action(self, state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.actions))
        return np.argmax(self.q_table[state])  # Choose action with max Q-value

    def learn(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.actions))
        if next_state not in self.q_table:
            self.q_table[next_state] = np.zeros(len(self.actions))
        
        # Update Q-value using Q-learning formula
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.discount_factor * self.q_table[next_state][best_next_action]
        self.q_table[state][action] += self.learning_rate * (td_target - self.q_table[state][action])

# Example usage:
actions = [0, 1, 2]  # Define possible actions
agent = ReinforcementLearningAgent(actions)
