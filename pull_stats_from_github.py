from github import Github, UnknownObjectException
import os
# Authentication is defined via github.Auth
from github import Auth

token = os.getenv("GH_TOKEN")
repository = "instructlab/taxonomy"

open_pulls = []
triage_requested_prs = []
triage_needed_prs = []
triage_requested_and_needed_prs = []
precheck_generate_ready = []
total_triage_rejected_prs = []


def total_open_pulls(repo):
    # pulls
    repo_pulls = repo.get_pulls(state="open", sort="number")
    for pull in repo_pulls:
        open_pulls.append(pull)
    return f"{len(open_pulls)}"


def total_triage_requested_changes_labeled(repo):
    triage_requested_prs_labeled = repo.get_issues(labels=["triage-requested-changes"])
    for pr in triage_requested_prs_labeled:
        triage_requested_prs.append(pr)
    return f"{len(triage_requested_prs)}"


def total_triage_needed_prs(repo):
    triage_needed_prs_labeled = repo.get_issues(labels=["triage-needed"])
    for pr in triage_needed_prs_labeled:
        triage_needed_prs.append(pr)
    return f"{len(triage_needed_prs)}"


def total_triage_requested_changes_and_triage_needed_labeled(repo):
    triage_requested_changes_and_triage_needed = repo.get_issues(labels=["triage-requested-changes", "triage-needed"])
    for pr in triage_requested_changes_and_triage_needed:
        triage_requested_and_needed_prs.append(pr)
    return f"{len(triage_requested_and_needed_prs)}"


def total_precheck_generate_ready(repo):
    total_precheck_generate = repo.get_issues(labels=["precheck-generate-ready"])
    for pr in total_precheck_generate:
        precheck_generate_ready.append(pr)
    return f"{len(precheck_generate_ready)}"


def total_triage_rejected(repo):
    total_rejected = repo.get_issues(labels=["triage-rejected"], state="all")
    for pr in total_rejected:
        total_triage_rejected_prs.append(pr)
    return f"{len(total_triage_rejected_prs)}"


def main(repo):
    print(f"Total open taxonomy pull requests: {total_open_pulls(repo)}")
    print(f"Total open triage needed pulls: {total_triage_needed_prs(repo)}")
    print(f"Total open triage requested pulls: {total_triage_requested_changes_labeled(repo)}")
    print(f"Total open triage requested and triage-needed pulls: {total_triage_requested_changes_and_triage_needed_labeled(repo)}")
    print(f"Total open precheck generate ready pulls: {total_precheck_generate_ready(repo)}")
    print(f"Total triage rejected pulls: {total_triage_rejected(repo)}")


if __name__ == "__main__":
    # using an access token
    auth = Auth.Token(token)
    # Public Web Github
    g = Github(auth=auth)
    # Then play with your Github objects:
    repo = g.get_repo(repository)
    main(repo)
    g.close()
