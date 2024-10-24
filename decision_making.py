class DecisionEngine:
    def __init__(self):
        self.rules = []  # List of decision rules

    def add_rule(self, condition, action):
        self.rules.append((condition, action))

    def make_decision(self, context):
        for condition, action in self.rules:
            if condition(context):
                return action(context)  # Execute action if condition is met
        return None  # Default action

# Example usage:
def is_high_risk(context):
    return context['risk_level'] > 7

def alert_action(context):
    print("Alert! High-risk situation detected.")

decision_engine = DecisionEngine()
decision_engine.add_rule(is_high_risk, alert_action)
decision_engine.make_decision({'risk_level': 8})  # This would trigger the alert
