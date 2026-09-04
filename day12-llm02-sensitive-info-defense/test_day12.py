from defense_day12 import SafeErrorHandler, risky_divide

handler = SafeErrorHandler()

print("=== ATTACK PAYLOAD (Day 3's real exploit - empty message) ===")
result = handler.safe_call(risky_divide, "")
leaked = "postgres" in result["response"] or "SuperSecret123" in result["response"]
print(f"User-facing response: {result['response']}")
print(" BLOCKED - no credentials leaked" if not leaked else " FAILED - credentials leaked!")
print(f"Internal log still captured it: {handler.internal_log}")

print("\n=== BASELINE (normal, non-empty message) ===")
result2 = handler.safe_call(risky_divide, "hello")
print(f"User-facing response: {result2['response']}")
print(" ALLOWED (correct)" if result2["success"] else " FALSE POSITIVE - broke normal use")