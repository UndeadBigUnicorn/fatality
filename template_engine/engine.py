import re


class TemplateEngine:

    def __init__(self, templates):
        self.templates = templates

    def process_question(self, question):
        """
        Process user question and find the right answer for it
        :param question: string with a question
        :return: string with an answer
        """
        # lower case the question
        question = question.lower()
        # check each template
        for (template, answer) in self.templates:
            result = self.parse_template(template, question, answer)
            if result is not None:
                return result

    def parse_template(self, template, question, answer):

        if template.find("*") != -1:
            template = template.replace("*", "")

            # template is empty
            if not template:
                return answer

        if template.find("<c>") != -1:
            template = template.replace("<c>", "")
            # rf"((?:{template}\s))(\w+)
            pattern = re.compile(rf"((?:{template}\s))(\w+)")
            match = pattern.search(question)
            if match is None:
                return None

            match = match.group(0).replace(template, "").strip()
            return answer.replace("<c>", match)

        return answer
