# ip-control
Related files and scripts for home built linux router

Basic implementation takes configuration from Python dict and use Jinja for the iptables templating.  
Edit `iptables.py -> configuration` for custom settings.

Configuration Schema:
```python
configuration = {
    # Basic Network Configuration
    "network": {
        "wan": "enp3s0", # Internet In
        "lan": "enp4s0", # Internal Network (To a switch or AP)
    },
    # List of Port Forwards
    "port_forwards": [
        {
            "comment":  "Webserver",
            "src_port": "65536",     # Open Port on Router
            "dst_ip":   "10.10.0.1", # Internal Device IP
            "dst_port": "80",        # Internal Device Port
        },
    ],
    # List of Open Ports on Router
    "open_ports": [
        {
            "comment": "SSH", 
            "port":    "22",
        },
    ]
}
```

To run:
```bash
# Generate rules
python iptables.py > iptables
# Apply rules
iptables-restore < iptables
```


## Todo
- Support for passing in configuration from file as argument
- Support for passing in template from file as argument
- Support to apply rules with script
- Support to backup rules with script
- Validation on configuration
