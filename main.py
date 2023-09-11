import os

issue_context = os.environ.get("ISSUE_CONTEXT", None)
if issue_context is None:
    raise ValueError("ISSUE_CONTEXT must be provided!")

print(type(issue_context))
print(issue_context)
