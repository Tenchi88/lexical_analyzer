import os
import collections
import lexical_analyzer
import sys


def show_stat(projects_path, top_function):
    wds = []
    projects = [
        'django',
        'flask',
        'pyramid',
        'reddit',
        'requests',
        'sqlalchemy',
    ]
    for project in projects:
        full_path = os.path.join(projects_path, project)
        wds += top_function(full_path)

    top_size = 200
    print('total %s words, %s unique' % (len(wds), len(set(wds))))
    for word, occurence in collections.Counter(wds).most_common(top_size):
        print(word, occurence)


if __name__ == '__main__':
    # default value for example
    path = '/usr/local/lib/python3.5/site-packages/'
    if len(sys.argv) > 1:
        path = sys.argv[1]
    if not os.path.isdir(path):
        print(path, "is not existing dir")
        sys.exit(0)
    print("Top functions names in", path)
    show_stat(path, lexical_analyzer.get_top_functions_names_in_path)
    print("Top verbs in", path)
    show_stat(path, lexical_analyzer.get_top_verbs_in_path)
