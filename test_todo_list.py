import pytest 
import todo_list2 as todo
from unittest.mock import patch

@pytest.fixture 
def mock_todo_data():
    return ({"01:00" : "Quiet Time", "02:00": "Sleep"})


@pytest.fixture
def mock_get_time():
    with patch("todo_list2.get_valid_time", return_value ="02:00" ) as mock:
        yield mock


@pytest.fixture
def mock_save_todo_list():
    with patch ("todo_list2.save_todo_list") as mock_save:
        yield mock_save


def test_modify_item(mock_save_todo_list, mock_get_time,mock_todo_data):
    with patch ("todo_list2.load_todo_list", return_value = mock_todo_data.copy()), \
        patch ("builtins.input", side_effect = ["sleep"]):
        todo.modify_item()
        mock_save_todo_list.assert_called_with({"01:00": "Quiet Time", "02:00": "sleep"})



def test_delete_item(mock_save_todo_list, mock_get_time, mock_todo_data):
    with patch ("todo_list2.load_todo_list", return_value = mock_todo_data.copy()):
        todo.delete_item()
        mock_save_todo_list.assert_called_with({"01:00": "Quiet Time"})


def test_create_list(mock_save_todo_list, mock_todo_data):
    with patch ("todo_list2.load_todo_list", return_value = mock_todo_data.copy()),\
        patch ("todo_list2.get_valid_time", return_value = "03:00"),\
        patch("builtins.input", side_effect = ["1", "Eat"]),\
        patch("todo_list2.save_todo_list") as mock_save:
        todo.create_list()
        mock_save.assert_called_with ({"01:00" : "Quiet Time", "02:00": "Sleep", "03:00": "Eat"})
        
    
        
