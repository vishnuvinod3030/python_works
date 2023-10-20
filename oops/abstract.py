# from abc import ABC,abstractmethod   # abc - abstract baseclass
# class car(ABC):

#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def accelerate(self):
#         pass


#     @abstractmethod
#     def stop(self):
#         pass

# class swift(car):

#     def start(self):
#         print("swift start method")

#     def accelerate(self):
#         print("swift accelerate method")

#     def stop(self):
#         print("stop method")


# obj=swift()
# obj.start()
# obj.accelerate()
# obj.stop()

#-----------------------------------------------------------------


from abc import ABC,abstractmethod
class editor(ABC):


    @abstractmethod
    def edit(self):
        pass

    def find_error(self):
        pass

    def debug(self):
        pass


class vscode(editor):

    def edit(self):
        print("vscode can edit")

    def find_error(self):
        print("find error")

    def debug(self):
        print("debug")

obj=vscode()
obj.edit()
obj.find_error()
obj.debug()