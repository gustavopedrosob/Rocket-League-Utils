import pytest
from rl_data_utils.item.platform.constants import *
from rl_data_utils.item.platform.platform import Platform

pair_equals = [['pc', 'Pc'], ['ps4', 'Ps4'], ['xbox', 'Xbox'], ['switch', 'Switch']]


def test_from_random():
    print(Platform.create_random())


@pytest.mark.parametrize('platform', [PC, XBOX, SWITCH, PS4])
def test_is_platform(platform):
    assert Platform(platform).is_valid()


@pytest.mark.parametrize('platform_1,platform_2', pair_equals)
def test_compare_platform(platform_1, platform_2):
    assert Platform(platform_1).compare(Platform(platform_2))


@pytest.mark.parametrize('platform', ['pc'])
def test_is_pc(platform):
    assert Platform(platform).is_exactly(PC)


@pytest.mark.parametrize('platform', ['ps4', 'ps 4', 'play 4', 'playstation 4'])
def test_is_ps4(platform):
    assert Platform(platform).is_exactly(PS4)


@pytest.mark.parametrize('platform', ['xbox'])
def test_is_xbox(platform):
    assert Platform(platform).is_exactly(XBOX)


@pytest.mark.parametrize('platform', ['switch'])
def test_is_switch(platform):
    assert Platform(platform).is_exactly(SWITCH)
