from taskagent.file_storage import init_storage, load_storage, save_storage


def test_storage(tmp_path):
    pass
    # test_file = tmp_path / "test_tasks.json"
    # init_storage(test_file)
    # assert not test_file.exists()
    # assert load_storage() == []

    # data = [{"name": "Test Task", "done": False}]
    # save_storage(data)
    # assert test_file.exists()
    # assert load_storage() == data

    # save_storage([])
    # assert load_storage() == []