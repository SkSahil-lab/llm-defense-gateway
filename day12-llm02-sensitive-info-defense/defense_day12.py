class SafeErrorHandler:
    """
    Defends against LLM02 Sensitive Information Disclosure (Day 3's exploit).
    Wraps risky operations so exceptions never leak internal details to the
    user - full detail still gets logged internally for real debugging.
    """

    def __init__(self):
        self.internal_log = []  # simulates a real internal-only logging system

    def safe_call(self, risky_function, *args, **kwargs) -> dict:
        try:
            result = risky_function(*args, **kwargs)
            return {"success": True, "response": result}
        except Exception as e:
            # Log the FULL real error internally - nothing lost for debugging
            self.internal_log.append(str(e))
            # But the user only ever sees this generic, safe message
            return {"success": False, "response": "Something went wrong. Please try again."}


# --- Simulates the original Day 3 vulnerable logic, now wrapped safely ---
DB_CONFIG = "postgres://admin:SuperSecret123@internal-db.acme.local:5432/customers"

def risky_divide(message: str) -> str:
    word_count = 100 / len(message)  # crashes on empty message, same as Day 3
    return f"[stub response to: {message}]"


if __name__ == "__main__":
    handler = SafeErrorHandler()
    result = handler.safe_call(risky_divide, "")
    print(f"User sees: {result}")
    print(f"Internal log (never shown to user): {handler.internal_log}")