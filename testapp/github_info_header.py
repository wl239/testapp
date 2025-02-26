from git import Repo
from datetime import datetime
from os import getcwd
from dash import html


def github_info_header():
    repo = Repo(search_parent_directories=True)

    return html.Div([
        html.P("Current working directory: {0}".format(getcwd())),
        html.P(repo.head.ref.path),
        html.P(repo.head.object.hexsha),
        html.P(repo.head.commit.message),
        html.P(repo.head.commit.author.name),
        html.P(
            datetime.fromtimestamp(repo.head.commit.committed_date).strftime(
                "%A, %d %b %Y at %H:%M:%S"
            )
        )
    ])
