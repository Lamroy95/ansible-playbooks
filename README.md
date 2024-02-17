# Repo with ansible playbooks
- ## Basic server setup: 
   - Playbook: `basic_server_setup.yml`
   - Role `create-user-with-ssh-access` gets keys from Github repo. Upload your public key there and set `github_username` in `group_vars/all`

- ## Install VPNs and proxies:
   - Playbook: `vpn.yml`
   - Use host alias to set outline server name (e.g. in `hosts` file: `SOME_VPN ansible_host=1.2.3.4 ansible_ssh_private_key_file=...`)
   - Check `logs/outline/server-<host_alias>-access.log` files for manager credentials after playbook execution

# How to use:
1. Install ansible
2. Install roles dependencies, if required (see playbooks description above):
   ```sh
   ansible-galaxy install -r requirements.yml
   ```
3. Prepare hosts (e.g. setup ssh access with key or get username-pwd credentials) and upload your public key in your github repo
4. Adjust variables
   - `group_vars/*`
   - `ansible.cfg`
   - Create file `hosts` with required host groups (you can specify credentials per host here)
5. Run playbook
   ```sh
   ansible-playbook basic_server_setup.yml
   ```

## FAQ:
- If you are working in WSL Ansible can skip using `ansible.cfg` due to wide file permisions if this file is mounted from windows fs.  
   - You can adjust permissions (pain in the ass in WSL) or just set env var `ANSIBLE_CONFIG=ansible.cfg` before running the commands
- Same issue can appear with your ssh keys if they are mounted into WSL from windows.
   - Copy keys directly into WSL from mounted location or use different keys generated in WSL, not in windows.