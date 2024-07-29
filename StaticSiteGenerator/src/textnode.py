class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text=text
        self.text_type=text_type
        self.url=url

    def __eq__(TextNode1,TextNode2):
        if TextNode1.__dict__==TextNode2.__dict__:
            return True
        else:
            return False
        
    def __repr__(self):
        if self.url==None:
            return f"TextNode({self.text}, {self.text_type})"
        else:
            return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def main():
    text='This is a text node'
    text_type='bold'
    url='http://www.boot.dev'
    text_node=TextNode(text=text,text_type=text_type,url=url)
    text_node_text=text_node.__repr__()
    return print(text_node_text)

if __name__=="__main__":
    main()