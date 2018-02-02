
- name: Create a10_slb_template_persist_cookie example playbook
  connection: local
  hosts: localhost
  tasks:
  - name: Create a10_slb_template_persist_cookie instance
    a10_slb_template_persist_cookie:
      a10_host: "{{ a10_host }}"
      a10_username: "{{ a10_username }}"
      a10_password: "{{ a10_password }}"
      name: sg-cookie-persist
      cookie_name: thecookie
