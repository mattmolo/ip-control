from jinja2 import Environment, FileSystemLoader
import os

template = "iptables_template"

configuration = {
    "network": {
        "wan": "enp3s0",
        "lan": "enp4s0",
    },
    "port_forwards": [
        {
            "comment":  "Webserver",
            "src_port": "65536",
            "dst_ip":   "10.10.0.1",
            "dst_port": "80",
        },
    ],
    "open_ports": [
        {
            "comment": "SSH",
            "port":    "22",
        },
    ]
}

curr_dir = os.path.dirname(os.path.abspath(__file__))
j2_env = Environment(loader=FileSystemLoader(curr_dir), trim_blocks=True)

print j2_env.get_template(template).render(configuration)
