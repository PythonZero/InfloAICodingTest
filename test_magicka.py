import pytest

from magicka import Magicka


def test_check_combine():
    elements = 'RRQR'
    combine = 'QRI'
    assert 'RIR' == Magicka._check_combine(elements, combine)


def test_check_oppose():
    elements = 'FAQFDF'
    oppose = 'QF'
    assert 'FDF' == Magicka._check_oppose(elements, oppose)


@pytest.mark.skip('get a example in')
def test_invoke_only_elements():
    combine = ''
    oppose = ''
    elements = 'EA'
    assert 'EA' == Magicka.invoke(combine, oppose, elements)


def test_iterator():
    input = 'ABCDEFGHIJK'
    combine = 'ADT'
    oppose = 'XY'
    expected_out = Magicka.iterator(input, oppose, combine)
    assert expected_out == input