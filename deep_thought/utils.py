"utility functions"

def dumps(obj, ensure_ascii=True):
    """Serialize ``obj`` to a JSON formatted :class:`str`.

    For example:

    >>> from deep_thought.utils import dumps
    >>> data = dict(spam=1, ham='egg')
    >>> dumps(data)
    '{spam: 1, ham: "egg"}'

    :param dict obj: dict type object to serialize.
    :param bool ensure_ascii: Default is True. If
       False, all non-ASCII characters are not ...
    :return: JSON formatted string
    :rtype: str

    """
    return 'to-be-implemented'


def spam():
    """SPAM SPAM SPAM"""
    return ''


def ham():
    """HAM HAM HAM"""
    return ''


def egg():
    return ''

