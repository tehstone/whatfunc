import copy

'''
function 'what' required applying object, expected result at least.
'''

def what(obj, expectedResult):
    MethodFinder.show(obj, expectedResult)

class MethodFinder(object):
    blacklist = ['daemonize' 'display' 'exec' 'exit' 'fork' 'sleep' 'system'
                 'syscall' 'what' 'ed' 'emacs' 'mate' 'nano' 'vi' 'vim']

    'required returning seaquenecial object'
    @classmethod
    def find(self, anObject, expectedResult):
        res = filter(lambda x: x not in self.blacklist, dir(type(anObject)))

        def calling(name):
            try:
                if getattr(copy.deepcopy(anObject), name)() is expectedResult:
                    return name
            except:
                return False
            return False

        res = filter(lambda x: calling(x), res)
        return res

    @classmethod
    def show(self, anObject, expectedResult):
        for name in self.find(anObject, expectedResult):
            print '''%s.%s == %s''' % (
                repr(anObject),
                name,
                repr(expectedResult))
