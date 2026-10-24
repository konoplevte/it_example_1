import pytest

from taskagent.tasks import add_task, done_task, list_tasks, init_tasks, get_tasks, delete_task


@pytest.fixture(autouse=True)
def clear_tasks():
    init_tasks([])

def test_add_task():
    add_task("АТЖУМАНЯ")

    assert len(get_tasks()) == 1
    assert list_tasks() == "1. [ ] АТЖУМАНЯ\n"

@pytest.fixture
def add_tasks():
    init_tasks([
        {"name": "test1", "done": False},
        {"name": "test2", "done": False},
        {"name": "test3", "done": False}
    ])

@pytest.mark.parametrize("idx", [0, 1, 2])
def test_done_tasks(add_tasks, idx):
    done_task(idx)

    assert get_tasks()[idx]["done"] == True

def test_delete_tasks(add_tasks):
    task = delete_task(1)
    assert task == {"name": "test2", "done": False}
    assert len(get_tasks()) == 2
    assert delete_task(10) is None    