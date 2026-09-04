from defense_day14 import (
    DependencyIntegrityGuard,
    TRUSTED_SOURCE,
    COMPROMISED_SOURCE,
    trusted_analyze,
    compromised_analyze,
)

guard = DependencyIntegrityGuard()
guard.register_trusted("sentiment_plugin", TRUSTED_SOURCE)

print("=== ATTACK PAYLOAD (Day 4's real exploit - silently swapped plugin) ===")
result = guard.verify_and_run("sentiment_plugin", COMPROMISED_SOURCE, compromised_analyze, "hello")
print(result)
print(" BLOCKED - compromised code never executed" if not result["allowed"] else " FAILED - malicious code ran")

print("\n=== BASELINE (unmodified, trusted plugin) ===")
result2 = guard.verify_and_run("sentiment_plugin", TRUSTED_SOURCE, trusted_analyze, "hello")
print(result2)
print(" ALLOWED (correct)" if result2["allowed"] else " FALSE POSITIVE")