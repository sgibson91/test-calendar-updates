import json
import os
import sys

issue_context = json.loads(os.environ.get("ISSUE_CONTEXT", None))
if issue_context is None:
    raise ValueError("ISSUE_CONTEXT must be provided!")

labels = [label["name"] for label in issue_context["labels"] if label["name"] == "Time Off"]

if len(labels) == 0:
    print("Issue does not have the appropriate label. Exiting script.")
    sys.exit()

print(issue_context.keys())
