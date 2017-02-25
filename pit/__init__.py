from pit.utils.logger import DJLogger
import pit.test.test_logger as test_logger


def joke():
    return (u'Wenn ist das Nunst\u00fcck git und Slotermeyer? Ja! ... '
            u'Beiherhund das Oder die Flipperwaldt gersput.')


def test():
    logger = DJLogger.getLogger()
    logger.debug(test_logger)
