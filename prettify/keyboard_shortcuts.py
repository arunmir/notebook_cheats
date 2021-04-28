import sys
sys.path.insert(0,'..')

from IPython.display import HTML
from output_printer import OutputPrinter


def import_style(path):
    HTML(''.format(open(path).read()))


@OutputPrinter.htmlout
def format_keys(keys,kb="mac"):
    cc = ""
    mac_keys = {'cmd':'⌘',
                'ctrl':'⌃',
                'option':'⌥',
                }
    win_keys = {'win':'⊞ Win',
                'ctrl':'Ctrl',
                'alt':'Alt'}
    key_replacements = {
        'shift':'⇧',
        'fun':'fn'
    }
    
    if kb == "mac":
        key_replacements.update(mac_keys)
    elif kb == "win":
        key_replacements.update(win_keys)
    

    output_keys  = []
    for k in keys:
        output_keys.append("<kbd>" + key_replacements.get(k,k) + "</kbd>")
        
    return " + ".join(output_keys)

@OutputPrinter.htmlout
def display_shortcut(key_comb, description):
    return "%s\t%s\n"%(format_keys(key_comb), description)

@OutputPrinter.htmlout
def display_shortcut_list(lst,kb="mac"):
    cc = ""
    cc += "<table>"
    cc += "<tr><th>Keys</th><th>Description</th></tr>"
    for sc in lst:
        cc += "<tr><td>%s</td><td>%s</td></tr>"% (format_keys(sc[0],kb),sc[1])
    cc += "</table>"
    return cc