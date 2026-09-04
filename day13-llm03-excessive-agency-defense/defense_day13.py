class AgencyLimitGuard:
    """
    Defends against LLM03 Excessive Agency (Day 7's exploit).
    Adds two independent checks before any impactful agent action:
    1. A hard cap on action size (e.g. refund amount)
    2. Mandatory second-approval for anything irreversible
    """

    REFUND_CAP = 500  # anything above this needs human approval, no exceptions
    IRREVERSIBLE_ACTIONS = {"delete_account"}

    def __init__(self):
        self.pending_approval = []  # simulates a real human-approval queue

    def check_refund(self, amount: int) -> dict:
        if amount > self.REFUND_CAP:
            self.pending_approval.append({"action": "refund", "amount": amount})
            return {
                "executed": False,
                "reason": "exceeds_auto_approval_cap",
                "cap": self.REFUND_CAP,
                "requested": amount,
                "status": "queued_for_human_approval",
            }
        return {"executed": True, "reason": "within_auto_approval_cap", "amount": amount}

    def check_action(self, action_name: str) -> dict:
        if action_name in self.IRREVERSIBLE_ACTIONS:
            self.pending_approval.append({"action": action_name})
            return {
                "executed": False,
                "reason": "irreversible_action_requires_human_confirmation",
                "status": "queued_for_human_approval",
            }
        return {"executed": True, "reason": "reversible_action_allowed"}