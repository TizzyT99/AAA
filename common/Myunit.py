import unittest

from common.selenium_and_driver import logger, selenium_And_Driver

class MyUnit(unittest.TestCase):

    def setUp(self):
        logger.info("_______获取驱动________")
        self.driver = selenium_And_Driver()

    def tearDown(self):
        logger.info("_______测试完毕，驱动关闭________")
        self.driver.quit()

if __name__ == '__main__':
    MyUnit.main()
    