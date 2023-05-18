import sys
import os

# Adiciona o caminho para o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from test_login_success import TestLoginSuccess
from test_loggout import TestLoggoutSuccess

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLoginSuccess))
suite.addTest(unittest.makeSuite(TestLoggoutSuccess))


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)