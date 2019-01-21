#管理员类
class Manager:

    #menu即为视图
    menu = {
        '创建讲师账号': '',
        '创建学生账号': '',
        '创建课程': '',
        '创建班级': '',
    }

    def __init__(self,name, ID):
        self.name = name
        self.ID = ID

    def createTeacher(self):
        pass
    def createStudent(self):
        pass
    def createCourse(self):
        pass
    def createClass(self):
        pass