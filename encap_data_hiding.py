class MyClass:
    def __init__(self, public, protected, private):
        self.__private = private
        self._protected = protected
        self.public = public

    # to access private fields, make a property
    @property
    def myprivatefield(self):
        return self.__private

    @myprivatefield.setter
    def myprivatefield(self, value):
        self.__private = value



if __name__ == '__main__':
    c = MyClass('Public', 'Protected', 'Private')
    print('My Public Attribute is {}'.format(c.public))
    print('My Protected Attribute is {} to encourage users not to use it out of the class.'.format(c._protected))
    print('My Private Attribute is Not Accessible Here.')

    c.myprivatefield = 'Updated Here'
    print('My Private Attribute is accessible throu the property: {}'.format(c.myprivatefield))
