class Todo:
    def __init__(self,id:int,title:str,done=False):
        self.id = id
        self.title = title
        self.done = done

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "done": self.done
        }

    def __repr__(self):
        return f"Todo(id={self.id}, title='{self.title}', done={self.done})"
    
sample = Todo(10, "山田", True)
print(sample.to_dict())