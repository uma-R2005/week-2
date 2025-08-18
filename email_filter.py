# Define initial spam email sets from two filters
filter_a_spam = {"spam1@example.com", "spam2@example.com", "spam3@example.com"}
filter_b_spam = {"spam2@example.com", "spam4@example.com", "spam5@example.com"}

# Input: Get new emails from user to add to filters
new_a = input("Enter new spam email to add to Filter A (or press Enter to skip): ").strip().lower()
if new_a:
    filter_a_spam.add(new_a)

new_b = input("Enter new spam email to add to Filter B (or press Enter to skip): ").strip().lower()
if new_b:
    filter_b_spam.add(new_b)

# Output: Show all suspected spam emails (union)
all_spam = filter_a_spam.union(filter_b_spam)
print("\nAll Suspected Spam Emails (Union):")
for email in sorted(all_spam):
    print(f"- {email}")

# Output: Show high-confidence spam emails (intersection)
high_conf_spam = filter_a_spam.intersection(filter_b_spam)
print("\nHigh Confidence Spam Emails (Intersection):")
for email in sorted(high_conf_spam):
    print(f"- {email}")

# Output: Show emails flagged only by Filter A
only_a = filter_a_spam - filter_b_spam
print("\nEmails Flagged Only by Filter A:")
for email in sorted(only_a):
    print(f"- {email}")

# Output: Show emails flagged only by Filter B
only_b = filter_b_spam - filter_a_spam
print("\nEmails Flagged Only by Filter B:")
for email in sorted(only_b):
    print(f"- {email}")

# Output: Summary statistics
print("\nSummary Statistics:")
print(f"Total emails flagged by Filter A: {len(filter_a_spam)}")
print(f"Total emails flagged by Filter B: {len(filter_b_spam)}")
print(f"High-confidence spam emails (both filters): {len(high_conf_spam)}")
print(f"Total suspected spam (either filter): {len(all_spam)}")
