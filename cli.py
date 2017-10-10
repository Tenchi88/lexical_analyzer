# -*- coding: utf-8 -*-

import argparse
import lexical_analyzer
import output_manager
import source_downloader


def download_sources_from_git(git_dir, link, username, project):
    git_downloader = source_downloader.GitDownloader(work_dir=git_dir)
    if link:
        git_downloader.download_by_link(link)
        return
    if not username:
        raise ValueError("Git-link and GitHub username is not specified")
    if not project:
        git_downloader.download_all_from_user(username)
    else:
        git_downloader.download(username, project)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="You can choose one or more output options.\n"
                    "And you have to choose only one option for sources:\n"
                    "* in option 1 some existing sources will be analyzed\n"
                    "* in option 2-3 sources will be downloaded from some git repository and than analyzed\n",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-j", "--json_output", help="Output to specified .json-file",
                        type=str)
    parser.add_argument("-c", "--csv_output", help="Output to specified .csv-file",
                        type=str)
    parser.add_argument("-p", "--print_output", help="Print output to console", default=False,
                        action="store_true")
    parser.add_argument("-s", "--speech_part",
                        help="Get top for specified speech part. Options: verb, noun",
                        default="verb")
    parser.add_argument("-n", "--name_type",
                        help="Get top for specified names type. Options: function_definition, variable",
                        default="function_definition")
    parser.add_argument("-t", "--top_size",
                        help="Top size",
                        type=int, default=10)
    parser.add_argument("--path", help="[option 1] Path to sources for analyzing",
                        type=str)
    parser.add_argument("--git_path",
                        help="[for options 2-3] Downloaded sources from git to this dir. Than dir will be analyzed",
                        type=str)
    parser.add_argument("--git_link",
                        help="[option 2] Git-link to repository. It'll be downloaded to [git_dir] and analyzed",
                        type=str)
    parser.add_argument("--git_username",
                        help="[option 3] GitHub username. Download one or all projects of this user. See [git_project]",
                        type=str)
    parser.add_argument("--git_project",
                        help="[option 3+] GitHub project. If specified, only this project by [git_username] will be "
                             "downloaded. All projects of this user will be downloaded in other case.",
                        type=str)

    arguments = parser.parse_args()

    if not lexical_analyzer.speech_part_is_supported(arguments.speech_part):
        raise ValueError("Speech part is not supported: " + arguments.speech_part)
    if not lexical_analyzer.name_type_is_supported(arguments.name_type):
        raise ValueError("Names type is not supported: " + arguments.name_type)

    work_path = None
    if arguments.path:
        work_path = arguments.path

    if arguments.git_path:
        work_path = arguments.git_path
        download_sources_from_git(work_path, arguments.git_link, arguments.git_username, arguments.git_project)

    if not work_path:
        raise ValueError("You have to choose one of sources options")

    output = output_manager.OutputManager(
        print_output=arguments.print_output,
        json_file_name=arguments.json_output,
        csv_file_name=arguments.csv_output
    )

    top = lexical_analyzer.get_top_words_in_path(
        work_path, arguments.name_type,
        arguments.speech_part, arguments.top_size
    )
    output.generate_output(top)

