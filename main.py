if __name__ == '__main__':
    with open('template-responses.txt', 'r') as templates_responses:
        templates = []
        for template in templates_responses.readlines():
            templates.append(tuple(template.split(':')))