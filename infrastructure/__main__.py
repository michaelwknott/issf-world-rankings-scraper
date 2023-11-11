"""A DigitalOcean Python Pulumi program."""
import os

from dotenv import load_dotenv
import pulumi
import pulumi_digitalocean as do


load_dotenv()
domain_name = os.getenv("DOMAIN_NAME")
new_user = os.getenv("NEW_USER")
ssh_key = os.getenv("SSH_KEY")
trusted_ip = os.getenv("TRUSTED_IP")

# Create a DigitalOcean resource (Domain)
domain = do.Domain("issf-world-rankings-domain", name=domain_name)

# Create a DigitalOcean resource (Droplet)
droplet = do.Droplet(
    "issf-world-rankings",
    image="ubuntu-20-04-x64",
    region="lon1",
    size="s-1vcpu-1gb",
    user_data=f"""#cloud-config
    users:
      - name: {new_user}
        sudo: ['ALL=(ALL) NOPASSWD:ALL']
        groups: sudo
        shell: /bin/bash
        ssh-authorized-keys:
          - {ssh_key}
        disable_root: true
    """,
)

# Create a DigitalOcean resource (Firewall)
firewall = do.Firewall(
    "my-firewall",
    inbound_rules=[
        do.FirewallInboundRuleArgs(
            protocol="tcp",
            port_range="22",  # SSH port
            source_addresses=[trusted_ip],  # replace with your trusted IPs
        )
    ],
    droplet_ids=[droplet.id],
)

# Export the name of the domain
pulumi.export("domain_name", domain.name)

# Export the IPv4 address of the droplet
pulumi.export("droplet_ip", droplet.ipv4_address)
