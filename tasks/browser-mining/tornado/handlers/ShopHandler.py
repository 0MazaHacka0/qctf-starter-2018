from tornado.web import RequestHandler
from tornado import gen
from json import dumps
from db import DbHandler

class ShopHandler(RequestHandler):
    def initialize(self, flag):
        self.db = DbHandler.get_db()
        self.flag = flag
    
    @gen.coroutine
    def get(self):
        user = self.get_secure_cookie("user")
        if user:
            balance = yield self.db.get_balance(user.decode())
            self.render("shop.html", balance=balance)
        else:
            self.redirect("/login")  

    @gen.coroutine
    def post(self):
        user = self.get_secure_cookie("user").decode()
        flag, balance = yield self.db.get_flag(user)
        if flag:
            self.write(dumps({
                "flag" : self.flag,
                "balance" : balance
            }))
        else:
            self.write(dumps({
                "error" : "Недостаточно монет",
                "balance" : balance
            }))
