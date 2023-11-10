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
domain = do.Domain("issf_world_rankings_domain", name=domain_name)

# Create a DigitalOcean resource (Droplet)
droplet = do.Droplet(
    "issf_world_rankings",
    image="ubuntu-20-04-x64",
    region="lon1",
    size="s-1vcpu-1gb",
    user_data=f"""#cloud-config
    runcmd:
      # Install Fail2Ban for SSH protection
      - apt-get update
      - apt-get install -y fail2ban
      - systemctl enable fail2ban
      - systemctl start fail2ban
      # Install Auditd for system auditing
      - apt-get install -y auditd
      # Set up a rule to monitor the auth.log file
      - echo '-w /var/log/auth.log -p wa -k auth_log' >> /etc/audit/rules.d/auth_log.rules
      - systemctl restart auditd
      # Set up a cron job to check for non-ssr user logins
      - echo '0 0 * * * root ausearch -k auth_log -m USER_LOGIN | grep -v "ssr" > /var/log/non_ssr_logins.log' >> /etc/crontab
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
