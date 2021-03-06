from testtool import test

test.assert_equals('foo'.upper(), 'FOO')
test.assert_not_equals('foo'.upper(), 'Foo')
test.assert_true('FOO'.isupper())
test.assert_false('FOO'.islower())
test.assert_is('FOO', str)
test.assert_is_not('FOO', int)
test.assert_is_none(None)
test.assert_is_not_none('FOO')
test.assert_in('FOO', ('FOO',"F"))
test.assert_not_in('FOO', ('F','G'))
test.assert_is_instance('FOO', str)
test.assert_is_not_instance('Foo', int)

test.run_test()
