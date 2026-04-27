class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(left, right, curr):
            if left == 0 and right == 0:
                res.append(curr)
                return
            if right > 0:
                helper(left, right - 1, ')' + curr)
            if left > right:
                helper(left - 1, right, '(' + curr)
        helper(n, n, "")
        return res
