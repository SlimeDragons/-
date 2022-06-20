import unittest
import time
from page.announcement.look_announcement_page import Look
from case.login import login
from common.data import Data

class LookCase(unittest.TestCase):
    """查看公告"""

    @classmethod
    def setUpClass(cls) -> None:
        data = Data()
        ITEM = 'announcement'
        cls._annName = data.read_option(ITEM, 'title')
        cls.an = Look()
        time.sleep(1.5)
        cls.an.click_an()
        cls.an.click_lookan()
        cls.an.center_iframe()

    def tearDown(self) -> None:
        pass

    def test_1_look(self):
        self.an.input_title(self._annName)
        self.an.click_query()
        self.assertTrue(self.an.is_table(),"没有公告内容")
        self.an.click_look()
        self.an.rich_father_iframe()
        self.an.click_close()
        self.an.content_iframe()
        self.an.center_iframe()
        self.assertTrue(self.an.is_text(),"公告未能查看")


if __name__ == '__main__':
    unittest.main()
