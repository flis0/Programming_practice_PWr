# Szymon Flis 280153 @flis0

import unittest
from Test_driven_development.solution_1 import Add


class TestMyMethods ( unittest.TestCase ):
    def test_empty( self ):
        self.assertEqual( Add('') , 0)

    def test_one_num( self ):
        self.assertEqual( Add('1') , 1)
        self.assertEqual( Add('5') , 5)
        self.assertEqual( Add('27') , 27)
        
    def test_two_nums( self ):
        self.assertEqual( Add('1,6') , 7)
        self.assertEqual( Add('5,36') , 41)
        self.assertEqual( Add('27,32') , 59)
        self.assertEqual( Add('927,586') , 1513)
        self.assertEqual( Add('33114,134') , 33248)
        self.assertEqual( Add('4,26537') , 26541)

    def test_multiple_nums( self ):
        self.assertEqual( Add('1,6,5,3') , 15)
        self.assertEqual( Add('5,36,46') , 87)
        self.assertEqual( Add('27,32,0.123') , 59.123)
        self.assertEqual( Add('927,586,0.000001,0.000001,0.000001') , 1513.000003)
        self.assertEqual( Add('33114,134,-12.46584') , 33235.53416)
        self.assertEqual( Add('-4,12,0.34563,-0.000005') , 8.345625)

    def test_valueerror( self ):
        with self.assertRaises(ValueError):
            Add('1,2,f,4,5')
            Add('243,243,234,/')
            Add('74,$,%,423')
            Add('45,nieliczba,094')
            Add('243, 2 2 , 423')

    def test_newline( self ):
        self.assertEqual( Add('1\n6') , 7)
        self.assertEqual( Add('5\n36') , 41)
        self.assertEqual( Add('927\n586,0.000001,0.000001\n0.000001') , 1513.000003)
        self.assertEqual( Add('33114,134\n-12.46584') , 33235.53416)
        self.assertEqual( Add('-4,12\n0.34563\n-0.000005') , 8.345625)

unittest.main()