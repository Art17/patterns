from program.program import *
from security.security import *
from writer.writer import *
from render.renderer import *

def main():
    s1 = PasswordSecurity("Hell")
    s2 = NoSecurity()

    p1 = Program(s1, "Computer secret 1")
    p2 = Program(s2, "Computer secret 2")

    print("Data from computer1: " + p1.get_data())
    print("Data from computer12: " + p2.get_data())

    r2 = AsteriskRenderer()
    w2 = Writer(r2)

    w2.write('ao')


if __name__ == "__main__":
    main()
