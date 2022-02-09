import json


# For using JSON string directly as Python code
true, false, null = True, False, None

# To parse json automatically
class JSONParser:

    def __init__(self, template):
        kwargs = {w: [] for w in template.__code__.co_varnames}
        wanted = {id(kwargs[kw]): kw for kw in kwargs}       
        self.roadmaps, self.functions = {}, {}
        def dfs(tmp, path):
            if id(tmp) in wanted:
                self.roadmaps[wanted[id(tmp)]] = "".join(path)
                self.functions[wanted[id(tmp)]] = eval("lambda _:_" + "".join(path))
            elif type(tmp) == dict:
                for key, value in tmp.items():
                    path.append(f"['{key}']")
                    dfs(value, path)
            elif type(tmp) == list:
                for index, value in enumerate(tmp):
                    path.append(f"[{index}]")
                    dfs(value, path)
            if path: path.pop(-1)
        dfs(template(**kwargs), [])
    
    def get_wanted(self, obj=None, raw=None, file=None):
        assert obj or raw or file
        if file:
            with open(file, "r") as reader: 
                raw = reader.read()
        if raw:
            obj = json.loads(raw)
        if obj:
            return {variable: value(obj) for variable, value in self.functions.items()}
        else:
            return {}

