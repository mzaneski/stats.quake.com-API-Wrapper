import asyncio
import unittest
from qcapi import QCPlayer

class TestPlayerAPIAsync(unittest.TestCase):

    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def tearDown(self):
        self.loop.close()

    def test_get(self):
        result = self.loop.run_until_complete(QCPlayer.from_name_coro('phy1um'))
        self.assertIsInstance(result, QCPlayer)

    def test_rank(self):
        result = self.loop.run_until_complete(QCPlayer.from_name_coro('phy1um'))
        r = result.get_rank_value("duel")
        self.assertIsInstance(r, int)

    def test_async(self):
        async def __playerstats(name):
            player = await QCPlayer.from_name_coro(name)
            self.assertIsNotNone(player)
            self.assertEqual(player.model.name.lower(), name.lower())
            print(player.model.name)
            self.assertIsInstance(player.get_rank_value('duel'), int)
            print('  elo: ' + str(player.get_rank_value('duel')))
            self.assertIsInstance(player.get_level(), int)
            print('  lvl: ' + str(player.get_level()))
            self.assertIsInstance(player.get_experience(), int)
            print('  exp: ' + str(player.get_experience()))

        names = ['rapha', 'dahang', 'phy1um', 'mzULTRA']
        tasks = [__playerstats(n) for n in names]
        self.loop.run_until_complete(asyncio.wait(tasks))

if __name__ == '__main__':
    unittest.main()