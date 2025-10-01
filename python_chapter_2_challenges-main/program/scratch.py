class PasswordManager():
    password_dict = {}
    def add(self, service, password):

        if len(password) < 8:
            print(f'{password} is not a valid password')
        
        elif '!' in password:
            self.password_dict[service] = password
        elif '@' in password:
            self.password_dict[service] = password
        elif '$' in password:
            self.password_dict[service] = password
        elif '%' in password:
            self.password_dict[service] = password
        elif '&' in password:
            self.password_dict[service] = password
        else:
            print(f'{password} is not a valid password')
        
    def get_for_service(self, service):
        return self.password_dict.get(service)
    
    def list_services(self):

        return list(self.password_dict.keys())


invalid_test = PasswordManager()

invalid_test.add('aceplay', '12345678!')
invalid_test.add("willslazerpalace", "12345678@")
invalid_test.add("makerbnb", "12345$678")
invalid_test.add("discgolfuk", "12345678%")
invalid_test.add("deathmetalforcats", "12345678&")

# subject.add('sky', '1230Romeen!')
# subject.add('sky', '1230R')
# subject.add('sky', '1230Romeen12301230')
invalid_test.add('service1', '1234567')
print(invalid_test.list_services())
print(invalid_test.get_for_service('service1'))


invalid_test.add('service2', '1234567!')
print(invalid_test.list_services())
print(invalid_test.get_for_service('service2'))

invalid_test.add('service_3', '12345678')
invalid_test.add('service_4', '!@$%&')
print(invalid_test.list_services())
