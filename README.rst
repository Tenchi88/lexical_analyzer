This library is used for statistical analysing of the Python source code.

In ``lexical_analyzer.py`` you can find main public functions:

*   ``get_top_words_in_path(path, name_type, speech_part, top_size=10)`` - most common function
    You can check parameters for it by using ``speech_part_is_supported(speech_part)``
    and ``name_type_is_supported(names_type)`` functions.
*   Or you can use one of specialized functions:
    - get_top_verbs_in_function_names(path, top_size=10)
    - get_top_nouns_in_function_names(path, top_size=10)
    - get_top_verbs_in_variable_names(path, top_size=10)
    - get_top_nouns_in_variable_names(path, top_size=10)

You can find some usage examples in ``example.py``.

Another files content:

*   ``output_manager.py``  - class for output saving in different formats
*   ``lexical_analyzer_helpers.py``  - library's internal functions

Also you can use CLI:

usage: cli.py [-h] [-j JSON_OUTPUT] [-c CSV_OUTPUT] [-p] [-s SPEECH_PART]
              [-n NAME_TYPE] [-t TOP_SIZE] [--path PATH] [--git_path GIT_PATH]
              [--git_link GIT_LINK] [--git_username GIT_USERNAME]
              [--git_project GIT_PROJECT]

You can choose one or more output options. And you have to choose only one
option for sources: * in option 1 some existing sources will be analyzed * in
option 2-3 sources will be downloaded from some git repository and than
analyzed

optional arguments:
  -h, --help            show this help message and exit
  -j JSON_OUTPUT, --json_output JSON_OUTPUT
                        Output to specified .json-file (default: None)
  -c CSV_OUTPUT, --csv_output CSV_OUTPUT
                        Output to specified .csv-file (default: None)
  -p, --print_output    Print output to console (default: False)
  -s SPEECH_PART, --speech_part SPEECH_PART
                        Get top for specified speech part. Options: verb, noun
                        (default: verb)
  -n NAME_TYPE, --name_type NAME_TYPE
                        Get top for specified names type. Options:
                        function_definition, variable (default:
                        function_definition)
  -t TOP_SIZE, --top_size TOP_SIZE
                        Top size (default: 10)
  --path PATH           [option 1] Path to sources for analyzing (default:
                        None)
  --git_path GIT_PATH   [for options 2-3] Downloaded sources from git to this
                        dir. Than dir will be analyzed (default: None)
  --git_link GIT_LINK   [option 2] Git-link to repository. It'll be downloaded
                        to [git_dir] and analyzed (default: None)
  --git_username GIT_USERNAME
                        [option 3] GitHub username. Download one or all
                        projects of this user. See [git_project] (default:
                        None)
  --git_project GIT_PROJECT
                        [option 3+] GitHub project. If specified, only this
                        project by [git_username] will be downloaded. All
                        projects of this user will be downloaded in other
                        case. (default: None)
