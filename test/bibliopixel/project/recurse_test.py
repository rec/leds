import json, unittest
from bibliopixel.project import fields, recurse
from bibliopixel import colors


class Tester:
    @staticmethod
    def fix_fields(x):
        for k, v in x.items():
            if k != 'typename' and isinstance(v, str):
                x[k] = 'post-' + x[k]

    @staticmethod
    def children(x):
        return ('foo', x),


class RecurseTest(unittest.TestCase):
    def test_empty(self):
        self.assertEquals(recurse.fix({}), {})

    def test_trivial(self):
        self.assertEquals(recurse.fix({'a': {}}), {'a': {}})

    fix_fields = staticmethod(fields.CONVERTER)

    def test_simple(self):
        source = {'datatype': RecurseTest, 'foo': 'bar', 'color': 'red'}
        expected = {'datatype': RecurseTest, 'foo': 'bar', 'color': colors.Red}
        self.assertEquals(expected, recurse.fix(source))

    def test_complex(self):
        source = {
            'typename': '%s.%s' % (Tester.__module__, Tester.__name__),
            'foo': {'datatype': RecurseTest, 'foo': 'bar', 'color': 'red'},
            'bing': 'bang',
        }
        expected = {
            'typename': '%s.%s' % (Tester.__module__, Tester.__name__),
            'datatype': Tester,
            'foo': {'datatype': RecurseTest, 'foo': 'bar', 'color': colors.Red},
            'bing': 'post-bang',
        }
        self.assertEquals(expected, recurse.fix(source))