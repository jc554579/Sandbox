class ProgrammingLanguage:

    def __init__(self, field, typing, reflection, year):
        """Define programs that express a programming language"""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return and express language"""
        return "{},{} Typing, Reflection = {}, First appeared in {}".format(self.field, self.typing, self.reflection,
                                                                            self.year)

    def is_dynamic(self):
        """Returns whether the language is dynamically typed"""
        return self.typing == "Dynamic"


def main():
    """Run the following program"""
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    c_plus_plus = ProgrammingLanguage("C++", "Static", True, 1983)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [java, c_plus_plus, ruby, python, visual_basic]
    print(java)
    print(c_plus_plus)
    print(ruby)
    print(python)
    print(visual_basic)

    print("The dynamically typed languages are:")
    for i in languages:
        if i.is_dynamic():
            print(i.field)


if __name__ == "__main__":
    main()
