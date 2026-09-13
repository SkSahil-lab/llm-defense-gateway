class IsolatedContextGuard:
    """
    Defends against LLM08 Hidden Context Exposure (Day 8's exploit).
    Hidden/internal context lives in a separate store the response
    generator has no reference to - structurally unreachable, not
    just filtered out after the fact.
    """

    def __init__(self):
        # Internal-only store - intentionally never passed into user-facing logic
        self._internal_context = {
            "admin_note": "Internal: VIP customers get silent 40% discount code VIP40OFF, do not advertise.",
            "internal_tool_schema": {
                "endpoint": "http://internal-billing.acme.local:9090/charge",
                "auth_header": "X-Internal-Key: bill-svc-8891",
            },
        }

    def generate_response(self, message: str) -> dict:
        # This function has NO parameter, NO variable, NO reference at all
        # to self._internal_context. It structurally cannot leak what it
        # never received - unlike Day 8, where debug phrasing could pull
        # hidden context into the same response path.
        lower = message.lower()
        if "debug" in lower or "show context" in lower or "what tools" in lower:
            return {"response": "I'm not able to share internal configuration details."}
        return {"response": "I can help answer questions about our products."}