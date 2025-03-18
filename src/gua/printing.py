__all__ = ["printEventDetails"]

def printCommitCommentEvent(event):
    repo_name = event["repo"]["name"]
    print(f"- Commented on a commit in {repo_name}")

def printCreateEvent(event):
    repo_name = event["repo"]["name"]
    ref_type = event["payload"]["ref_type"]
    print(f"- Created a {ref_type} in {repo_name}")

def printDeleteEvent(event):
    repo_name = event["repo"]["name"]
    print(f"- Deleted a branch or tag in {repo_name}")

def printForkEvent(event):
    repo_name = event["repo"]["name"]
    print(f"- Forked {repo_name}")

def printIssueCommentEvent(event):
    repo_name = event["repo"]["name"]
    print(f"- Commented on an issue in {repo_name}")

def printIssuesEvent(event):
    repo_name = event["repo"]["name"]
    action = event["payload"]["action"]
    print(f"- {action.capitalize()} an issue in {repo_name}")

def printPublicEvent(event):
    repo_name = event["repo"]["name"]
    print(f"- Made {repo_name} public")

def printPullRequestEvent(event):
    repo_name = event["repo"]["name"]
    action = event["payload"]["action"]
    print(f"- {action.capitalize()} a pull request in {repo_name}")

def printPullRequestReviewEvent(event):
    repo_name = event["repo"]["name"]
    print(f"- Reviewed a pull request in {repo_name}")

def printPullRequestReviewCommentEvent(event):
    repo_name = event["repo"]["name"]
    print(f"- Commented on a pull request review in {repo_name}")

def printPushEvent(event):
    repo_name = event["repo"]["name"]
    commits = len(event["payload"]["commits"])
    print(f"- Pushed {commits} commit(s) to {repo_name}")

def printReleaseEvent(event):
    repo_name = event["repo"]["name"]
    print(f"- Released a new version in {repo_name}")

def printWatchEvent(event):
    repo_name = event["repo"]["name"]
    print(f"- Starred {repo_name}")

def printUnknownEvent(event):
    repo_name = event["repo"]["name"]
    print(f"- Performed an unknown action in {repo_name}")

def printEventDetails(event):
    type = event["type"]    
    match type:
        case "CommitCommentEvent":
            printCommitCommentEvent(event)
        case "CreateEvent":
            printCreateEvent(event)
        case "DeleteEvent":
            printDeleteEvent(event)
        case "ForkEvent":
            printForkEvent(event)
        case "IssueCommentEvent":
            printIssueCommentEvent(event)
        case "IssuesEvent":
            printIssuesEvent(event)
        case "PublicEvent":
            printPublicEvent(event)
        case "PullRequestEvent":
            printPullRequestEvent(event)
        case "PullRequestReviewEvent":
            printPullRequestReviewEvent(event)
        case "PullRequestReviewCommentEvent":
            printPullRequestReviewCommentEvent(event)
        case "PushEvent":
            printPushEvent(event)
        case "ReleaseEvent":
            printReleaseEvent(event)
        case "WatchEvent":
            printWatchEvent(event)
        case _:
            printUnknownEvent(event)