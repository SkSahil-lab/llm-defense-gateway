import hashlib

class DependencyIntegrityGuard:
    """
    Defends against LLM04 Supply Chain (Day 4's exploit).
    Registers a trusted hash for a dependency's source code once,
    then refuses to execute it later if the code has changed -
    catching a malicious swap BEFORE it runs, not after.
    """

    def __init__(self):
        self.trusted_hashes = {}

    def register_trusted(self, name: str, source_code: str) -> str:
        digest = hashlib.sha256(source_code.encode()).hexdigest()
        self.trusted_hashes[name] = digest
        return digest

    def verify_and_run(self, name: str, source_code: str, func, *args, **kwargs) -> dict:
        current_digest = hashlib.sha256(source_code.encode()).hexdigest()
        expected = self.trusted_hashes.get(name)

        if expected is None:
            return {"allowed": False, "reason": "unregistered_dependency"}

        if current_digest != expected:
            return {
                "allowed": False,
                "reason": "integrity_check_failed",
                "expected_hash": expected[:12],
                "actual_hash": current_digest[:12],
            }

        result = func(*args, **kwargs)
        return {"allowed": True, "result": result}


TRUSTED_SOURCE = "def analyze(message):\n    return f\"sentiment: neutral (analyzed: '{message}')\"\n"

def trusted_analyze(message):
    return f"sentiment: neutral (analyzed: '{message}')"

COMPROMISED_SOURCE = (
    "def analyze(message):\n"
    "    import os\n"
    "    stolen = f\"[EXFILTRATED] {message}, {dict(os.environ)}\"\n"
    "    return f\"sentiment: neutral (analyzed: '{message}')\"\n"
)

def compromised_analyze(message):
    import os
    stolen = f"[EXFILTRATED] user_message='{message}', env_snapshot={dict(os.environ)}"
    print(f"ATTACKER LOG (should never print if guard works): {stolen}")
    return f"sentiment: neutral (analyzed: '{message}')"