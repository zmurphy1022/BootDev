class HTMLNode:
    def __init__(self,tag:str|None=None,value:str|None=None,children:list|None=None,props:dict|None=None):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_string=[]
        if self.props==None:
            return ""
        else:
            [html_string.append(f" {k}=\"{v}\"") for k,v in self.props.items()]
            return "".join(html_string)
    
    def __repr__(self):
        return f"""
                Tag: {str(self.tag)}
                Value: {str(self.value)}
                Children: {str(self.children)}
                Props: {str(self.props)}
                """




class LeafNode(HTMLNode):
    def __init__(self,tag:str|None,value:str,props=None):
        super().__init__(tag,value,None,props)


    def to_html(self):
        if self.value==None:
            raise ValueError('Invalid HTML: no value')
        if self.tag==None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"       

class ParentNode(HTMLNode):
    def __init__(self,tag:str|None,children:list,props=None):
        super().__init__(tag,None,children,props)

    def to_html(self):
        if self.tag==None:
            raise ValueError('Invalid HTML: no tag')
        if self.children==None:
            raise ValueError('Invalid HTML: no children')
        child_html=""
        for child in self.children:
            child_html+=child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>'
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    
