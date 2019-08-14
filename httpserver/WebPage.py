class WebPage:

    def head(self):
        return "<head>" + self.title() +"</head>"

    def body(self):
        return "<title>TITLE</title>"
    
    def title(self):
        return "<body><p>It Works!</p></body>"

    def html(self):
        return "<html>" + self.head() + self.body() + "</html>"
