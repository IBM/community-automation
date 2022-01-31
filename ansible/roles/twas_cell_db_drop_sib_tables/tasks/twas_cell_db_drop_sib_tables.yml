---

- name: copy db2_drop_sib.py script
  copy:
   src: db2_drop_sib.py
   dest: "~/db2_drop_sib.py"
   mode: 0755

- name: run the db2_drop_sib.py script
  shell: "~/db2_drop_sib.py {{ db_name }}"
  register: dropSibOutput
  failed_when: ( dropSibOutput.rc not in [ 0, 255 ] )
- name: dropSibOutput
  debug:
   msg: "{{ dropSibOutput.stdout_lines }}"

