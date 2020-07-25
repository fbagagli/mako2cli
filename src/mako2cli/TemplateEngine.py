import attr
from pathlib import Path
from mako.lookup import TemplateLookup
from mako.template import Template
from mako import exceptions


class TemplateEngineException(Exception):
    pass


@attr.s
class TemplateEngine():
    template = attr.ib(type=Template)

    @classmethod
    def initialize(cls,
                   template_filename=None,
                   template_directories_list=['.']):
        try:
            lookup = TemplateLookup(directories=template_directories_list)
            template = lookup.get_template(template_filename)
            return cls(template)
        except:
            print(exceptions.text_error_template().render())
            raise TemplateEngineException()

    def render(self, output_file_name, data):
        try:
            output_file = Path(output_file_name)
            output_file.write_text(self.template.render(**data))
        except:
            print(exceptions.text_error_template().render())
            raise TemplateEngineException()
