import os
import unittest

if __name__ == '__main__':
    # Define o diretório raiz dos seus testes
    # estão em uma subpasta como 'tests/'
    test_root_dir = os.path.dirname(os.path.abspath(__file__))
    print(test_root_dir)# Pega o diretório onde 'run.py' está

    test_loader = unittest.TestLoader()

    # Ele irá recursivamente encontrar todos os testes nos subdiretórios
    all_tests_suite = test_loader.discover(start_dir=test_root_dir, pattern='test_*.py')

    unittest.TextTestRunner(verbosity=2).run(all_tests_suite)