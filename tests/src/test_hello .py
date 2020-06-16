from src.service.util import hello


class Test:

    def test(self):
        INP = 'Nam'

        EXP = 'Hello Nam!'

        # testee code
        ACT = hello(INP)

        assert ACT == EXP
