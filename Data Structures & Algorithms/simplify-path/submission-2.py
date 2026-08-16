class Solution:
    def simplifyPath(self, path: str) -> str:
        filePath = path.split("/")
        results = []

        for path in filePath:
            if path == "" or path == ".":
                continue
            
            if path == "..":
                if results:
                    results.pop()
            else:
                results.append(path)
        
        return "/" + "/".join(results)