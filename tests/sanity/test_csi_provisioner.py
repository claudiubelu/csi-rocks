#
# Copyright 2024 Canonical, Ltd.
# See LICENSE file for licensing details
#

from k8s_test_harness.util import docker_util, env_util


def test_csi_provisioner_rock():
    """Test csi-provisioner rock."""
    rock = env_util.get_build_meta_info_for_rock_version(
        "csi-provisioner", "4.0.0", "amd64"
    )
    image = rock.image

    # check binary.
    process = docker_util.run_in_docker(image, ["/csi-provisioner", "--help"], False)
    assert "Usage of /csi-provisioner" in process.stderr
