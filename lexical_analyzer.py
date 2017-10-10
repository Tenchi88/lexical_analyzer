# -*- coding: utf-8 -*-

import collections

from lexical_analyzer_helpers import *


def get_top_words_in_path(path, name_type, speech_part, top_size=10):
    if name_type not in ["variable", "function_definition"]:
        raise ValueError(name_type + " not supported. Available types: [variable, function_definition]")
    if speech_part not in ["noun", "verb"]:
        raise ValueError(speech_part + " not supported. Available types: [noun, verb]")
    if name_type is "variable":
        names = get_all_words_in_path(path, get_all_variables_names)
    else:
        names = get_all_words_in_path(path, get_all_function_names)
    if speech_part is "noun":
        words = flat([split_snake_case_name_to_words(name, is_noun) for name in names])
    else:
        words = flat([split_snake_case_name_to_words(name, is_verb) for name in names])

    return collections.Counter(words).most_common(top_size)


def get_top_verbs_in_function_names(path, top_size=10):
    return get_top_words_in_path(path, name_type="function_definition", speech_part="verb", top_size=top_size)


def get_top_nouns_in_function_names(path, top_size=10):
    return get_top_words_in_path(path, name_type="function_definition", speech_part="noun", top_size=top_size)


def get_top_verbs_in_variable_names(path, top_size=10):
    return get_top_words_in_path(path, name_type="variable", speech_part="verb", top_size=top_size)


def get_top_nouns_in_variable_names(path, top_size=10):
    return get_top_words_in_path(path, name_type="variable", speech_part="noun", top_size=top_size)


def get_top_for_projects_in_path(projects_path, projects, top_function, top_size=10):
    top_words = {}
    for project in projects:
        full_path = os.path.join(projects_path, project)
        top = top_function(full_path, top_size=top_size)
        top_words = sum_occurrence(top_words, top)
    top_words_list = []
    for word in top_words:
        top_words_list.append((word, top_words[word]))

    return top_words_list


def speech_part_is_supported(speech_part):
    return speech_part in ["verb", "noun"]


def name_type_is_supported(names_type):
    return names_type in ["function_definition", "variable"]
