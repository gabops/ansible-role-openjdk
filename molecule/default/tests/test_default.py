import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_java_installed(host):
    distro = host.system_info.distribution
    version = host.system_info.release

    c = host.run("java -version 2>&1 | grep 'openjdk version'")
    if distro == "debian" and version.startswith("10"):
        assert "11.0" in c.stdout
    else:
        assert "1.8" in c.stdout
