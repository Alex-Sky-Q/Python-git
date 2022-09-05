import contextlib
from datetime import datetime, timezone
from io import StringIO
import unittest
import sys
sys.path.append('../')
from tgc import func as f


class TestFunc(unittest.TestCase):
    def test_url_builder(self):
        self.assertTupleEqual(f.url_builder('sf'), ('https://skyfitness.ru', 'skyfitness.ru'))
        self.assertTupleEqual(f.url_builder('google.com'), ('https://google.com', 'google.com'))
        self.assertTupleEqual(f.url_builder('https://google.com'), ('https://google.com', 'google.com'))
        self.assertTupleEqual(f.url_builder('https://skyfitness.ru/complexes/no-xplode-20/'),
                              ('https://skyfitness.ru/complexes/no-xplode-20', 'skyfitness.ru'))
        self.assertTupleEqual(f.url_builder('skyfitness.ru/complexes/no-xplode-20/'),
                              ('https://skyfitness.ru/complexes/no-xplode-20', 'skyfitness.ru'))

    def test_syn_reader(self):
        self.assertEqual(f.syn_reader('sf'), 'skyfitness.ru')

    def test_syn_reader_out(self):
        sys.argv = ['', '']
        with self.assertRaises(SystemExit):
            f.syn_reader('unknown_syn')

    def test_run_command_unknown(self):
        printed_out = StringIO()
        with contextlib.redirect_stdout(printed_out):
            f.run_command('unknown_comm', 'site')
        self.assertEqual(printed_out.getvalue().strip(), f.UNKNOWN_COMM)

    def test_lxml_parser_date(self):
        check_date_now = datetime.now(timezone.utc)
        tags, check_date = f.lxml_parser('https://google.ru')
        self.assertTrue(check_date > check_date_now)

    def test_db_conn(self):
        self.assertTrue(f.db_conn())

    def test_db_reader(self):
        sys.argv = ['', '']
        printed_out = StringIO()
        with contextlib.redirect_stdout(printed_out):
            f.db_reader('no_rec')
        self.assertEqual(printed_out.getvalue().strip(), f.NO_REC_DB)


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main(verbosity=2)

# Files for testing
# with open("Tests/Test.html") as f:
#     soup = BeautifulSoup(f, "html.parser")
# with open("Tests/Test.html") as f:
#     page = html.fromstring(f.read())
