class HTMLNode:
    def __init__(self,tag:str|None=None,value:str|None=None,children:list|None=None,props:dict|None=None):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_string=''
        if self.props==None:
            return None
        else:
            for k,v in self.props.items():
                html_string+=f" {k}=\"{v}\""
            return html_string
    
    def __repr__(self):
        return f"""
                Tag: {str(self.tag)}
                Value: {str(self.value)}
                Children: {str(self.children)}
                Props: {str(self.props)}
                """
