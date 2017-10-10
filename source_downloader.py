# -*- coding: utf-8 -*-

import os
from github import Github
from git import Repo
from re import split
from shutil import rmtree


class BaseDownloader:
    def __init__(
            self,
            work_dir="tmp"
    ):
        self.work_dir = work_dir
        if not os.path.exists(work_dir):
            os.mkdir(work_dir)

    def download(self, path):
        raise NotImplementedError


class GitDownloader(BaseDownloader):
    def __init__(
            self,
            work_dir="tmp",
            login_or_token=None,
            password=None
    ):
        super(GitDownloader, self).__init__(work_dir=work_dir)
        self.git = Github(login_or_token=login_or_token, password=password)

    def download_by_link(
            self,
            git_url,
            overwrite=False
    ):
        user = split("/", git_url)[-2]
        if not os.path.exists(os.path.join(self.work_dir, user)):
            os.mkdir(os.path.join(self.work_dir, user))
        repo_name = split("/", git_url)[-1][:-4]
        download_to = os.path.join(self.work_dir, user, repo_name)
        if os.path.exists(download_to) and not overwrite:
            return
        elif os.path.exists(download_to):
            rmtree(download_to)
        Repo.clone_from(git_url, download_to)

    def download(
            self,
            user,
            repo_name,
            overwrite=False
    ):
        repo = self.find_user_by_name(user).get_repo(repo_name)
        self.download_by_link(repo.clone_url, overwrite=overwrite)

    def download_all_from_user(
            self,
            user,
            overwrite=False
    ):
        for repo in self.find_user_by_name(user).get_repos():
            self.download_by_link(repo.clone_url, overwrite=overwrite)

    def find_user_by_name(
            self,
            name
    ):
        return self.git.search_users(name)[0]


if __name__ == '__main__':
    git_downloader = GitDownloader()
    print("Download by link")
    git_downloader.download_by_link("https://github.com/Tenchi88/test.git")
    print("Download project X by user Y")
    git_downloader.download("Tenchi88", "test")
    print("Download all by user")
    git_downloader.download_all_from_user("Tenchi88", overwrite=True)
