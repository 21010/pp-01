# in VS Code add "-s" to pytestArgs to see messages from stopwatch decorator

from poetry.decorators import stopwatch


@stopwatch
def test_stopwatch():
    assert True
