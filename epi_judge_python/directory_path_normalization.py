from ntpath import join
from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    if not path:
        raise ValueError('Empty string is not valid path')

    path_names = []
    if path[0] == '/':
        path_names.append('/')

    for token in (token for token in path.split('/') if token not in ['.', '']):
        if token == '..':
            if not path_names or path_names[-1] == '..':
                path_names.append(token)
            else:
                if path_names[-1] == '/':
                    raise ValueError('error path')
                path_names.pop()
        else: # must be a name
            path_names.append(token)

    result = '/'.join(path_names)
    return result[result.startswith('//'):]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
