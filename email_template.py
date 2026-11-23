from jinja2 import Template

def gerar_email_template(feedbacks):
    with open("template_email.html", encoding="utf-8") as f:
        template = Template(f.read())
    html_content = template.render(feedbacks=feedbacks)
    return html_content
