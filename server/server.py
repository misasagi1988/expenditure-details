import web

urls = (
    '/', 'index',
    '/blog', 'blog'
)

class index:
    def GET(self):
        return "get Hello, arcelan world!, dev branch."

    def POST(self):
        """ Add new entry """
        return "post Hello, world"

    def PUT(self):
        """ Add new entry """
        return "put Hello, meng_yujing!"

    def DELETE(self):
        """ Add new entry """
        return "delete Hello, world!"

class blog:
    def GET(self):
        return "get blog Hello, world!"

    def POST(self):
        """ Add new entry """
        return "post blog Hello, world!"

    def PUT(self):
        """ Add new entry """
        return "put blog Hello, meng_yujing!"

    def DELETE(self):
        """ Add new entry """
        return "delete blog Hello, world!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()