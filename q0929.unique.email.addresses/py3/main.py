class Solution:
    def numUniqueEmails(self, emails) -> int:
        ans = set()

        for e in emails:
            localdomain = e.split('@')
            local = localdomain[0].split("+")
            local = local[0].replace(".","")

            ans.add(local+"@"+localdomain[1])

        return len(ans)


def test_ex1():
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    ans = 2

    sol = Solution()
    assert ans == sol.numUniqueEmails(emails)

test_ex1()