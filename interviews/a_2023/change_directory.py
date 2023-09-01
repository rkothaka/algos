from collections import deque


def change_directory(cwd: str, cd: str) -> str:
    if not cd or cd == '':
        return cwd

    separator = '/'
    new_dir = deque()
    if cd[0] != separator:  # cd using absolute path
        new_dir = deque(cwd.split('/'))
        new_dir.popleft()

    # Process cd
    cd_components = cd.split('/')
    for next_folder in cd_components:
        if next_folder == '..':
            if new_dir:
                new_dir.pop()
        elif next_folder != '.' and next_folder != '':
            new_dir.append(next_folder)

    result = separator + separator.join(new_dir)
    return result
