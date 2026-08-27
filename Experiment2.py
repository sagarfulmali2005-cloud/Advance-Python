# Decorator for bold text


def bold_text(func):
    def wrapper(text):
        return "**" + func(text) + "**"
    return wrapper


class Report:
    templates = {}

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def add_template(cls, name, template):
        cls.templates[name] = template

    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name)

    def __call__(self, template_name):
        template = self.get_template(template_name)

        if template:
            return template(self.title, self.content)
        else:
            return "Template does not exist."

    def __str__(self):
        return self.title + "\n" + self.content


def simple_template(title, content):
    return "\n" + title + "\n" + content


@bold_text
def fancy_title(title):
    return title


def fancy_template(title, content):
    return "\n" + fancy_title(title) + "\n" + "-" * 35 + "\n" + content


def main():

    Report.add_template("simple", simple_template)
    Report.add_template("fancy", fancy_template)

    report = Report(
        "Student Report",
        "The student has performed well in academics."
    )

    print("Simple Template:")
    print(report("simple"))

    print("\nFancy Template:")
    print(report("fancy"))

    print("\nUsing Report Object:")
    print(report)


if __name__ == "__main__":
    main()