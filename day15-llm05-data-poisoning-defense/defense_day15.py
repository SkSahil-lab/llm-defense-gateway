class KnowledgeIntegrityGuard:
    """
    Defends against LLM05 Data and Model Poisoning (Day 5's exploit).
    Separates 'submitted' from 'verified' - a fact only becomes
    servable truth after an explicit, separate approval step.
    Unreviewed submissions are NEVER served to users, even if asked.
    """

    def __init__(self):
        self.pending_review = {}   # submitted, not yet trusted
        self.verified_facts = {}   # promoted, safe to serve

    def submit_fact(self, topic: str, answer: str, source: str) -> dict:
        # VULNERABLE VERSION (Day 5) would write directly to servable truth here.
        # This version only stages it - nothing is servable yet.
        self.pending_review[topic.lower()] = {"answer": answer, "source": source}
        return {"status": "pending_review", "topic": topic, "note": "Not yet visible to any user"}

    def approve_fact(self, topic: str, approved_by: str) -> dict:
        key = topic.lower()
        if key not in self.pending_review:
            return {"status": "error", "reason": "no_pending_submission_for_topic"}
        fact = self.pending_review.pop(key)
        fact["approved_by"] = approved_by
        self.verified_facts[key] = fact
        return {"status": "approved", "topic": topic}

    def get_answer(self, topic: str) -> dict:
        key = topic.lower()
        if key in self.verified_facts:
            return {"response": self.verified_facts[key]["answer"], "verified": True}
        if key in self.pending_review:
            # Even though something was submitted, we NEVER serve unreviewed content
            return {"response": "No verified information available on this topic yet.", "verified": False}
        return {"response": "No information available on this topic.", "verified": False}