# -*- coding: utf-8 -*-

import os
import lexical_analyzer
import sys


def show_path_stat(path, top_function, top_size=10):
    top = top_function(path, top_size=top_size)
    for word, occurrence in top:
        print(word, occurrence)


def show_projects_stat(path, projects, top_function, top_size=10):
    for word, occurrence in lexical_analyzer.get_top_for_projects_in_path(path, projects, top_function, top_size):
        print(word, occurrence)


if __name__ == '__main__':
    projects = [
        'django',
        'flask',
        'pyramid',
        'reddit',
        'requests',
        'sqlalchemy',
    ]
    # default value for example
    path = '/usr/local/lib/python3.5/site-packages/'
    if len(sys.argv) > 1:
        path = sys.argv[1]
    if not os.path.isdir(path):
        print(path, "is not existing dir")
        sys.exit(0)
    print("Top verbs in function names in ", path)
    show_projects_stat(path, projects, lexical_analyzer.get_top_verbs_in_function_names)
    print("Top nouns in function names in ", path)
    show_projects_stat(path, projects, lexical_analyzer.get_top_nouns_in_function_names)
    print("Top verbs in variable names in ", path)
    show_projects_stat(path, projects, lexical_analyzer.get_top_verbs_in_variable_names)
    print("Top nouns in variable names in ", path)
    show_projects_stat(path, projects, lexical_analyzer.get_top_nouns_in_variable_names)


