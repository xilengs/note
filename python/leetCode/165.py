# 比较版本号
class Solution:
    def compareVersion(self, version1, version2):
        version1 = [x for x in version1.split('.')]
        version2 = [x for x in version2.split('.')]
        for x, y in zip(version1, version2):
            if int(x) < int(y):
                return -1
            elif int(x) > int(y):
                return 1

        if len(version1) == len(version2):
            return 0
        elif len(version1) < len(version2):
            if any(x.isdigit() and int(x) != 0 for x in version2[len(version1):]):
                return -1
            else:
                return 0
        else:
            if any(x.isdigit() and int(x) != 0 for x in version1[len(version2):]):
                return 1
            else:
                return 0

def test():
    s = Solution()
    print(s.compareVersion("1.2", "1.10"))
    print(s.compareVersion("1.01", "1.001"))
    print(s.compareVersion("1.0", "1.0.0.0"))
    print(s.compareVersion("1", "1.0.1"))

test()