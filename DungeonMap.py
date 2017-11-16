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

class MultiPointer():
    def __init__(self, value):
        self.pointer = value
        self.indirect = True

    def access(self):
        return self.pointer if self.indirect else self.pointer.access()

    def redirect(self, other):
        self.pointer = other
        self.indirect = False

    def parent_pointer(self):
        return self if self.indirect else self.pointer.parent_pointer()

class Areas:
    def __init__(self):
        self.areas = dict()

    def add_connection(self, fr, to):
        ptr1 = self.areas.setdefault(fr, MultiPointer({fr})).parent_pointer()
        ptr2 = self.areas.setdefault(to, MultiPointer({to})).parent_pointer()
        if ptr1 is ptr2:
            return
        result_set = ptr1.access()
        result_set |= ptr2.access()
        ptr2.redirect(ptr1)

    def isreachable(self, start, end):
        from_ptr = self.areas.get(start, None)
        return from_ptr is not None and end in from_ptr.access()

    def print_areas(self):
        for i in self.areas:
            print(i, self.areas[i].access())
            print("########################################")

if __name__ == "__main__":
    ir = InputReader()
    areas = Areas()
    for fr, to in ir.edges():
        areas.add_connection(fr, to)

    enter, exit = ir.end_points()
    print("YES" if areas.isreachable(enter, exit) else "NO")


