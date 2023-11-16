from interviews.a_2023.change_directory import change_directory


def test_change_directory1():
    cwd = '/users/rohan'
    cd = 'documents/python/project'
    expected_result = '/users/rohan/documents/python/project'
    assert change_directory(cwd, cd) == expected_result


def test_change_directory2():
    cwd = '/users/rohan'
    cd = '/documents/python/project'
    expected_result = '/documents/python/project'
    assert change_directory(cwd, cd) == expected_result


def test_change_directory3():
    cwd = '/users/rohan'
    cd = '/../python/project'
    expected_result = '/python/project'
    assert change_directory(cwd, cd) == expected_result


def test_change_directory4():
    cwd = '/users/rohan'
    cd = '../python/project'
    expected_result = '/users/python/project'
    assert change_directory(cwd, cd) == expected_result


def test_change_directory5():
    cwd = '/users/rohan'
    cd = '../python/./project'
    expected_result = '/users/python/project'
    assert change_directory(cwd, cd) == expected_result
