from output_printer import OutputPrinter

SSH_KEYFILE = '~.ssh/id_rsa'


class SSHConfig:
    username = 'blackbird'
    port = 22
    host = '127.0.0.1'


@OutputPrinter.print_o_copy
def set_keybased_authentication(config: SSHConfig):
    return 'ssh-copy-id -p {port} {user}@{host}\n'.format(
        user=config.username,
        port=config.port,
        host=config.host
    )

@OutputPrinter.print_o_copy
def ssh(**kwargs):
    title = kwargs.pop("title","new SSH")
    identity = kwargs.pop("identity_file",None)
    user = kwargs.pop("user",None)
    host = kwargs.pop("host")
    port = kwargs.pop("port",None)
    port_fwd = kwargs.pop("bind_address",None)
    
    cc = f"echo -n -e \"\\033]0;{title}\\007\"\n"
    
    cmd = "ssh"
    if identity is not None:
        cmd += f" -i {identity} "
        
    if port is not None:
        cmd += f" -p {port} "
        
    if user is not None:
        cmd += f" {user}@{host}"
    else:
        cmd += f" {host} "
    
    pfwd_str = ""
    if isinstance(port_fwd,int):
        port_fwd =[port_fwd]

    if port_fwd is not None:
        
        for pw in port_fwd:
            if isinstance(pw,int):
                pfwd_str += f"-L {pw}:localhost:{pw} "
            elif isinstance(pw,dict):
                pfwd_str += f"-L {pw['local_port']}:{pw['host']}:{pw['server_port']} "


            
        cmd += f" {pfwd_str}"

    cmd += "\n"
    cc += cmd
    return cc

@OutputPrinter.print_o_copy
def scp(**kwargs):
    
    recursive = kwargs.pop("recursive",None)
    identity = kwargs.pop("identity_file",None)
    from_user = kwargs.pop("from_user",None)
    from_host = kwargs.pop("from_host",None)
    from_path = kwargs.pop("from_path",None)
    to_user = kwargs.pop("to_user",None)
    to_host = kwargs.pop("to_host",None)
    to_path = kwargs.pop("to_path",None)
    
    cmd = "scp "
    if recursive is not None:
        cmd += f" -r"
    
    if identity is not None:
        cmd += f" -i {identity} "
              
    if from_host is not None:
        if from_user is not None:
            cmd += f" {from_user}@{from_host}:"
        else:
            cmd += f" {from_host}:"
    cmd += f"{from_path} "
    
    if to_host is not None:
        if to_user is not None:
            cmd += f" {to_user}@{to_host}:"
        else:
            cmd += f" {to_host}:"
    cmd += f"{to_path} "
    
   
    cmd += "\n"
    return cmd


# @OutputPrinter.print_o_copy
# def ssh_authentication(user,host,port, port_fwd=None):
#     pfwd_str = ""
#     if isinstance(port_fwd,int):
#         port_fwd =[port_fwd]

#     if port_fwd is not None:
#         for pw in port_fwd:
#             pfwd_str += f"-L {pw}:localhost:{pw} "


#     return 'ssh -p {port} {user}@{host} {port_fwd}\n'.format(
#         user=user,
#         port=port,
#         host=host,
#         port_fwd = pfwd_str
#     )


# @OutputPrinter.print_o_copy
# def scp_copy_to(user,host,port, src, dst):
#     return f'scp -P {port} {src} {user}@{host}:{dst}\n'


# @OutputPrinter.print_o_copy
# def scp_copy_from(user,host,port, src, dst):
#     return f'scp -P {port} {user}@{host}:{src} {dst}\n'
    