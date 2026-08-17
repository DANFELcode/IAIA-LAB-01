class Problem:
    def __init__(self, initial_state, goals, graph, heuristic):
        self.initialState = initial_state
        self.goals = goals
        self.graph = graph
        self.heuristic = heuristic

    def is_goal(self, state):
        return state in self.goals

    def result_actions(self, state):
        actions = self.graph[state]

        return set(actions.keys())

    def action_cost(self, state, action, state_1):
        actions = self.graph[state]
        return actions[state_1]

    def heuristic(self, state):
        return self.heuristic[state]
