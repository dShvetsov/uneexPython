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
        self.areas = []

    def add_connection(self, conn):
        new_area = conn.copy()
        replacing_areas = []
        for area in self.areas:
            if conn & area:
                new_area |= area
            else:
                replacing_areas.append(area)
        self.areas = replacing_areas
        self.areas.append(new_area)

    def add_connection2(self, fr, to):
        new_area = set(fr, to)
        replacing_areas = []
        for area in self.areas:
            if fr in area or to in area:
                new_area |= area
            else:
                replacing_areas.append(area)
        self.areas = replacing_areas
        self.areas.append(new_area)

    def isreachable(self, conn):
        for area in self.areas:
            if area.issuperset(conn):
                return True
        return False

    def print_areas(self):
        for i in self.areas:
            print(i)

if __name__ == "__main__":
    ir = InputReader()
    areas = Areas()
    for fr, to in ir.edges():
        areas.add_connection(set((fr, to)))

    enter, exit = ir.end_points()
    print("YES" if areas.isreachable({enter, exit}) else "NO")


