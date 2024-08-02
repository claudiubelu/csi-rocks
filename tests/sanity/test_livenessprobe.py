#
# Copyright 2024 Canonical, Ltd.
# See LICENSE file for licensing details
#

from k8s_test_harness.util import docker_util, env_util


def test_livenessprobe_rock():
    """Test livenessprobe rock."""
    rock = env_util.get_build_meta_info_for_rock_version(
        "livenessprobe", "2.12.0", "amd64"
    )
    image = rock.image

    # check binary.
    process = docker_util.run_in_docker(image, ["/livenessprobe", "--help"])
    assert "Usage of /livenessprobe" in process.stderr
