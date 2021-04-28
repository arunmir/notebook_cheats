from output_printer import OutputPrinter


@OutputPrinter.print_o_copy
def sys_cd(path):
    return "cd \"{path}\"\n".format(path=path)


@OutputPrinter.print_o_copy
def sys_copy(src, dst,recursive=False):
    return "cp {r} {src} {dst}\n".format(src=src, dst=dst,r = "-r" if recursive else "")


@OutputPrinter.print_o_copy
def sys_zip(src, dst):
    return "zip -rvD \"{dst}\" \"{src}\" \n".format(src=src, dst=dst)


@OutputPrinter.print_o_copy
def sys_rm(parms, directory=False):
    return "rm {directory} \"{parms}\"\n".format(directory="-r" if directory else "",
                                                 parms=parms)

@OutputPrinter.print_o_copy
def sys_find_process_using_port(port):
    return f"sudo lsof -i :{port}\n"


@OutputPrinter.print_o_copy
def sys_open_finder(path):
    return "open -R \"{path}\" \n".format(path=path)


@OutputPrinter.print_o_copy
def sys_url_in_browser(url):
    return "open \"{url}\" \n".format(url=url)


@OutputPrinter.print_o_copy
def sys_link(link_file, link_target):
    cc = "ln -s \"{link_file}\" \"{link_target}\"\n".format(link_file=link_file, link_target=link_target)
    cc += "ls -l \"{link_file}\" \"{link_target}\"\n".format(link_file=link_file, link_target=link_target)
    return cc


@OutputPrinter.print_o_copy
def sys_text_editor(path):
    return "open -t \"{path}\" \n".format(path=path)


@OutputPrinter.print_o_copy
def sys_make_dir(path,intermediate_dirs = False):
    return "mkdir {interm} \"{path}\" \n".format(interm = "-p" if intermediate_dirs else "", path=path)


@OutputPrinter.print_o_copy
def sys_open_simple_webserver(port=8000):
    return f"python -m SimpleHTTPServer {port}\n"


@OutputPrinter.print_o_copy
def sys_python(script):
    return f"python {script}\n"

@OutputPrinter.print_o_copy
def sys_tar(outputname,files, **kwargs):
    toggle_keys_values = {'create':'c', 'file':'f','gzip':'z'}
    toggle_strs = ""

    for k,v in kwargs.items():
        if kwargs[k] == True:
            toggle_strs += toggle_keys_values[k]
    
    if toggle_strs!="":
        toggle_strs = "-" + toggle_strs
        
    src_files = " ".join(files)
    
    return f"tar {toggle_strs} {outputname} {src_files}\n"
