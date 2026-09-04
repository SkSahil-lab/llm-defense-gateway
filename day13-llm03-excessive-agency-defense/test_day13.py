from defense_day13 import AgencyLimitGuard

guard = AgencyLimitGuard()

print("=== ATTACK PAYLOAD 1 (Day 7's real exploit - $999,999 refund) ===")
result = guard.check_refund(999999)
print(result)
print(" BLOCKED - queued for human approval" if not result["executed"] else " FAILED - auto-approved")

print("\n=== ATTACK PAYLOAD 2 (Day 7's real exploit - account deletion) ===")
result2 = guard.check_action("delete_account")
print(result2)
print(" BLOCKED - queued for human approval" if not result2["executed"] else " FAILED - auto-approved")

print("\n=== BASELINE (normal, reasonable refund) ===")
result3 = guard.check_refund(20)
print(result3)
print(" ALLOWED (correct)" if result3["executed"] else " FALSE POSITIVE")

print(f"\nHuman approval queue now has {len(guard.pending_approval)} item(s) waiting: {guard.pending_approval}")