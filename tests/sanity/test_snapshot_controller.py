#
# Copyright 2024 Canonical, Ltd.
# See LICENSE file for licensing details
#

from k8s_test_harness.util import docker_util, env_util


def test_snapshot_controller_rock():
    """Test snapshot-controller rock."""
    rock = env_util.get_build_meta_info_for_rock_version(
        "snapshot-controller", "6.3.3", "amd64"
    )
    image = rock.image

    # check binary.
    process = docker_util.run_in_docker(image, ["/snapshot-controller", "--help"])
    assert "Usage of /snapshot-controller" in process.stderr
