# Repo with ansible playbooks
- ## Basic server setup: 
   - Playbook: `basic_server_setup.yml`

- ## Install VPNs and proxies:
   - Playbook: `vpn.yml`  
   - Check `outline-server-<ip>-info.log` files for manager credentials after playbook execution

# How to use:
1. Install ansible
2. Install roles dependencies:
   ```sh
   ansible-galaxy install -p dependent-roles -r requirements.yml
   ```
3. Prepare hosts (e.g. setup ssh access with key) and upload your public key in your github repo
4. Adjust variables
   - `group_vars/all`
   - `ansible.cfg`
   - Create file `hosts` with required host groups
5. Run playbook
   ```sh
   ansible-playbook basic_server_setup.yml --private-key=$SSH_KEYPATH
   ```
