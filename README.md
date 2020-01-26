gabops.java_openjdk
=========
[![Build Status](https://travis-ci.org/gabops/ansible-role-java-openjdk.svg?branch=master)](https://travis-ci.org/gabops/ansible-role-openjdk)

Installs and configures OpenJDK.

Requirements
------------

None.

Role Variables
--------------

| Variable | Default value | Description |
| :--- | :--- | :--- |
| java_openjdk_version | 8 | Defines the OpenJDK version to install. |
| java_openjdk_home | "" | Defines the value for the JAVA_HOME environment variable. |
| java_openjdk_tool_options | "" | A set of options as string to be used as value for the `JAVA_TOOL_OPTIONS` environment variable. This allows you to set parameters globally. See `Example playbook` for more details. |

### Notes:
- Keep in mind that not all versions defined on `java_openjdk_version` will be available on the system you are targeting. The next table may help you:

| Distro | Version 6 | Version 7 | Version 8 | Version 9 | Version 10 | Version 11 | Version 12 | Version 13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **CentOS 6**       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: | :x: | :x: | :x: | :x: |
| **CentOS 7**       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: | :heavy_check_mark: | :x: | :x: | :x: |
| **CentOS 8**       | :x: | :x: | :heavy_check_mark: | :x: | :x: | :x: | :x: | :x: | :x: |
| **Amazon Linux 1** | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: | :x: | :x: | :x: | :x: |
| **Amazon Linux 2** | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: | :x: | :x: | :x: | :x: |
| **Debian 9**       | :x: | :x: | :heavy_check_mark: | :x: | :x: | :x: | :x: | :x: | :x: |
| **Debian 10**      | :x: | :x: | :x: | :x: | :x: | :heavy_check_mark: | :x: | :x: | :x: |
| **Ubuntu 16.04**   | :x: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| **Ubuntu 18.04**   | :x: | :x: | :heavy_check_mark: | :x: | :x: | :x: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: servers
  vars:
    java_openjdk_version: 11
    java_openjdk_tool_options: -Xms64M -Xmx256M -Djava.awt.headless=true
  roles:
      - role: gabops.java_openjdk
```

License
-------

[MIT]((./LICENSE))

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
