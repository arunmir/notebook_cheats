from ..output_printer import OutputPrinter
from .system import *

@OutputPrinter.print_o_copy
def docker_build(deploy_dir):
    cc = sys_cd(deploy_dir)
    cc += "docker-compose build\n"
    return cc

@OutputPrinter.print_o_copy
def docker_up(deploy_dir,background=False):
    cc = sys_cd(deploy_dir)
    cc += "docker-compose up {background}\n".format(background="-d" if background else "")
    return cc

@OutputPrinter.print_o_copy
def docker_stop(docker):
    return "docker stop {docker}\n".format(docker=docker)

@OutputPrinter.print_o_copy
def docker_start(docker):
    return "docker start {docker}\n".format(docker=docker)


@OutputPrinter.print_o_copy
def docker_remove(docker):
    return "docker rm {docker}\n".format(docker=docker)


@OutputPrinter.print_o_copy
def docker_exec(docker):
    return "docker exec -it {docker} /bin/bash\n".format(docker=docker)

