import os

from output_printer import OutputPrinter


@OutputPrinter.print_enumerated_list
def find_pom_files(base_dir):
    pom_list = list()
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith("pom.xml"):
                pom_list.append(os.path.join(root, file))
    return pom_list


@OutputPrinter.print_enumerated_list
def get_components(base_dir):
    return [mvn.replace(base_dir, "").replace("pom.xml", "") for mvn in find_pom_files(base_dir)]


@OutputPrinter.print_o_copy
def compile(base_dir, component, clean=True, test=True, local=False):
    cc = ""
    cc += "cd \"{path}\"\n".format(path=os.path.join(base_dir, component))
    cc += "mvn {clean} {local} install {test}\n".format(
        clean="clean" if clean else "",
        test="-Dmaven.test.skip=true" if not test else "",
        local = "-o" if local else "")

    return cc


@OutputPrinter.print_o_copy
def migrate_jars(base_dir, component, deployment):
    target_dir = os.path.join(base_dir, component, "target")
    build_files = list()
    cc = ""
    if os.path.exists(target_dir)==False:
        cc+=f"echo {target_dir} missing\n"
        return cc
    
    for f in os.listdir(target_dir):
#         if os.path.isfile(os.path.join(target_dir, f)):
        build_files.append(f)
#     [f for f in os.listdir(target_dir) if os.path.isfile(os.path.join(target_dir, f))]
    jars = [f for f in build_files if f.endswith(".jar")]


    for jar in jars:
        cc += "cp {jar} {deployment}\n".format(jar=os.path.join(target_dir, jar),
                                               deployment=os.path.join(deployment, jar))

    return cc
