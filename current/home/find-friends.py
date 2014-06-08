def check_connection(network, first, second):
    def create_graph(netw):
        g = {}
        for rel in netw:
            p1, p2 = rel.split('-')
            if p1 in g:
                g[p1] += [p2]
            else:
                g[p1] = [p2]
            if p2 in g:
                g[p2] += [p1]
            else:
                g[p2] = [p1]
        return g
    def find_path(graph, n1, n2, path=[]):
        path += [n1]
        if n1 == n2:
            return path
        for n in graph[n1]:
            if n not in path:
                return find_path(graph, n, n2, path)
        return None
    return find_path(create_graph(network), first, second) != None


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
