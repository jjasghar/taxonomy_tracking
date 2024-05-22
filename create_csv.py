import csv
import datetime
import os
from pull_stats_from_github import *

token = os.getenv("GH_TOKEN")
repository = "instructlab/taxonomy"


def main(repo):
    csv_file = "taxonomy_stats.csv"
    today_date = datetime.date.today()
    if os.path.exists(csv_file):
        with open(csv_file, 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([f'{today_date}',f'{total_open_pulls(repo)}',f'{total_triage_requested_changes_labeled(repo)}',f'{total_triage_needed_prs(repo)}',f'{total_triage_requested_changes_and_triage_needed_labeled(repo)}',f'{total_precheck_generate_ready(repo)}',f'{total_triage_rejected(repo)}',f'{total_stale_prs(repo)}',f'{total_stale_prs(repo)}',f'{total_stale_prs(repo)}',f'{total_stale_prs(repo)}'])
    else:
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['Date','OpenPRs','RequestedChanges','TriageNeeded','TriageRC&TriageNeeded','PrecheckGeneratedReady','TriageRejected', "StalePRs"])
            writer.writerow([f'{today_date}',f'{total_open_pulls(repo)}',f'{total_triage_requested_changes_labeled(repo)}',f'{total_triage_needed_prs(repo)}',f'{total_triage_requested_changes_and_triage_needed_labeled(repo)}',f'{total_precheck_generate_ready(repo)}',f'{total_triage_rejected(repo)}',f'{total_stale_prs(repo)}'])


if __name__ == '__main__':
    from github import Github, Auth
    # using an access token
    auth = Auth.Token(token)
    # Public Web Github
    g = Github(auth=auth)
    # Then play with your Github objects:
    repo = g.get_repo(repository)
    main(repo)
    g.close()
