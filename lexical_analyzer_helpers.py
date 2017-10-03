import ast
import os
import collections

from nltk import pos_tag


def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def is_verb(word):
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] == 'VB'


def file_to_tree(filename, with_file_names=False, with_file_content=False):
    with open(filename, 'r', encoding='utf-8') as attempt_handler:
        main_file_content = attempt_handler.read()
    try:
        tree = ast.parse(main_file_content)
    except SyntaxError as e:
        print(e)
        tree = None
    if not with_file_names:
        return tree
    if with_file_content:
        return filename, main_file_content, tree
    else:
        return filename, tree


def get_trees(path, with_file_names=False, with_file_content=False, print_debug=False):
    print(path)
    file_names = []
    trees = []
    for dir_name, dirs, files in os.walk(path, topdown=True):
        python_files = [os.path.join(dir_name, file) for file in files if file.endswith('.py')]
        file_names.append(python_files)
    file_names = flat(file_names)
    if print_debug:
        print('total %s files' % len(file_names))
    for filename in file_names:
        trees.append(file_to_tree(filename, with_file_names, with_file_content))
    if print_debug:
        print('trees generated')
    return trees


def get_all_names(tree):
    return [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]


def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_verb(word)]
