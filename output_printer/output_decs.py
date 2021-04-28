import pyperclip as pyperclip
from IPython.display import HTML

class OutputPrinter:
    @staticmethod
    def htmlout(func):
        def wrapper(*args, **kwargs):
            oHTML = kwargs.pop('oHTML', False)
            output = func(*args, **kwargs)
            if oHTML:
                return HTML(output)
            return output
        return wrapper    
    
    @staticmethod
    def print_o_copy(func):
        def wrapper(*args, **kwargs):
            o_print = kwargs.pop('oPrint', False)
            o_copy = kwargs.pop('oCopy', False)
            output = func(*args, **kwargs)
            if o_print:
                print(output)
            if o_copy:
                pyperclip.copy(output)
            return output

        return wrapper

    @staticmethod
    def print_enumerated_list(func):
        def wrapper(*args, **kwargs):
            o_print = kwargs.pop('oPrint', False)
            o_copy = kwargs.pop('oCopy', False)
            lst = func(*args, **kwargs)
            if o_print:
                out = ""
                for i, item in enumerate(lst):
                    out += ("%s\t%s\n" % (i, item))
                print(out)

            if o_copy:
                out = ""
                for i, item in enumerate(lst):
                    out += ("%s\t%s\n" % (i, item))
                pyperclip.copy(out)

            return lst

        return wrapper
