import averages
import sys
# need to mock inputs here, overwrite them
def test_averages(capsys):
    averages.averages()
    # input = [1,2,3,4,5,6,7,8,9,'ten']
    assert capsys.readoutr().out == "45 9 5\n"


def fake_input(the_prompt):
    prompt_to_return_val = {
        'please enter a number: ': '6',
        'please, enter a value less then 5: ': '2',
    }
    val = prompt_to_return_val[the_prompt]
    return val

def test_input(monkeypatch):
    monkeypatch.setattr('builtins.input', fake_input)
    test = function()
    assert test == 2
    
# If you install the plugin pytest-mock
def test_input(mocker):
    mocker.patch('builtins.input', side_effect=[1,2,3,4,5,6,7,8,9,'ten'])
    averages.averages()
    assert capsys.readoutr().out == "45 9 5\n"