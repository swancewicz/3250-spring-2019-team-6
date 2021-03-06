"""Unittest to be used with op_codes.py"""
import unittest
from unittest.mock import mock_open
 # from jvpm.utils import T_INT, T_FLOAT, T_LONG
from jvpm.op_codes import *


class TestOpCodes(unittest.TestCase):
    """Unittest for opcodes"""

    # def test_not_implemented(self):
    #   self.assertEqual(OpCodes().interpret(0), 'not implemented')
    #   with self.assertRaises(KeyError):
    #   OpCodes().interpret(1)

    def test_iadd_simple(self):
        """Tests iadd method"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(2)
        op_code.stack.append(2)
        op_code.add()
        self.assertEqual(op_code.pop_from_stack(), 4)

    def test_int_overflow_positive(self):
        """Tests for possible integer overflow"""
        op_code = OpCodes()
        op_code.type = T_INT
        self.assertRaises(ValueError, op_code.push_int_to_stack, 2147483648)

    def test_int_overflow_negative(self):
        """Tests for possible negative integer overflow"""
        op_code = OpCodes()
        op_code.type = T_INT
        self.assertRaises(ValueError, op_code.push_int_to_stack, -2147483649)

    def test_int_max_positive(self):
        """Tests that the possible max integer in java is allowed"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.push_int_to_stack(2147483647)
        self.assertEqual(op_code.stack.pop(), 2147483647)

    def test_int_min_negative(self):
        """Tests that the possible minimum integer in java is allowed"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.push_int_to_stack(-2147483648)
        self.assertEqual(op_code.stack.pop(), -2147483648)

    def test_iand_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(5)
        op_code.stack.append(3)
        op_code.opcode_and()
        self.assertEqual(op_code.stack.pop(), 1)

    def test_iconst_m1_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.const_m1()
        self.assertEqual(op_code.stack.pop(), -1)

    def test_iconst_0_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.const_0()
        self.assertEqual(op_code.stack.pop(), 0)

    def test_iconst_1_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.const_1()
        self.assertEqual(op_code.stack.pop(), 1)

    def test_iconst_2_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.const_2()
        self.assertEqual(op_code.stack.pop(), 2)

    def test_iconst_3_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.const_3()
        self.assertEqual(op_code.stack.pop(), 3)

    def test_iconst_4_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.const_4()
        self.assertEqual(op_code.stack.pop(), 4)

    def test_iconst_5_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.const_5()
        self.assertEqual(op_code.stack.pop(), 5)

    def test_idiv_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(2)
        op_code.stack.append(4)
        op_code.div()
        self.assertEqual(op_code.stack.pop(), 2)

    def test_imul_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(2)
        op_code.stack.append(4)
        op_code.mul()
        self.assertEqual(op_code.stack.pop(), 8)

    def test_ineg_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(5)
        op_code.neg()
        self.assertEqual(op_code.stack.pop(), -5)

    def test_ior_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(6)
        op_code.stack.append(2)
        op_code.opcode_or()
        self.assertEqual(op_code.stack.pop(), 6)

    def test_irem_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(3)
        op_code.stack.append(7)
        op_code.rem()
        self.assertEqual(op_code.stack.pop(), 1)

    def test_ishl_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(3)
        op_code.stack.append(8)
        op_code.shl()
        self.assertEqual(op_code.stack.pop(), 64)

    def test_ishr_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(3)
        op_code.stack.append(8)
        op_code.shr()
        self.assertEqual(op_code.stack.pop(), 1)

    def test_isub_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(2)
        op_code.stack.append(6)
        op_code.sub()
        self.assertEqual(op_code.stack.pop(), 4)

    def test_iushr_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(3)
        op_code.stack.append(8)
        op_code.shr()

    def test_ixor_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(7)
        op_code.stack.append(3)
        op_code.xor()
        self.assertEqual(op_code.stack.pop(), 4)

    def test_invoke_virtual(self):
        """Tests invokeVirtual method java/io/PrintStream with various inputs"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(7)
        self.assertEqual(op_code.invoke_virtual(
            "java/io/PrintStream.println:(I)V"), 7)
        op_code.stack.append(1)
        self.assertEqual(op_code.invoke_virtual(
            "java/io/PrintStream.println:(Z)V"), 'true')
        op_code.stack.append(0)
        self.assertEqual(op_code.invoke_virtual(
            "java/io/PrintStream.println:(Z)V"), 'false')
        op_code.stack.append("HelloWorld")
        self.assertEqual(op_code.invoke_virtual("java/io/PrintStream.println:"
                                                "(Ljava/lang/String;)V"), 'HelloWorld')
        self.assertRaises(NotImplementedError, op_code.invoke_virtual, "java/util/Stack.push:")

    def test_i2b_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(-128)
        op_code.convert_byte()
        self.assertEqual(op_code.stack.pop(), b'\x80')

    def test_i2b_simple_test(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(127)
        op_code.convert_byte()
        self.assertEqual(op_code.stack.pop(), b'\x7f')

    def test_i2b_show_error(self):
        """Tests that OverFlow error is thrown when the value is too large to be a byte"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(128)
        self.assertRaises(OverflowError, op_code.convert_byte)

    def test_show_error(self):
        """Tests that OverFlow error is thrown when the value is too small to be a byte"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(-129)
        self.assertRaises(OverflowError, op_code.convert_byte)

    def test_i2c_simple_test(self):
        """Tests that the number given returns as the correct char type"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(0)
        op_code.convert_char()
        self.assertEqual(op_code.stack.pop(), '\x00')

    def test_i2c_simple_test_2(self):
        """Tests that the number given returns as the correct char type"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(127)
        op_code.convert_char()
        self.assertEqual(op_code.stack.pop(), '\x7f')

    def test_i2c_simple_test_3(self):
        """Tests that the number given returns as the correct char type"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(65)
        op_code.convert_char()
        self.assertEqual(op_code.stack.pop(), 'A')

    def test_i2c_simple_test_4(self):
        """Tests that the number given returns as the correct char type"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(-128)
        self.assertRaises(ValueError, op_code.convert_char)

    def test_i2c_simple_test_5(self):
        """Tests that the number given returns as the correct char type"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(128)
        op_code.convert_char()
        self.assertEqual(op_code.stack.pop(), '\x80')

    def test_i2d_simple_test(self):
        """Tests that a double value in java is returned as a float"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(2 ** 20 - 1)
        op_code.convert_float()
        self.assertAlmostEqual(op_code.stack.pop(), 2 ** 20 - 1)

    def test_i2d_simple_test_2(self):
        """Tests that a double value in java is returned as a float"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(-2 ** 20)
        op_code.convert_float()
        self.assertAlmostEqual(op_code.stack.pop(), -2 ** 20)

    def test_i2f_simple_test(self):
        """Tests that an integer is returned as a float"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(2 ** 10 - 1)
        op_code.convert_float()
        self.assertAlmostEqual(op_code.stack.pop(), 2 ** 10 - 1)

    def test_i2f_simple_test_2(self):
        """Tests that an integer is returned as a float"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(-2 ** 10)
        op_code.convert_float()
        self.assertAlmostEqual(op_code.stack.pop(), -2 ** 10)

    def test_i2s_value_too_large(self):
        """Tests that a ValueError is thrown when trying to cast an integer that is too large
        to a short type"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(2 ** 16)
        self.assertRaises(ValueError, op_code.convert_short)

    def test_i2s_value_too_small(self):
        """Tests that a ValueError is thrown when trying to cast an integer that is too small
        to a short type"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(-2 ** 16 - 1)
        self.assertRaises(ValueError, op_code.convert_short)

    def test_i2l_value_too_large(self):
        """Tests that a ValueError is thrown when trying to cast an integer that is too large
        to a short type"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(2 ** 64)
        self.assertRaises(ValueError, op_code.convert_long)

    def test_i2l_value_too_small(self):
        """Tests that a ValueError is thrown when trying to cast an integer that is too small
        to a short type"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(-2 ** 64 - 1)
        self.assertRaises(ValueError, op_code.convert_long)

    def test_iload1_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.localvar.insert(1, 8)
        op_code.load_1()
        self.assertEqual(op_code.stack.pop(), 8)

    def test_iload0_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.localvar.insert(0, 8)
        op_code.load_0()
        self.assertEqual(op_code.stack.pop(), 8)

    def test_iload2_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.localvar.insert(2, 6)
        op_code.load_2()
        self.assertEqual(op_code.stack.pop(), 6)

    def test_iload3_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.localvar.insert(3, 4)
        op_code.load_3()
        self.assertEqual(op_code.stack.pop(), 4)

    def test_istore0_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(5)
        op_code.store_0()
        self.assertEqual(op_code.localvar[0], 5)

    def test_istore1_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(5)
        op_code.store_1()
        self.assertEqual(op_code.localvar[1], 5)

    def test_istore2_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(4)
        op_code.store_2()
        self.assertEqual(op_code.localvar[2], 4)

    def test_istore3_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(2)
        op_code.store_3()
        self.assertEqual(op_code.localvar[3], 2)

    def test_str_scanner_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        with unittest.mock.patch('builtins.input', return_value="Testing"):
            self.assertEqual(op_code.invoke_virtual(
                "java/util/Scanner.nextString:()Ljava.lang/String"), "Testing")

    def test_int_scanner_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_INT
        with unittest.mock.patch('builtins.input', return_value=2):
            assert op_code.invoke_virtual(
                "java/util/Scanner.nextInt:()I") == 2

    def test_float_scanner_simple(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_FLOAT
        with unittest.mock.patch('builtins.input', return_value=1.0):
            assert op_code.invoke_virtual("java/util/Scanner.nextDouble:()D") == 1.0

    def test_lshl(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(1)
        op_code.push_long_to_stack(5)
        op_code.shl()
        self.assertEqual(op_code.pop_long_from_stack(), 10)

    def test_lshl_neg(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(-1)
        op_code.push_long_to_stack(5)
        self.assertRaises(ValueError, op_code.shl)

    def test_lshl_zeros(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(0)
        op_code.push_long_to_stack(5)
        op_code.shl()
        self.assertEqual(op_code.pop_long_from_stack(), 5)

    def test_lshl_max(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(1)
        op_code.push_long_to_stack(2 ** 62 - 1)
        op_code.shl()
        self.assertEqual(op_code.pop_long_from_stack(), 2 ** 63 - 2)

    def test_lshl_min(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(1)
        op_code.push_long_to_stack(-(2 ** 62) + 1)
        op_code.shl()
        self.assertEqual(op_code.pop_long_from_stack(), -(2 ** 63 - 2))

    def test_lshl_long_neg(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(1)
        op_code.push_long_to_stack(-5)
        op_code.shl()
        self.assertEqual(op_code.pop_long_from_stack(), -10)

    def test_lshr(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(1)
        op_code.push_long_to_stack(3)
        op_code.shr()
        self.assertEqual(op_code.pop_long_from_stack(), 1)

    def test_lshr_neg(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(-1)
        op_code.push_long_to_stack(3)
        self.assertRaises(ValueError, op_code.shr)

    def test_lshr_zeros(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(0)
        op_code.push_long_to_stack(3)
        op_code.shr()
        self.assertEqual(op_code.pop_long_from_stack(), 3)

    def test_lshr_max(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(1)
        op_code.push_long_to_stack(2 ** 63 - 1)
        op_code.shr()
        self.assertEqual(op_code.pop_long_from_stack(), 2 ** 62 - 1)

    def test_lshr_min(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(1)
        op_code.push_long_to_stack(-(2 ** 63-1))
        op_code.shr()
        self.assertEqual(op_code.pop_long_from_stack(), -(2 ** 62))

    def test_push_pop_long(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(-(2 ** 63-1))
        self.assertEqual(op_code.pop_long_from_stack(), -(2 ** 63-1))

    def test_lshr_long_neg(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(1)
        op_code.push_long_to_stack(-3)
        op_code.shr()
        self.assertEqual(op_code.pop_long_from_stack(), -2)

    def test_ladd(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(1)
        op_code.push_long_to_stack(1)
        op_code.add()
        self.assertEqual(op_code.pop_long_from_stack(), 2)

    def test_ladd_negs(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(-1)
        op_code.push_long_to_stack(-1)
        op_code.add()
        self.assertEqual(op_code.pop_long_from_stack(), -2)

    def test_ladd_maximum(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(2 ** 63 - 2)
        op_code.push_long_to_stack(1)
        op_code.add()
        self.assertEqual(op_code.pop_long_from_stack(), (2 ** 63 - 1))

    def test_ladd_minimum(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(-(2 ** 63 - 2))
        op_code.push_long_to_stack(-1)
        op_code.add()
        self.assertEqual(op_code.pop_long_from_stack(), -(2 ** 63) + 1)

    def test_land(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(3)
        op_code.push_long_to_stack(2)
        op_code.opcode_and()
        self.assertEqual(op_code.pop_long_from_stack(), 2)

    def test_lconst_m1(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.const_m1()
        self.assertEqual(op_code.pop_long_from_stack(), -1)

    def test_lconst_0(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.const_0()
        self.assertEqual(op_code.pop_long_from_stack(), 0)

    def test_lconst_1(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.const_1()
        self.assertEqual(op_code.pop_long_from_stack(), 1)

    def test_lconst_2(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.const_2()
        self.assertEqual(op_code.pop_long_from_stack(), 2)

    def test_lconst_3(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.const_3()
        self.assertEqual(op_code.pop_long_from_stack(), 3)

    def test_lconst_4(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.const_4()
        self.assertEqual(op_code.pop_long_from_stack(), 4)

    def test_lconst_5(self):
        """As method name implies"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.const_5()
        self.assertEqual(op_code.pop_long_from_stack(), 5)

    def test_ldiv_0(self):
        """tests opcode ldiv (division with long)"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(0)
        op_code.push_long_to_stack(4)
        self.assertRaises(ZeroDivisionError, op_code.div)

    def test_ldiv(self):
        """tests opcode ldiv (division with long)"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(2)
        op_code.push_long_to_stack(4)
        op_code.div()
        self.assertEqual(op_code.pop_long_from_stack(), 2)

    def test_lmul(self):
        """Tests opcode lmul (multiply with long)"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(2)
        op_code.push_long_to_stack(4)
        op_code.mul()
        self.assertEqual(op_code.pop_long_from_stack(), 8)

    def test_lneg_neg_to_pos(self):
        """tests opcode lneg (long negative)"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(-1)
        op_code.neg()
        self.assertEqual(op_code.pop_long_from_stack(), 1)

    def test_lneg_pos_to_neg(self):
        """tests opcode lneg (long negative)"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(1)
        op_code.neg()
        self.assertEqual(op_code.pop_long_from_stack(), -1)

    def test_lor(self):
        """tests opcode lor (long or)"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(1)
        op_code.push_long_to_stack(8)
        op_code.opcode_or()
        self.assertEqual(op_code.pop_long_from_stack(), 9)

    def test_lrem(self):
        """tests opcode lrem works (long remainder)"""
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(5)
        op_code.push_long_to_stack(12)
        op_code.rem()
        self.assertEqual(op_code.pop_long_from_stack(), 2)
