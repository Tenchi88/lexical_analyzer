# -*- coding: utf-8 -*-

import ast
import os

from nltk import pos_tag


def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def is_verb(word):
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] == 'VB'


def is_noun(word):
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] == 'NN'


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
    if print_debug:
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


def get_all_variables_names(tree):
    return [node.id.lower() for node in ast.walk(tree) if isinstance(node, ast.Name)]


def get_all_function_names(tree):
    return [node.name.lower() for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]


def split_snake_case_name_to_words(name, some_filter=None):
    if some_filter is not None:
        return [word for word in name.split('_') if some_filter(word)]
    return [word for word in name.split('_') if word]


def is_not_builtin_function(function_name):
    return not (function_name.startswith('__') and function_name.endswith('__'))


def sum_occurrence(top, add_words):
    for word, cnt in add_words:
        if word in top:
            top[word] += cnt
        else:
            top[word] = cnt
    return top


def get_all_words_in_path(path, get_some_type):
    trees = get_trees(path)
    return [f for f in flat([get_some_type(t) for t in trees]) if is_not_builtin_function(f)]
