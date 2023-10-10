import unittest
import sys
sys.path.append("C:/Users/ghdau/Desktop/python_coding/python/Level_1")

# from score_of_memory import examine_dict
# from coke import examine_coke
# from 삼총사 import examine_musketeers
# from 푸드_파이트 import food_Fight
# from Handling_the_code import Handling_the_code
# from Push_the_str import push_the_str 
# from 바탕화면_정리 import Clean_up_your_desktop
# from Take_a_personality_test import Take_a_personality_test
# from 숫자_짝꿍 import 숫자_짝꿍
#from 과일장수 import 과일장수
#from 시저암호 import 시저암호
from 기능개발 import solution
class Test(unittest.TestCase):
    def test_dict(self):
        # answer1 = examine_dict(["kali", "mari", "don"],[11, 1, 55],[["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]])
        # answer2 = examine_dict(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])
        # self.assertEqual(answer1,[67, 0, 55])
        # self.assertEqual(answer2,[19, 15, 6])
        #self.assertEqual(examine_coke(3, 1, 20), 9)
        #self.assertEqual(examine_coke(2, 1, 20), 19)
        #self.assertEqual(examine_musketeers([-2, 3, 0, 2, -5]),2)
        #self.assertEqual(examine_musketeers([-3, -2, -1, 0, 1, 2, 3]),5)
        #self.assertEqual(food_Fight([1, 3, 4, 6]),"1223330333221")
        #self.assertEqual(food_Fight([1, 7, 1, 2]),"111303111")
        #self.assertEqual(Handling_the_code("abc1abc1abc"),"acbac")
        #self.assertEqual(push_the_str("hello","ohell"),1)
        #self.assertEqual(Clean_up_your_desktop([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]),[0, 0, 7, 9])
        #self.assertEqual(Take_a_personality_test(["AN", "CF", "MJ", "RT", "NA"],[5,3,2,7,5]),"TCMA")
        #self.assertEqual(숫자_짝꿍("100","123450"),"10")
        #self.assertEqual(과일장수(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]),33)
        #self.assertEqual(시저암호("a B z",4),"e F d")
        self.assertEqual(solution([93, 30, 55],[1, 30, 5]),[2,1])





if __name__ == '__main__':
    unittest.main()