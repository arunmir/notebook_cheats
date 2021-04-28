import os

from output_printer import OutputPrinter
from pkg_resources import resource_stream
from system_tool_set import system as tss


@OutputPrinter.print_o_copy
def git_pull(remote,branch):
    return f"git pull \"{remote}\" \"{branch}\"\n"


@OutputPrinter.print_o_copy
def git_clone(giturl):
    return "git clone \"{giturl}\"\n".format(giturl=giturl)


@OutputPrinter.print_o_copy
def git_add_remote(name, giturl):
    return "git remote add {name} \"{giturl}\"\n".format(name=name, giturl=giturl)


@OutputPrinter.print_o_copy
def git_add(arg):
    return "git add {arg}\n".format(arg=arg)


@OutputPrinter.print_o_copy
def git_commit(msg):
    return "git commit -m \"{msg}\"\n".format(msg=msg)


@OutputPrinter.print_o_copy
def git_merge_branch(from_branch,to_branch):
    cc = f"git checkout {from_branch}\n"
    cc += f"git merge {to_branch}\n"
    return cc    

@OutputPrinter.print_o_copy
def git_new_branch(branch_name):
    cc = f"git checkout -b {branch_name}\n"
    return cc 

@OutputPrinter.print_o_copy
def git_push(remote="origin"):
    return "git push {remote}\n".format(remote=remote)


@OutputPrinter.print_o_copy
def git_create_standard_ignore(path, replace=False):
    git_ignore_path = os.path.join(path, ".gitignore")
    if (os.path.exists(git_ignore_path)) and (not replace):
        raise Exception("ignore file already exist")

    std_file = resource_stream("resources.system_toolset", "standard-gitignore.txt")
    with open(git_ignore_path, 'bw+') as fid:
        fid.write(std_file.read())
    std_file.close()

    return "#Git ignore file created in %s\n" % git_ignore_path
