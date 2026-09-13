class ConsumptionAndGroundingGuard:
    """
    Defends against LLM06 Unbounded Consumption + LLM07 Misinformation (Day 9's exploit).
    1. Hard iteration cap on any agent loop - no goal, achievable or not, runs forever.
    2. Answers only come from a real knowledge base - no knowledge, no answer,
       never a confident guess dressed up as fact.
    """

    MAX_ITERATIONS = 5  # dramatically lower than Day 9's uncapped (demo-capped-at-50) loop

    def run_bounded_loop(self, goal: str, is_achieved_fn) -> dict:
        iterations = 0
        achieved = False
        while not achieved and iterations < self.MAX_ITERATIONS:
            iterations += 1
            achieved = is_achieved_fn(goal)
        return {
            "iterations_used": iterations,
            "achieved": achieved,
            "stopped_reason": "goal_achieved" if achieved else "max_iterations_reached",
        }

    def answer_grounded(self, question: str, knowledge_base: dict) -> dict:
        for topic, answer in knowledge_base.items():
            if topic in question.lower():
                return {"response": answer, "grounded": True}
        # VULNERABLE version would generate a plausible-sounding fake answer here instead
        return {"response": "No verified information available on this topic.", "grounded": False}


def never_achievable(goal: str) -> bool:
    # Simulates Day 9's impossible goal - designed to never resolve
    return False