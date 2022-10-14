# DFF TODO World's worst service factory EVER!

from resources.student_data_service import StudentDataService
from resources.student_resource import StudentResource
from middleware.context import Context


class ServiceFactory:

    def __init__(self):

        self.services = dict()
        ctx = Context()

        db_info = ctx.get_context_variable("DB_CONNECT_INFO")
        c = {"DB_CONNECT_INFO": ctx.get_context_variable("DB_CONNECT_INFO")}
        sd = StudentDataService(c)
        c2 = {"data_service": sd}
        s = StudentResource(c2)

        self.services["students"] = s

    def get_service(self, s_name):
        result = self.services.get(s_name)
        return result

