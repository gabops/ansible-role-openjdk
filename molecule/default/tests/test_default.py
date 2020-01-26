import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_java_installed(host):
    c = host.run("java -version 2>&1 | grep 'openjdk version'")

    assert "1.8" in c.stdout
