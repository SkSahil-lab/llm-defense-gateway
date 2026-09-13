from defense_day19 import OutputSanitizationGuard

guard = OutputSanitizationGuard()

print("=== ATTACK PAYLOAD (Day 6's real exploit) ===")
malicious_review = "Great product! <script>alert('XSS')</script>"
result = guard.render_review_safely(malicious_review)
print(result)
still_executable = "<script>" in result
print(" BLOCKED - script tag rendered as inert text" if not still_executable else " FAILED - script tag still executable")

print("\n=== BASELINE (normal review) ===")
normal_review = "This product is great!"
result2 = guard.render_review_safely(normal_review)
print(result2)
print("ALLOWED (correct) - normal text unaffected" if "This product is great!" in result2 else " FALSE POSITIVE")