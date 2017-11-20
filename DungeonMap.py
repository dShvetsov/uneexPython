#!/usr/bin/env python3


# Вводится карта проходимых в обе стороны тоннелей подземлья в виде строк,
# содержащих разделённые пробелом названия двух пещер, которые соединяет соответствующий тоннель.
# Две последние строки не содержат пробелов — это название входа в подземелье и название выхода.
# Вывести "YES", если из входа можно попасть в выход, и "NO" в противном случае.
# Пары могут повторяться или содержать одинаковые слова.
# Input:
#
# markers jumping
# jumping guinea
# skiing pre
# markers gauge
# skiing mpeg
# solar jackson
# skiing solar
# guinea gauge
# mpeg honor
# pre honor
# guinea gauge
# pre mpeg
# markers guinea
# markers gauge
# honor mpeg
# markers jumping
# skiing
# jumping
#
# Output:
#
# NO

class InputReader :
    def __init__(self):
        self.nextline = input()

    def edges(self):
        while self.__is_edge(self.nextline):
            yield self.__extract_edge(self.nextline)
            self.nextline = input()
    def end_points(self):
        assert not self.__is_edge(self.nextline), "Not all edges was read"
        fr = self.nextline
        to = input()
        return fr, to

    def __is_edge(self, line):
        return ' ' in line

    def __extract_edge(self, line):
        ret = line.split()
        assert len(ret) == 2, "invalid input string"
        return ret

class Areas:
    def __init__(self):
        self.areas = dict()

    def add_connection(self, fr, to):
        s1 = self.areas.setdefault(fr, {fr})
        s2 = self.areas.setdefault(to, {to})
        s1.add(to)
        s2.add(fr)

    def close(self, what, predicat):
        s = self.areas.get(what)
        if s is None: return False, None
        while True:
            closed_set = s.copy()
            for i in s:
                closed_set |= self.areas[i]
            if predicat(closed_set):
                return True, closed_set
            if s == closed_set :
                break
            s = closed_set
        return False, s


    def isreachable(self, start, end):
        pred = lambda s : end in s
        res, close_set = self.close(start, pred)
        return res

#    def print_areas(self):
#        for i in self.areas:
#            print(i, self.areas[i].access())
#            print("########################################")

if __name__ == "__main__":
    ir = InputReader()
    areas = Areas()
    for fr, to in ir.edges():
        areas.add_connection(fr, to)

    enter, exit = ir.end_points()
    print("YES" if areas.isreachable(enter, exit) else "NO")


