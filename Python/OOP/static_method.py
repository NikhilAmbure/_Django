class Employee:

    @staticmethod
    # we cannot use self here
    # No need to pass parameter
    def demo_static_method():
        print('Static Method')
    
Employee.demo_static_method()