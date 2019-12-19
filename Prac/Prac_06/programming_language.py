class ProgrammingLanguage:
    """Express information about the programming language"""

    def __init__(self, Field, Typing, Reflection, Year):
        """Define programs that express a programming language"""
        self.Field = Field
        self.Typing = Typing
        self.Reflection = Reflection
        self.Year = Year

    def __str__(self):
        """Return and express language"""
        return "{},{} Typing, Reflection = {}, First appeared in {}".format(self.Field, self.Typing, self.Reflection,
                                                                            self.Year)

    def is_dynamic(self):
        """Returns whether the language is dynamically typed"""
        return self.Typing == "Dynamic"


def main():
    """Run the following program"""
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    c_PlusPlus = ProgrammingLanguage("C++", "Static", True, 1983)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [java, c_PlusPlus, ruby, python, visual_basic]
    print(java)
    print(c_PlusPlus)
    print(ruby)
    print(python)
    print(visual_basic)

    print("The dynamically typed languages are:")
    for i in languages:
        if i.is_dynamic():
            print(i.Field)


if __name__ == "__main__":
    main()
