import pandas as pd
import github
import secret


g = github.Github(secret.TOKEN)


def collect_stats(repo_name):
    repo = g.get_repo(repo_name)
    commits = repo.get_commits()
    return dict(
        name=repo.name,
        stars=repo.stargazers_count,
        forks=repo.forks_count,
        contributors=repo.get_contributors().totalCount,
        commits=commits.totalCount,
        open_issues=repo.open_issues_count,
        closed_issues=repo.get_issues(state="closed").totalCount,
        created=repo.created_at.strftime("%Y-%m-%d"),
        last_commit=commits[0].commit.author.date.strftime("%Y-%m-%d"),
        license=repo.get_license().license.spdx_id,
    )


def compare_repos(repos):
    return pd.DataFrame([collect_stats(r) for r in repos]).set_index("name")
