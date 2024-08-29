#
# Copyright 2024 Canonical, Ltd.
# See LICENSE file for licensing details
#

import pytest
from k8s_test_harness.util import docker_util, env_util


@pytest.mark.parametrize("image_version", ("2.12.0", "2.13.1"))
def test_livenessprobe_rock(image_version):
    """Test livenessprobe rock."""
    rock = env_util.get_build_meta_info_for_rock_version(
        "livenessprobe", image_version, "amd64"
    )
    image = rock.image

    # check binary.
    process = docker_util.run_in_docker(image, ["/livenessprobe", "--help"])
    assert "Usage of /livenessprobe" in process.stderr
