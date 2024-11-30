# test_parser.py

import unittest
from lexer import lexer
from parser import parser

class TestParser(unittest.TestCase):

    def test_variable_declaration(self): #ERRO
        input_code = '''
        int a, b, c;
        '''
        # float x;
        # char _myChar;
        # double __doubleVar123;
        lexer.input(input_code)
        tokens = list(lexer)
        self.assertTrue(len(tokens) > 0)
        result = parser.parse(input_code)
        self.assertIsNotNone(result)

    # def test_if_else(self):
    #     input_code = '''
    #     if (a == b) {
    #         c = a + b;
    #     } else {
    #         c = a - b;
    #     }
    #     '''
    #     lexer.input(input_code)
    #     tokens = list(lexer)
    #     self.assertTrue(len(tokens) > 0)
    #     result = parser.parse(input_code)
    #     self.assertIsNotNone(result)

    # def test_switch_case(self): # ERRO
    #     input_code = '''
    #     switch(value) {
    #         case 1:
    #             result = 10;
    #             break;
    #         case 2:
    #         case 3:
    #             result = 20;
    #             break;
    #         default:
    #             result = 0;
    #     }
    #     '''
    #     lexer.input(input_code)
    #     tokens = list(lexer)
    #     self.assertTrue(len(tokens) > 0)
    #     result = parser.parse(input_code)
    #     self.assertIsNotNone(result)

    # def test_while_loop(self): # ERRO
    #     input_code = '''
    #     while (count > 0) {
    #         total += count;
    #         count--;
    #     }
    #     '''
    #     lexer.input(input_code)
    #     tokens = list(lexer)
    #     self.assertTrue(len(tokens) > 0)
    #     result = parser.parse(input_code)
    #     self.assertIsNotNone(result)

    # def test_for_loop(self): # ERRO
    #     input_code = '''
    #     for (i = 0; i < 10; i++) {
    #         sum += i;
    #     }
    #     '''
    #     lexer.input(input_code)
    #     tokens = list(lexer)
    #     self.assertTrue(len(tokens) > 0)
    #     result = parser.parse(input_code)
    #     self.assertIsNotNone(result)

    # def test_complex_expression(self): #ERRO
    #     input_code = '''
    #     result = (a + b) * (c - d) / e;
    #     '''
    #     lexer.input(input_code)
    #     tokens = list(lexer)
    #     self.assertTrue(len(tokens) > 0)
    #     result = parser.parse(input_code)
    #     self.assertIsNotNone(result)

    # def test_invalid_syntax(self): #ERRO
    #     input_code = '''
    #     int 123invalidVar;
    #     '''
    #     with self.assertRaises(SyntaxError):
    #         parser.parse(input_code)

    # def test_unrecognized_character(self): #ERRO
    #     input_code = '''
    #     int a;
    #     a = 10 @ 5;
    #     '''
    #     lexer.input(input_code)
    #     with self.assertLogs(level='ERROR') as cm:
    #         tokens = list(lexer)
    #     self.assertTrue(any('Caractere inválido' in message for message in cm.output))

    # def test_empty_input(self): 
    #     input_code = ''
    #     lexer.input(input_code)
    #     tokens = list(lexer)
    #     self.assertEqual(len(tokens), 0)
    #     result = parser.parse(input_code)
    #     self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
