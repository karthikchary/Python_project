class account:
    def check_password_length(self, password):
        if len(password) > 8:
            return True
        else:
            return False

if __name__ == '__main__':
    accVerify = account()
    print('Acoount pyhton file')
    print('The password length is fair' + str(accVerify.check_password_length('offtoschool')))
