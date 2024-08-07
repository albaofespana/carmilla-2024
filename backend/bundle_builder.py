import json
from backend.const import schedule as const

"""
: raise IOError: if an I/O operation fails (e.g. file not exists)
"""


def combine_bundle_js() -> None:
    with open(const.TOP_COMPONENT_FILE, 'r') as file:
        top_component = file.read()

    with open(const.SCHEDULE_JSON_FILE, 'r') as file:
        ip_ranges = json.load(file)['castings']

    with open(const.BOTTOM_COMPONENT_FILE, 'r') as file:
        bottom_component = file.read()

    with open(const.BUNDLE_JS_FILE, 'w') as file:
        file.write(top_component)

        for index, ip in enumerate(ip_ranges):
            is_last = False

            if index == len(ip_ranges) - 1:
                is_last = True

            formatted_ip = _format_json_to_str(ip, is_last)
            file.write(formatted_ip)

        file.write(bottom_component)


def _format_json_to_str(json_input: dict, is_last=False) -> str:
    s = ("    \"{\" \n +" +
         "\"      \\\"playDate\\\": \\\"" + json_input['playDate'] + "\\\", \" \n +" +
         "\"      \\\"playTime\\\": \\\"" + json_input['playTime'] + "\\\", \" \n +" +
         "\"      \\\"carmilla\\\": \\\"" + json_input['carmilla'] + "\\\", \" \n +" +
         "\"      \\\"laura\\\": \\\"" + json_input['laura'] + "\\\", \" \n +" +
         "\"      \\\"nick\\\": \\\"" + json_input['nick'] + "\\\", \" \n +" +
         "\"      \\\"spielsdorf\\\": \\\"" + json_input['spielsdorf'] + "\\\" \" \n +" +
         "\"   }, \" \n +"
         )

    if is_last:
        s = ("    \"{\" \n +" +
             "\"      \\\"playDate\\\": \\\"" + json_input['playDate'] + "\\\", \" \n +" +
             "\"      \\\"playTime\\\": \\\"" + json_input['playTime'] + "\\\", \" \n +" +
             "\"      \\\"carmilla\\\": \\\"" + json_input['carmilla'] + "\\\", \" \n +" +
             "\"      \\\"laura\\\": \\\"" + json_input['laura'] + "\\\", \" \n +" +
             "\"      \\\"nick\\\": \\\"" + json_input['nick'] + "\\\", \" \n +" +
             "\"      \\\"spielsdorf\\\": \\\"" + json_input['spielsdorf'] + "\\\" \" \n +" +
             "\"   } \" \n +"
             )
    return s
