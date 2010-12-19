# ===========================================================================
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
# ===========================================================================

import sys, os, string, unittest, types
from System import DayOfWeek
from Python import Test


class EnumTests(unittest.TestCase):
    """Test CLR enum support."""

    def testEnumStandardAttrs(self):
        """Test standard enum attributes."""
        self.assertTrue(DayOfWeek.__name__ == 'DayOfWeek')
        self.assertTrue(DayOfWeek.__module__ == 'System')
        self.assertTrue(type(DayOfWeek.__dict__) == types.DictProxyType)
        self.assertTrue(DayOfWeek.__doc__ == None)


    def testEnumGetMember(self):
        """Test access to enum members."""
        self.assertTrue(DayOfWeek.Sunday == 0)
        self.assertTrue(DayOfWeek.Monday == 1)
        self.assertTrue(DayOfWeek.Tuesday == 2)
        self.assertTrue(DayOfWeek.Wednesday == 3)
        self.assertTrue(DayOfWeek.Thursday == 4)
        self.assertTrue(DayOfWeek.Friday == 5)
        self.assertTrue(DayOfWeek.Saturday == 6)


    def testByteEnum(self):
        """Test byte enum."""
        self.assertTrue(Test.ByteEnum.Zero == 0)
        self.assertTrue(Test.ByteEnum.One == 1)
        self.assertTrue(Test.ByteEnum.Two == 2)


    def testSByteEnum(self):
        """Test sbyte enum."""
        self.assertTrue(Test.SByteEnum.Zero == 0)
        self.assertTrue(Test.SByteEnum.One == 1)
        self.assertTrue(Test.SByteEnum.Two == 2)


    def testShortEnum(self):
        """Test short enum."""
        self.assertTrue(Test.ShortEnum.Zero == 0)
        self.assertTrue(Test.ShortEnum.One == 1)
        self.assertTrue(Test.ShortEnum.Two == 2)


    def testUShortEnum(self):
        """Test ushort enum."""
        self.assertTrue(Test.UShortEnum.Zero == 0)
        self.assertTrue(Test.UShortEnum.One == 1)
        self.assertTrue(Test.UShortEnum.Two == 2)


    def testIntEnum(self):
        """Test int enum."""
        self.assertTrue(Test.IntEnum.Zero == 0)
        self.assertTrue(Test.IntEnum.One == 1)
        self.assertTrue(Test.IntEnum.Two == 2)


    def testUIntEnum(self):
        """Test uint enum."""
        self.assertTrue(Test.UIntEnum.Zero == 0L)
        self.assertTrue(Test.UIntEnum.One == 1L)
        self.assertTrue(Test.UIntEnum.Two == 2L)


    def testLongEnum(self):
        """Test long enum."""
        self.assertTrue(Test.LongEnum.Zero == 0L)
        self.assertTrue(Test.LongEnum.One == 1L)
        self.assertTrue(Test.LongEnum.Two == 2L)


    def testULongEnum(self):
        """Test ulong enum."""
        self.assertTrue(Test.ULongEnum.Zero == 0L)
        self.assertTrue(Test.ULongEnum.One == 1L)
        self.assertTrue(Test.ULongEnum.Two == 2L)


    def testInstantiateEnumFails(self):
        """Test that instantiation of an enum class fails."""
        def test():
            ob = DayOfWeek()

        self.assertRaises(TypeError, test)


    def testSubclassEnumFails(self):
        """Test that subclassing of an enumeration fails."""
        def test():
            class Boom(DayOfWeek):
                pass

        self.assertRaises(TypeError, test)


    def testEnumSetMemberFails(self):
        """Test that setattr operations on enumerations fail."""
        def test():
            DayOfWeek.Sunday = 13
            
        self.assertRaises(TypeError, test)

        def test():
            del DayOfWeek.Sunday

        self.assertRaises(TypeError, test)


    def testEnumWithFlagsAttrConversion(self):
        """Test enumeration conversion with FlagsAttribute set."""
        from System.Windows.Forms import Label

        # This works because the AnchorStyles enum has FlagsAttribute.
        label = Label()
        label.Anchor = 99

        # This should fail because our test enum doesn't have it.
        def test():
            Test.FieldTest().EnumField = 99
            
        self.assertRaises(ValueError, test)


    def testEnumConversion(self):
        """Test enumeration conversion."""
        object = Test.FieldTest()
        self.assertTrue(object.EnumField == 0)

        object.EnumField = Test.ShortEnum.One
        self.assertTrue(object.EnumField == 1)

        def test():
            Test.FieldTest().EnumField = 20
            
        self.assertRaises(ValueError, test)

        def test():
            Test.FieldTest().EnumField = 100000
            
        self.assertRaises(OverflowError, test)

        def test():
            Test.FieldTest().EnumField = "str"
            
        self.assertRaises(TypeError, test)



def test_suite():
    return unittest.makeSuite(EnumTests)

def main():
    unittest.TextTestRunner().run(test_suite())

if __name__ == '__main__':
    main()

