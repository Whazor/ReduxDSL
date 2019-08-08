import subprocess
import io
from textx import metamodel_from_file, get_children_of_type
from jinja2 import Template

redux_mm = metamodel_from_file('languages/redux/redux.tx')
redux_model = redux_mm.model_from_file('apps/counter/CountApp.rdx')

program = ""


actions = get_children_of_type('Action', redux_model)
reducers = get_children_of_type('Reducer', redux_model)
enums = get_children_of_type('Enum', redux_model)

rendered = Template(open('mcrl2.j2').read()) \
    .render(actions=actions, reducers=reducers, enums=enums)

print(rendered)